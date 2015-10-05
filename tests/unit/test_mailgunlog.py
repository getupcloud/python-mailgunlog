from tests import *
from mailgunlog.mailgunlog import strdate_to_rfc2822

class TestExample(unittest.TestCase):

    def test_strdate_to_rfc2822(self):
        self.assertEqual(strdate_to_rfc2822('2015/01/01'), 'Thu, 01 Jan 2015 23:59:59 -0000')
        self.assertEqual(strdate_to_rfc2822('2015/01/01', midnight=True), 'Thu, 01 Jan 2015 00:00:00 -0000')
