from twisted.python import usage

from txgopher import const


class BaseOptions(usage.Options):
    """
    """
    optFlags = [
        ["debug", "d", "run in debug mode"],
        ["no-banner", "b", "run without the banner"],
    ]
    optParameters = [
        ["port", "p", const.defaultPort, "a gopher server's port"],
    ]


class ClientOptions(BaseOptions):
    """
    """
    optParameters = [
        ["url", "u", const.defaultURL, "a gopherspace URL"],
        ["host", "h", None, "a gopher host"],
        ["type", "t", const.DIR, "a gopher item type"],
        ["selector", "s", None, "a gopher selector (path)"],
        ["query", "q", None, "a gopher search query"],
    ]


class ServerOptions(BaseOptions):
    """
    """


class GopherOptions(usage.Options):
    """
    """
    subCommands = [
        ["server", None, ServerOptions, "configure the server"],
    ]
