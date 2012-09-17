from twisted.python import usage

from txgopher import const


class ClientOptions(usage.Options):
    """
    """
    optFlags = [
        ["debug", "d", "run in debug mode"],
        ["no-banner", "b", "run without the banner"],
    ]
    optParameters = [
        ["url", "u", const.defaultURL, "a gopherspace URL"],
        ["host", "h", None, "a gopher host"],
        ["port", "p", const.defaultPort, "a gopher server's port"],
        ["type", "t", const.DIR, "a gopher item type"],
        ["selector", "s", None, "a gopher selector (path)"],
        ["query", "q", None, "a gopher search query"],
    ]
