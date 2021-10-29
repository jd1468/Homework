import unittest
import bs4
from rss_parser.rss_parser import RSSParser, CacheReader
from datetime import datetime


class TestRSSParser(unittest.TestCase):
    def setUp(self):
        self.parser1 = RSSParser()
        self.parser2 = RSSParser('https://www.onliner.by/feed')

        path = 'data/test_data/test.xml'

        with open(path, 'r') as file:
            self.soup = bs4.BeautifulSoup(file.read(), 'xml')

        self.item = self.soup.find_all('item')[0]
        self.ex_field = self.item.title
        self.non_ex_field = self.item.author
        self.ex_empty_field = self.item.comment

    def tearDown(self):
        pass

    def test_view_output(self):
        print('view_output() does not return anything')

    def test_parser_initiation(self):
        self.assertIsInstance(self.parser1.parser_initiation(), bs4.BeautifulSoup)
        self.assertNotIsInstance(self.parser2.parser_initiation(), list)

    def test_title_parser(self):
        self.assertIsInstance(self.parser1.title_parser(), dict)
        self.assertNotIsInstance(self.parser2.title_parser(), list)

    def test_title_view(self):
        print('title_view() does not return anything')

    def test_items_view(self):
        print('items_view() does not return anything')

    def test_item_parser(self):
        self.assertIsInstance(self.parser1.item_parser(self.item), dict)
        self.assertNotIsInstance(self.parser2.item_parser(self.item), list)

    def test_item_view(self):
        print('item_view() does not return anything')

    def test_empty_field_checker(self):
        self.assertEqual(self.parser1.empty_field_checker(self.ex_field), 'Pfizer Asks F.D.A. to Authorize Its '
                                                                          'Covid-19 Vaccine for Children 5 to 11')
        self.assertEqual(self.parser1.empty_field_checker(self.non_ex_field), 'field is not defined')
        self.assertEqual(self.parser1.empty_field_checker(self.ex_empty_field), 'field is empty')

    def test_feed_presentation(self):
        print('feed_presentation() does not return anything')

    def test_json_feed_generation(self):
        self.assertIsInstance(self.parser1.json_feed_generation(), str)
        self.assertNotIsInstance(self.parser2.json_feed_generation(), dict)

    def test_json_news_presentation(self):
        print('json_feed_presentation() does not return anything')


class TestCacheReader(unittest.TestCase):
    def setUp(self):
        d = '20211029'
        d = datetime.strptime(d, '%Y%m%d')
        self.cache_reader1 = CacheReader(d)
        self.cache_reader2 = CacheReader(d, limit=3, json_flag=True, source='https://www.times-series.co.uk/news/rss/')

        self.filename1 = '2021-10-29-01-04-23.json'
        self.filename2 = '2021-10-29-01-15-19.json'

    def tearDown(self):
        pass

    def test_view_output(self):
        print('view_output() does not return anything')

    def test_news_getter(self):
        self.assertIsInstance(self.cache_reader1.news_getter(), dict)
        self.assertNotIsInstance(self.cache_reader2.news_getter(), list)

    def test_single_file_date_checker(self):
        self.assertIsInstance(self.cache_reader1.single_file_date_checker(self.filename1), dict)
        self.assertNotIsInstance(self.cache_reader2.single_file_date_checker(self.filename2), list)

    def test_feed_presentation(self):
        print('feed_presentation() does not return anything')

    def test_title_presentation(self):
        print('title_presentation() does not return anything')

    def test_news_presentation(self):
        print('news_presentation() does not return anything')

    def test_single_news_presentation(self):
        print('single_news_presentation() does not return anything')

    def test_json_feed_generation(self):
        self.assertIsInstance(self.cache_reader1.json_feed_generation(), str)
        self.assertNotIsInstance(self.cache_reader2.json_feed_generation(), dict)

    def test_json_news_presentation(self):
        print('json_news_presentation() does not return anything')


if __name__ == '__main__':
    unittest.main()
