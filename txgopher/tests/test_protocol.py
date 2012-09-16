from twisted.trial import unittest

from txgopher import protocol


class GopherItemTypesTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        self.itemType = protocol.GopherItemTypes()

    def test_getByKey(self):
        self.assertEqual(self.itemType.get("file"), '0')
        self.assertEqual(self.itemType.get("uuencode"), '6')
        self.assertEqual(self.itemType.get("binaryFile"), '9')

    def test_getByValue(self):
        self.assertEqual(self.itemType.get(0), "file")
        self.assertEqual(self.itemType.get(1), "directory")
        self.assertEqual(self.itemType.get(2), "ccsoNameServer")

    def test_getByAttribute(self):
        self.assertEqual(self.itemType.file, '0')
        self.assertEqual(self.itemType.tn3270Session, "T")
        self.assertEqual(self.itemType.gif, "g")
