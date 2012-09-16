from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

from txgopher import const, protocol



class GopherClient(LineReceiver):
    """
    """
    def __init__(self, selector, debug=False):
        self.selector = selector
        self.debug = debug

    def getBanner(self, additionalText=""):
        if not self.factory.withBanner:
            return
        if not additionalText:
            additionalText = "A client for gopherspace.\n"
        separator = "-" * const.pageWidth
        return "%s%s\n%s%s" % (
            separator, const.banner, additionalText, separator)

    def sendCommand(self, selector=""):
        if not selector:
            selector = self.selector
        self.sendLine(selector)

    def handleGopherMapLine(self, line):
        parsed = protocol.GopherMapProtocol(self.factory.host, line)
        if self.factory.debug:
            print parsed
        elif parsed.type in const.RESOURCES:
            print "%s <link: %s>" % (parsed.display, parsed.url)
        else:
            print parsed.display

    def lineReceived(self, line):
        if line == const.DISCONNECT:
            self.transport.loseConnection()
            reactor.stop()
        elif self.factory.type == const.DIR:
            self.handleGopherMapLine(line)
        elif self.factory.type in const.FILES:
            print line


    def connectionMade(self):
        self.sendCommand()


class GopherClientFactory(Factory):
    """
    """
    def __init__(self, host, type, selector, debug=False, withBanner=True):
        self.host = host
        self.type = type
        self.selector = selector
        self.debug = debug
        self.withBanner = withBanner

    def buildProtocol(self, addr):
        protocol = GopherClient(self.selector, self.debug)
        protocol.factory = self
        return protocol
