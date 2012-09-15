from urlparse import urlparse

from txgopher import const


def getClientParams(url=""):
    result = urlparse(url)
    scheme = result.scheme
    hostAndPort = result.netloc.split(":")
    if len(hostAndPort) == 1:
        [host] = hostAndPort
        port = const.port
    elif len(hostAndPort) == 2:
        host, port = hostAndPort
    selector = result.path
    return (selector, host, port)
