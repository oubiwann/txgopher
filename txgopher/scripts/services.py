from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.python import log, usage

from txgopher import client, const, utils
from txgopher.scripts import options


class ClientService(object):
    """
    """
    @classmethod
    def gotProtocol(cls, protocol):
        """
        """
        banner = protocol.getBanner()
        if banner:
            print banner

    @classmethod
    def parseOptions(cls):
        opts = options.ClientOptions()
        opts.parseOptions()
        url = opts["url"]
        cls.debug = bool(opts["debug"])
        cls.withBanner = not bool(opts["no-banner"])
        if url:
            cls.type, cls.selector, cls.host, cls.port, cls.query = (
                utils.getClientParams(url))
        else:
            cls.type = opts["type"]
            cls.selector = opts["selector"]
            cls.host = opts["host"]
            cls.port = opts["port"]
            cls.query = opts["query"]

    @classmethod
    def run(cls):
        cls.parseOptions()
        endpoint = TCP4ClientEndpoint(reactor, cls.host, cls.port)
        factory = client.GopherClientFactory(
            cls.host, cls.type, cls.selector, cls.query, cls.debug,
            cls.withBanner)
        d = endpoint.connect(factory)
        d.addErrback(log.msg)
        d.addCallback(cls.gotProtocol)
        reactor.run()
