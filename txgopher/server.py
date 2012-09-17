from twisted.python import log
from twisted.internet import protocol


class GopherServer(protocol.Protocol):
    """
    """
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        log.msg("Remote host %s:%s connected ..." % self.transport.client)
        #import pdb;pdb.set_trace()
        self.transport.write("Welcome :-)\n")

    def connectionLost(self, reason):
        log.msg("Remote host %s:%s disconnected." % self.transport.client)
        self.transport.write("Good-bye :-(\n")

    def dataReceived(self, data):
        params = self.transport.client + (str(data),)
        log.msg("Data received from %s:%s: %s" % params)
        self.transport.write("You asked for the following: %s" % str(data))


class GopherServerFactory(protocol.Factory):
    """
    """
    def buildProtocol(self, addr):
        return GopherServer(self)
