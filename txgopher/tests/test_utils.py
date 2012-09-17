from twisted.trial import unittest

from txgopher import utils


class UtilsTestCase(unittest.TestCase):
    """
    """
    def test_getClientParamsNoURL(self):
        result = utils.getClientParams()
        expected = ('1', '/', 'sdf.lonestar.org', 70, '')
        self.assertEqual(result, expected)

    def test_getClientParamsWithItemType(self):
        url = "gopher://hostname:9999/0/path/to/a/file.txt"
        result = utils.getClientParams(url)
        expected = ('0', '/path/to/a/file.txt', 'hostname', '9999', '')
        self.assertEqual(result, expected)

    def test_getClientParamsWithoutItemType(self):
        url = "gopher://hostname:9999/path/to/a/file.txt"
        result = utils.getClientParams(url)
        expected = ('1', '/path/to/a/file.txt', 'hostname', '9999', '')
        self.assertEqual(result, expected)

    def test_getClientParamsWithSearchAndQuery(self):
        url = "gopher://hostname:9999/7?search text"
        result = utils.getClientParams(url)
        expected = ('7', '/', 'hostname', '9999', 'search text')
        self.assertEqual(result, expected)
