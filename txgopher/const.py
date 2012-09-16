pageWidth = 67
hostPortSeparator = ":"
selectorSeparator = "/"
fieldSeparator = "\t"
scheme = "gopher"
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
INFO = "i"
SOUND = "s"
JSON = "j"

FILES = [FILE, BINHEX, DOSBIN, UUENCODE, BIN, GIF, IMG, HTML, SOUND, JSON]
RESOURCES = FILES + [DIR, SEARCH]
ALL_ITEMS = RESOURCES + [CCSO, ERR, TELNET, DUP, TN3270, DISCONNECT, INFO]


defaultItem = DIR
