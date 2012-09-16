from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

from txgopher import const


def welcome(additionalText=""):
    if not additionalText:
        additionalText = "A client for gopherspace.\n"
    return "%s\n%s" % (const.banner, additionalText)


class GopherClient(LineReceiver):
    """
    """
    def __init__(self, selector):
        self.selector = selector

    def lineReceived(self, line):
        print line
        if line == ".":
            self.transport.loseConnection()
            reactor.stop()

    def connectionMade(self):
        self.sendLine(self.selector)


class GopherClientFactory(Factory):
    """
    """
    def __init__(self, selector):
        self.selector = selector

    def buildProtocol(self, addr):
        return GopherClient(self.selector)
