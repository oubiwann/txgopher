from zope.interface import implements

from twisted import plugin
from twisted.application import internet, service
from twisted.internet import endpoints, reactor
from twisted.python import log, usage

from txgopher import client, const, server, utils
from txgopher.scripts.options import ClientOptions, GopherOptions


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
        opts = ClientOptions()
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
    def getEndpoint(cls):
        endpointString = "tcp:host=%s:port=%s" % (cls.host, cls.port)
        return endpoints.clientFromString(reactor, endpointString)

    @classmethod
    def getFactory(cls):
        return client.GopherClientFactory(
            cls.host, cls.type, cls.selector, cls.query, cls.debug,
            cls.withBanner)

    @classmethod
    def run(cls):
        cls.parseOptions()
        d = cls.getEndpoint().connect(cls.getFactory())
        d.addErrback(log.msg)
        d.addCallback(cls.gotProtocol)
        reactor.run()
