from mininet.net import Mininet
from mininet.node import Host, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
    net = Mininet(switch = OVSSwitch)
    
    info('*** Add Switch\n')
    s1 = net.addSwitch('s1')
    
    info('*** Add Hosts\n')
    h1 = net.addHost('h1', cls = Host, mac='00:00:00:00:00:01', ip = '10.0.0.1/24')
    h2 = net.addHost('h2', cls = Host, mac='00:00:00:00:00:02', ip = '10.0.0.2/24')
    
    info('*** Add Links\n')
    net.addLink(h1, s1, intName2 = 's1-eth1')
    net.addLink(h2, s1, intName2 = 's1-eth2')

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
