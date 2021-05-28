from django.test import TestCase
from stock.bot_rules.request_parcer import stock_parser


# Create your tests here.
class BotTest(TestCase):

    def test_parse_stock_data(self):

        raw_string= ('Symbol,Date,Time,Open,High,Low,Close,'
                     'Volume\r\nAAPL.US,2021-05-27,22:00:'
                     '18,126.44,127.64,125.08,125.28,94503056\r\n')
        expected_data = '126.44,127.64,125.08,125.28,94503056'

        res = stock_parser(raw_string)

        assert res == expected_data

