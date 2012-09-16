from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

from txgopher import const, protocol


def welcome(additionalText=""):
    if not additionalText:
        additionalText = "A client for gopherspace.\n"
    separator = "-" * const.pageWidth
    return "%s%s\n%s%s" % (
        separator, const.banner, additionalText, separator)


class GopherClient(LineReceiver):
    """
    """
    def __init__(self, host, selector, debug=False):
        self.host = host
        self.selector = selector
        self.debug = debug

    def sendCommand(self, selector=""):
        if not selector:
            selector = self.selector
        self.sendLine(selector)

    def lineReceived(self, line):
        parsed = protocol.GopherLineProtocol(self.host, line)
        if self.debug:
            print parsed
        else:
            print parsed.display
        if parsed.type == const.DISCONNECT:
            self.transport.loseConnection()
            reactor.stop()

    def connectionMade(self):
        self.sendCommand()


class GopherClientFactory(Factory):
    """
    """
    def __init__(self, host, selector, debug=False):
        self.host = host
        self.selector = selector
        self.debug = debug

    def buildProtocol(self, addr):
        return GopherClient(self.host, self.selector, self.debug)
