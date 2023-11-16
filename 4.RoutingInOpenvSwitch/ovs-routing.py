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
    h1 = net.addHost('h1', cls = Host, ip = '10.0.1.10/24', mac = '00:00:00:00:00:01', defaultRoute = 'via 10.0.1.1')
    h2 = net.addHost('h2', cls = Host, ip = '10.0.2.10/24', mac = '00:00:00:00:00:02', defaultRoute = 'via 10.0.2.1')

    info('*** Add Links\n')
    net.addLink(h1, s1, intName2 = 's1-eth1')
    net.addLink(h2, s2, intName2 = 's2-eth1')
    net.addLink(s1, s2, intName1 = 's1-eth2', intName2 = 's2-eth2')

    info('*** Starting network\n')
    net.build()

    info('*** Starting switches\n')
    net.start()
    
    info('IP(h1-eth0) = ', h1.IP(intf='h1-eth0'), '\n')
    info('MAC(h1-eth0) = ', h1.MAC(intf='h1-eth0'), '\n')
    info('IP(h2-eth0) = ', h2.IP(intf='h2-eth0'), '\n')
    info('MAC(h2-eth0) = ', h2.MAC(intf='h2-eth0'), '\n')
    s1.setMAC('00:00:00:00:00:03', intf='s1-eth2')
    info('MAC(s1-eth2) = ', s1.MAC(intf = 's1-eth2'), '\n')
    s2.setMAC('00:00:00:00:00:04', intf='s2-eth2')
    info('MAC(s2-eth2) = ', s2.MAC(intf = 's2-eth2'), '\n')

    info('*** Enter command line interface\n')
    CLI(net)

    info('*** Stop network emulation\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
