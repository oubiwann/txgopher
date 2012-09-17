from twisted.internet import protocol


class GopherServer(protocol.Protocol):
    """
    """
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.transport.write("Welcome :-)")

    def connectionLost(self, reason):
        self.transport.write("Good-bye :-(")

    def dataReceived(self, data):
        self.transport.write(data)


class GopherServerFactory(protocol.Factory):
    """
    """
    def buildProtocol(self, addr):
        return GopherServer(self)
