from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.node import Host, Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

def myNetwork():
    net = Mininet()
    
    info('*** Add Switches\n')
    s1 = net.addSwitch('s1', cls = OVSKernelSwitch, failMode = 'standalone')
    s2 = net.addSwitch('s2', cls = OVSKernelSwitch, failMode = 'standalone')
        
    info('*** Add Routers\n')    
    r1 = net.addHost('r1', cls = Node, intf = 'r1-eth0', ip = '192.168.1.1/24')
    r1.cmd('sysctl net.ipv4.ip_forward = 1')
    r2 = net.addHost('r2', cls = Node, intf = 'r2-eth0', ip = '192.168.2.1/24')
    r2.cmd('sysctl net.ipv4.ip_forward = 1')
    r3 = net.addHost('r3', cls = Node, intf = 'r3-eth0', ip = '203.0.13.2/30')
    r3.cmd('sysctl net.ipv4.ip_forward = 1')

    info('*** Add Hosts\n')
    h1 = net.addHost('h1', cls = Host, ip = '192.168.1.10/24', defaultRoute = 'via 192.168.1.1')
    h2 = net.addHost('h2', cls = Host, ip = '192.168.2.10/24', defaultRoute = 'via 192.168.2.1')
    
    info('*** Add Links\n')

    info('*** Switches to Routers Links\n')
    net.addLink(s1, r1, intName1 = 's1-eth1', intName2 = 'r1-eth0')
    net.addLink(s2, r2, intName1 = 's2-eth1', intName2 = 'r2-eth0')
    
    info('*** Router to Router Links\n')
    net.addLink(r1, r3, intfName1='r1-eth1', intfName2='r3-eth0', params1={'ip': '203.0.13.1/30'}, params2={'ip': '203.0.13.2/30'})
    net.addLink(r3, r2, intfName1='r3-eth1', intfName2='r2-eth1', params1={'ip': '203.0.23.2/30'}, params2={'ip': '203.0.23.1/30'})

    info('*** Host to Switch Links\n')
    net.addLink(h1, s1, intName1 = 'h1-eth0', intName2 = 's1-eth2')
    net.addLink(h2, s2, intName1 = 'h2-eth0', intName2 = 's2-eth2')

    info('*** Starting network\n')
    net.build()

    info('*** Starting switches\n')
    net.start()

    info('*** Enter command line interface\n')
    CLI(net)

    info('*** Stop network emulation\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
