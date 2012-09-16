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
    """
    map = {
        "file": 0,
        "directory": 1,
        # see docstring
        "ccsoNameServer": 2,
        "error": 3,
        # see docstring
        "binHex": 4,
        # DOS binary archive of some sort
        "dosBin": 5,
        # a UNIX uuencoded file
        "uuencode": 6,
        "searchServer": 7,
        "telnetSession": 8,
        "binaryFile": 9,
        "redundantServer": "+",
        "tn3270Session": "T",
        "gif": "g",
        "image": "I",
    }

    lookup = dict([(val, key) for key, val in map.items()])

    def __getattribute__(self, name):
        try:
            return super(GopherItemTypes, self).__getattribute__(name)
        except AttributeError:
            value = self.get(name)
            #import pdb;pdb.set_trace()
            if value is not None:
                return value
            else:
                raise AttributeError()

    def get(self, value):
        if value in self.map.keys():
            return self.map[value]
        elif value in self.map.values():
            return self.lookup[value]
        else:
            return None


class GopherPlusItemTypes(GopherItemTypes):
    """
    """
