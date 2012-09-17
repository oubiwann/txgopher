from twisted.internet import protocol


class GopherServer(protocol.Protocol):
    """
    """
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "Welcome! There are currently %d open connections.\n" %
            (self.factory.numProtocols,))

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data):
        self.transport.write(data)


class GopherServerFactory(protocol.Factory):
    """
    """
    def buildProtocol(self, addr):
        return GopherServer()
