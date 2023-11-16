from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, Controller, RemoteController
from mininet.log import setLogLevel, info
from mininet.cli import CLI

def topology():
    info("*** Create a network with OVSKernelSwitch switching capability\n")
    net = Mininet(switch=OVSKernelSwitch)

    info("*** Create and add a controller running locally and listening at port 6653\n")
    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6653, protocols="OpenFlow13")
    info("*** Create and add a controller running locally and listening at port 6654\n")
    c1 = net.addController('c1', controller=Controller, ip='127.0.0.1', port=6654, protocols="OpenFlow13")
    info("*** Add a controller running remotely and listening at port 6633\n")
    c2 = net.addController('c2', controller=RemoteController, ip='192.168.100.93', port=6633, protocols="OpenFlow13")

    info("*** Create host h1 with IP address 10.0.0.1/24\n")
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    info("*** Create host h2 with IP address 10.0.0.2/24\n")
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    info("*** Create host h3 with IP address 10.0.0.3/24\n")
    h3 = net.addHost('h3', ip='10.0.0.3/24')
    info("*** Create host h4 with IP address 10.0.0.4/24\n")
    h4 = net.addHost('h4', ip='10.0.0.4/24')
    info("*** Create host h5 with IP address 10.0.0.5/24\n")
    h5 = net.addHost('h5', ip='10.0.0.5/24')
    info("*** Create host h6 with IP address 10.0.0.6/24\n")
    h6 = net.addHost('h6', ip='10.0.0.6/24')
    
    info("*** Create switch s1\n")
    s1 = net.addSwitch('s1')
    info("*** Create switch s2\n")
    s2 = net.addSwitch('s2')
    info("*** Create switch s3\n")
    s3 = net.addSwitch('s3')

    info("*** Add a link between host h1 and switch s1\n")
    net.addLink(h1, s1)
    info("*** Add a link between host h2 and switch s1\n")
    net.addLink(h2, s1)
    info("*** Add a link between host h3 and switch s2\n")
    net.addLink(h3, s2)
    info("*** Add a link between host h4 and switch s2\n")
    net.addLink(h4, s2)
    info("*** Add a link between host h5 and switch s3\n")
    net.addLink(h5, s3)
    info("*** Add a link between host h6 and switch s3\n")
    net.addLink(h6, s3)

    info("*** Add a link between switch s1 and s2\n")
    net.addLink(s1, s2)
    info("*** Add a link between switch s2 and s3\n")
    net.addLink(s2, s3)

    info("*** Build the network emulation\n")
    net.build()

    info("*** Start controller c0\n")
    c0.start()
    info("*** Start controller c1\n")
    c1.start()

    info("*** Start switch s1 with controller c0\n")
    s1.start([c0])
    info("*** Start switch s2 with controller c1\n")
    s2.start([c1])
    info("*** Start switch s3 with controller c2\n")
    s3.start([c2])

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
