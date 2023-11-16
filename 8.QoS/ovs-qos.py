from mininet.net import Mininet
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
    net = Mininet()
    
    info('*** Add Switch\n')
    s1 = net.addSwitch('s1', cls = OVSKernelSwitch, failMode = 'standalone')
    s2 = net.addSwitch('s2', cls = OVSKernelSwitch, failMode = 'standalone')
    
    info('*** Add Hosts\n')
    h1 = net.addHost('h1', cls = Host, ip = '10.0.0.1/24')
    h2 = net.addHost('h2', cls = Host, ip = '10.0.0.2/24')
    h3 = net.addHost('h3', cls = Host, ip = '10.0.0.3/24')
    h4 = net.addHost('h4', cls = Host, ip = '10.0.0.4/24')
    
    info('*** Add Links\n')
    net.addLink(h1, s1, intName2 = 's1-eth1')
    net.addLink(h3, s1, intName2 = 's1-eth2')
    net.addLink(h2, s2, intName2 = 's2-eth1')
    net.addLink(h4, s2, intName2 = 's2-eth2')
    net.addLink(s1, s2, intName1 = 's1-eth3', intName2 = 's2-eth3')
    
    info('*** Starting network\n')
    net.build()
    net.start()

    info('*** Enter command line interface\n')
    CLI(net)

    info('*** Stop network emulation\n')
    net.stop()
    
if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
