from txgopher import const


class GopherItemTypes(object):
    """
    Historical notes:

    A CCSO name-server or Ph protocol was an early form of database search on
    the web. In its most common form it was used to look up information such as
    phone numbers and e-mail addresses. Today this service has been largely
    replaced by LDAP. It was used mainly in the early-to-middle 1990s. The
    name-server was developed by Steve Dorner at the University of Illinois at
    Urbana-Champaign.

    BinHex, short for "binary-to-hexadecimal", is a binary-to-text encoding
    system that was used on the Mac OS for sending binary files through e-mail.
    It is similar to Uuencode, but combined both "forks" of the Mac file system
    together along with extended file information. BinHexed files take up more
    space than the original files, but will not be corrupted by non-"8-bit
    clean" software.

    Redundant server applies to a duplicated server. The information contained
    within is a duplicate of the primary server. The primary server is defined
    as the last DirEntity that is has a non-plus "Type" field. The client
    should use the transaction as defined by the primary server Type field.

    Telnet 3270, or TN3270 describes either the process of sending and
    receiving data streams of the IBM 3270 block-oriented terminals using the
    Telnet protocol or the software that emulates a 3270 class terminal that
    communicates using that process. TN3270 allows a 3270 terminal emulator to
    communicate over a TCP/IP network instead of an SNA network. (Standard
    telnet clients cannot be used as a substitute for TN3270 clients, as they
    use fundamentally different techniques for exchanging data.)
    """
    map = {
        "file": const.FILE,
        "directory": const.DIR,
        # see docstring
        "ccsoNameServer": const.CCSO,
        "error": const.ERR,
        # see docstring
        "binHex": const.BINHEX,
        # DOS binary archive of some sort
        "dosBin": const.DOSBIN,
        # a UNIX uuencoded file
        "uuencode": const.UUENCODE,
        "searchServer": const.SEARCH,
        "telnetSession": const.TELNET,
        "binaryFile": const.BIN,
        # see docstring
        "redundantServer": const.DUP,
        # see docstring
        "tn3270Session": const.TN3270,
        "gif": const.GIF,
        "image": const.IMG,
    }

    def __init__(self):
        self.lookup = dict([(val, key) for key, val in self.map.items()])

    def __getattribute__(self, name):
        try:
            return super(GopherItemTypes, self).__getattribute__(name)
        except AttributeError:
            value = self.get(name)
            if value is not None:
                return value
            else:
                raise AttributeError()

    def get(self, value):
        value = str(value)
        if value in self.map.keys():
            return self.map[value]
        elif value in self.map.values():
            return self.lookup[value]
        else:
            return None


class GopherPlusItemTypes(GopherItemTypes):
    """
    """


class GopherComprehensiveItemTypes(GopherPlusItemTypes):
    """
    """
    map = GopherPlusItemTypes.map
    map.update({
        "calendar": const.CAL,
        "disconnect": const.DISCONNECT,
        "event": const.EVENT,
        "html": const.HTML,
        "inline": const.INLINE,
        "multipart": const.MIME,
        "sound": const.SOUND,
    })


class TXGopherItemTypes(GopherComprehensiveItemTypes):
    """
    """
    map = GopherComprehensiveItemTypes.map
    map.update({
        "json": const.JSON
    })


class GopherMapProtocol(object):
    """
    """
    def __init__(self, host, line):
        self.host = host
        self.type = ""
        self.display = ""
        self.selector = ""
        self.itemhost = ""
        self.port = ""
        self.error = ""
        self.url = ""
        self.parseLine(line)

    def parseLine(self, line):
        if not line:
            return
        self.type = line[0]
        self.typeName = GopherComprehensiveItemTypes().get(self.type)
        if self.type == const.DISCONNECT:
            return
        self.display, self.selector, self.itemhost, self.port = line[1:].split(
            const.fieldSeparator)
        self.url = "%s://%s/%s%s" % (
            const.scheme, self.itemhost, self.type, self.selector)

    def __repr__(self):
        repr = "<%s type='%s'" % (self.__class__.__name__, self.typeName)
        if self.type != const.DISCONNECT:
            repr += ", data='%s'" % self.display
        if self.type == const.DIR:
            repr += " selector='%s'" % self.selector
        if (self.type not in [const.DISCONNECT, const.INLINE]
            and self.itemhost != self.host):
            repr += " host='%s'" % self.itemhost
        return repr + ">"
