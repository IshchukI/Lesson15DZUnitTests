import requests
from unittest import TestCase
from unittest.mock import patch
from datetime import datetime, timedelta
from http import cookies


url = "https://www.youtube.com/"
names = ['GPS', 'YSC', 'VISITOR_INFO1_LIVE', 'MNC']


class Test_youtube_cookies(TestCase):

    def setUp(self) -> None:
        respond = requests.get(url)
        self.cookies_dict = respond.cookies._cookies
        self.mock_coockie_MNC = cookies.SimpleCookie()
        self.mock_coockie_MNC['MNC'] = 'MNC'
        self.mock_coockie_MNC['MNC'].domain = '.youtube.com'
        self.mock_coockie_MNC['MNC'].secure = True
        self.mock_coockie_MNC['MNC'].version = 1
        self.mock_coockie_MNC['MNC'].expires = None

# youtube dictionary key tests
    def test_youtube_cookies_contain_name_GPS(self):
        self.assertTrue(names[0] in self.cookies_dict['.youtube.com']['/'].keys())
    def test_youtube_cookies_contain_name_YSC(self):
        self.assertTrue(names[1] in self.cookies_dict['.youtube.com']['/'].keys())
    def test_youtube_cookies_contain_name_VISITOR_INFO1_LIVE(self):
        self.assertTrue(names[2] in self.cookies_dict['.youtube.com']['/'].keys())
    def test_youtube_cookies_contain_name_MNC(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_coockie_MNC):
            self.assertTrue(names[3] in self.cookies_dict['.youtube.com']['/'].keys())

# youtube dictionary ['.youtube.com']['/']>GPS< tests
    def test_youtube_cookies_contain_name_GPS_domain(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[0]].domain, '.youtube.com')
    def test_youtube_cookies_contain_name_GPS_secure(self):
        self.assertTrue(self.cookies_dict['.youtube.com']['/'][names[0]].secure)
    def test_youtube_cookies_contain_name_GPS_version(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[0]].version, 0)
    def test_youtube_cookies_contain_name_GPS_expires(self):
        timestamp = self.cookies_dict['.youtube.com']['/'][names[0]].expires
        dt_timestamp = datetime.fromtimestamp(timestamp)
        dt = datetime.now() + timedelta(minutes=30) - timedelta(seconds=1)
        self.assertEqual(str(dt_timestamp), str(dt.strftime('%Y-%m-%d %H:%M:%S')))

# youtube dictionary ['.youtube.com']['/']>YCS< tests
    def test_youtube_cookies_contain_name_YCS_domain(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[1]].domain, '.youtube.com')
    def test_youtube_cookies_contain_name_YCS_secure(self):
        self.assertTrue(self.cookies_dict['.youtube.com']['/'][names[1]].secure)
    def test_youtube_cookies_contain_name_YCS_version(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[1]].version, 0)
    def test_youtube_cookies_contain_name_YCS_expires(self):
        self.assertIsNone(self.cookies_dict['.youtube.com']['/'][names[1]].expires)

# youtube dictionary ['.youtube.com']['/']>VISITOR_INFO1_LIVE< tests
    def test_youtube_cookies_contain_name_VISITOR_INFO1_LIVE_domain(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[2]].domain, '.youtube.com')
    def test_youtube_cookies_contain_name_VISITOR_INFO1_LIVE_secure(self):
        self.assertTrue(self.cookies_dict['.youtube.com']['/'][names[2]].secure)
    def test_youtube_cookies_contain_name_VISITOR_INFO1_LIVE_version(self):
        self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[2]].version, 0)
    def test_youtube_cookies_contain_name_VISITOR_INFO1_LIVE_expires(self):
        timestamp = self.cookies_dict['.youtube.com']['/'][names[2]].expires
        dt_timestamp = datetime.fromtimestamp(timestamp)
        dt = datetime.now() - timedelta(minutes=60) - timedelta(seconds=1) + timedelta(days=180)
        self.assertEqual(str(dt_timestamp), str(dt.strftime('%Y-%m-%d %H:%M:%S')))

    # youtube [Mock patch dict] dictionary ['.youtube.com']['/']>MNC< tests
    def test_youtube_cookies_contain_name_MNC_domain(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_coockie_MNC):
            self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[3]].domain, '.youtube.com')
    def test_youtube_cookies_contain_name_MNC_secure(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_coockie_MNC):
            self.assertTrue(self.cookies_dict['.youtube.com']['/'][names[3]].secure)
    def test_youtube_cookies_contain_name_MNC_version(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_coockie_MNC):
            self.assertEqual(self.cookies_dict['.youtube.com']['/'][names[3]].version, 1)
    def test_youtube_cookies_contain_name_MNC_expires(self):
        with patch.dict(self.cookies_dict['.youtube.com']['/'], self.mock_coockie_MNC):
            self.assertIsNone(self.cookies_dict['.youtube.com']['/'][names[3]].expires)









