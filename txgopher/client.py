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

    def sendCommand(self, selector="", query=""):
        if not selector:
            selector = self.selector
        command = selector
        if query:
            command = "%s\t%s" % (command, query)
        if self.factory.debug:
            print "Sending command '%s' ..." % command
        self.sendLine(command)

    def handleGopherMapLine(self, line):
        parsed = protocol.GopherMapProtocol(self.factory.host, line)
        if self.factory.debug:
            print parsed
        elif parsed.type in const.RESOURCES:
            print "%s <link %s>" % (parsed.display, parsed.url)
        else:
            print parsed.display

    def disconnect(self):
        if self.factory.debug:
            print "Disconnecting client ..."
        if self.transport.connected:
            self.transport.loseConnection()
        if reactor.running:
            reactor.stop()

    def lineReceived(self, line):
        if line == const.DISCONNECT:
            self.disconnect()
        elif self.factory.type in const.MENUS:
            self.handleGopherMapLine(line)
        elif self.factory.type in const.FILES:
            print line

    def connectionMade(self):
        if self.factory.debug:
            print "Connection made to %s." % self.factory.host
        args = [self.selector]
        if self.factory.type == const.SEARCH:
            args.append(self.factory.query)
        self.sendCommand(*args)

    def connectionLost(self, reason):
        if self.factory.debug:
            print "Connection lost: %s" % reason
        self.disconnect()


class GopherClientFactory(Factory):
    """
    """
    def __init__(self, host, type, selector, query="", debug=False,
                 withBanner=True):
        self.host = host
        self.type = type
        self.selector = selector
        self.query = query
        self.debug = debug
        self.withBanner = withBanner

    def buildProtocol(self, addr):
        protocol = GopherClient(self.selector, self.debug)
        protocol.factory = self
        return protocol
