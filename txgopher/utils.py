from urlparse import urlparse

from txgopher import const


def getClientParams(url=""):
    result = urlparse(url)
    scheme = result.scheme
    hostAndPort = result.netloc.split(const.hostPortSeparator)
    if len(hostAndPort) == 1:
        [host] = hostAndPort
        port = const.port
    elif len(hostAndPort) == 2:
        host, port = hostAndPort
    # note that getting the item type from the URL can be handy, just not
    # always authoritative -- best to check the returned data directly
    itemAndSelector = result.path
    parts = itemAndSelector.split(const.selectorSeparator)
    item = parts[1]
    if item in const.ALL_ITEMS:
        parts.pop(1)
    selector = const.selectorSeparator.join(parts)
    return (item, selector, host, port)
