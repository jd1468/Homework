import unittest
import bs4
from rss_parser.rss_parser import RSSParser, CacheReader, HTMLConverter
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


class TestHTMLConverter(unittest.TestCase):
    def setUp(self):
        news_dict = {'Times Series | News':
                         {'source': 'https://www.times-series.co.uk/news/rss/',
                          'header': {'title': 'Times Series | News',
                                     'link': 'https://www.times-series.co.uk/news/rss/',
                                     'description': 'Times Series News', 'copyright': 'field is not defined'},
                          'news': {'Bonfire Night 2021: Top 10 places to watch the fireworks':
                                       {'title': 'Bonfire Night 2021: Top 10 places to watch the fireworks',
                                        'description': "Bonfire Night will soon be upon us and Hertfordshire's night "
                                                       "skies will light up a multitude of fireworks displays.",
                                        'link': 'https://www.times-series.co.uk/news/19681990.bonfire-night-2021-top-'
                                                '10-places-watch-fireworks/?ref=rss',
                                        'date': 'Sat, 30 Oct 2021 13:00:00 +0100'},
                                   'Partial Closure Order in place at property in Potters Bar':
                                       {'title': 'Partial Closure Order in place at property in Potters Bar',
                                        'description': 'Action has been taken to prevent further anti-social behaviour '
                                                       'and suspected drug use at a flat in Potters Bar.',
                                        'link': 'https://www.times-series.co.uk/news/19683686.partial-closure-order-'
                                                'place-property-potters-bar/?ref=rss',
                                        'date': 'Sat, 30 Oct 2021 10:09:12 +0100'}}}}
        self.news_list = ['<div><h2>Times Series | News</h2><p>Link: <a href="https://www.times-series.co.uk/news/rss/">'
                     'https://www.times-series.co.uk/news/rss/</a></p><p>Description: Times Series News</p>'
                     '<p>Copyright: field is not defined</p><p>------------------------------------------------------'
                     '------</p><h3>Bonfire Night 2021: Top 10 places to watch the fireworks</h3><p>Description: '
                     'Bonfire Night will soon be upon us and Hertfordshire\'s night skies will light up a multitude of '
                     'fireworks displays.</p><p>Link: <a href="https://www.times-series.co.uk/news/19681990.bonfire-'
                     'night-2021-top-10-places-watch-fireworks/?ref=rss">https://www.times-series.co.uk/news/19681990.'
                     'bonfire-night-2021-top-10-places-watch-fireworks/?ref=rss</a></p><p>Date: Sat, 30 Oct 2021 '
                     '13:00:00 +0100</p><p>------------------------------------------------------------</p><h3>Partial '
                     'Closure Order in place at property in Potters Bar</h3><p>Description: Action has been taken to '
                     'prevent further anti-social behaviour and suspected drug use at a flat in Potters Bar.</p>'
                     '<p>Link: <a href="https://www.times-series.co.uk/news/19683686.partial-closure-order-place-'
                     'property-potters-bar/?ref=rss">https://www.times-series.co.uk/news/19683686.partial-closure-order'
                     '-place-property-potters-bar/?ref=rss</a></p><p>Date: Sat, 30 Oct 2021 10:09:12 +0100</p><p>-'
                     '-----------------------------------------------------------</p></div>']

        news_dict_content = news_dict[list(news_dict.keys())[0]]
        self.source = news_dict_content['source']
        self.title = news_dict_content['header']
        self.news = news_dict_content['news']

        self.html_converter1 = HTMLConverter(news_dict)
        self.html_converter2 = HTMLConverter(news_dict)

    def test_write_to_html(self):
        self.assertIsInstance(self.html_converter1.write_to_html(), str)
        self.assertNotIsInstance(self.html_converter2.write_to_html(), dict)

    def test_source_creation(self):
        self.assertIsInstance(self.html_converter1.source_creation(self.source), str)
        self.assertNotIsInstance(self.html_converter2.source_creation(self.source), dict)

    def test_title_creation(self):
        self.assertIsInstance(self.html_converter1.title_creation(self.title), str)
        self.assertNotIsInstance(self.html_converter2.title_creation(self.title), list)

    def test_news_creation(self):
        self.assertIsInstance(self.html_converter1.news_creation(self.news), str)
        self.assertNotIsInstance(self.html_converter2.news_creation(self.news), dict)

    def test_html_combination(self):
        self.assertIsInstance(self.html_converter1.html_combination(self.news_list), str)
        self.assertNotIsInstance(self.html_converter2.html_combination(self.news_list), list)

    def test_html_creation(self):
        print('html_creation() does not return anything')

    def test_dir_creation(self):
        print('dir_creation() does not return anything')






if __name__ == '__main__':
    unittest.main()
