import unittest
import bs4
from rss_parser import RSSParser
import os


class TestRSSParser(unittest.TestCase):
    def setUp(self):
        self.parser1 = RSSParser()
        self.parser2 = RSSParser('https://www.onliner.by/feed')

        path = os.path.join(os.path.dirname(os.getcwd()), 'data/test_data/test.xml')

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

    def test_json_feed_presentation(self):
        print('json_feed_presentation() does not return anything')


if __name__ == '__main__':
    unittest.main()
