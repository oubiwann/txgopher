pageWidth = 67
hostPortSeparator = ":"
selectorSeparator = "/"
fieldSeparator = "\t"
scheme = "gopher"
# XXX need to change these to RemoteHost
defaultHost = "sdf.lonestar.org"
defaultPort = 70
defaultURL = "%s://%s/" % (scheme, defaultHost)
banner = r"""

 |         __|          |
  _|\ \ / (_ |  _ \ _ \   \   -_)  _|
\__| _\_\\___|\___/.__/_| _|\___|_|
                  _|
"""

FILE = "0"
DIR = "1"
CCSO = "2"
ERR = "3"
BINHEX = "4"
DOSBIN = "5"
UUENCODE = "6"
SEARCH = "7"
TELNET = "8"
BIN = "9"
DUP = "+"
TN3270 = "T"
GIF = "g"
IMG = "I"
DISCONNECT = "."
HTML = "h"
INLINE = "i"
SOUND = "s"
CAL = "c"
EVENT = "e"
MIME = "M"
DOC = "d"
JSON = "j"

FILES = [FILE, BINHEX, DOSBIN, UUENCODE, BIN, GIF, IMG, HTML, SOUND, DOC, JSON]
MENUS = [DIR, SEARCH]
RESOURCES = FILES + MENUS
ALL_ITEMS = RESOURCES + [CCSO, ERR, TELNET, DUP, TN3270, DISCONNECT, INLINE]


defaultItem = DIR
