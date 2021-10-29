# TODO
#  1. Implement URL-shortener
#  3. Description text can include inner tags. Get rid of them


import os
import requests
from bs4 import BeautifulSoup
import argparse
import json
import logging
from datetime import datetime

CACHE_PATH = 'data/cache'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)

file_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(funcName)s : %(message)s')
stream_formatter = logging.Formatter('%(levelname)s : %(message)s')
file_handler = logging.FileHandler('../rss_parser.log')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)
stream_handler.setLevel(logging.INFO)


logger.addHandler(file_handler)


class NewsNotFoundError(Exception):
    pass


class DirectoryNotFoundError(Exception):
    pass


class RSSParser:
    def __init__(self, url='https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', limit=-1, json_flag=False):
        logger.info('RSS Parser is starting')
        self.url = url
        self.limit = limit
        self.soup = self.parser_initiation()
        self.json_flag = json_flag

    def view_output(self):
        """
        Method defines how data will be presented, based on passed arguments. If json_flag was passed, data will be
        presented in a json format, otherwise - in a human readable way.

        :return: None
        """
        if self.json_flag is False:
            logger.info('Printing output in a human readable way')
            self.feed_presentation()
        else:
            logger.info('Printing output in JSON format')
            self.json_feed_presentation()

    def parser_initiation(self):
        """
        Method gets initial parser data. Gets raw xml from passed link and initializes soup
        :return: bs4.BeautifulSoup
        """
        logger.info('Getting content of RSS link...')
        try:
            raw_rss = requests.get(self.url)
            logger.info('Connection established successfully')
            return BeautifulSoup(raw_rss.content, 'xml')
        except Exception as err:
            logger.error(err)

    def title_parser(self):
        """
        Method works with soup object, parses hardcoded tags of xml 'title'
        :return: dict
        """
        logger.info('Parsing \'title\'...')
        title_dict = {}

        title = self.empty_field_checker(self.soup.find('title'))
        title_dict['title'] = title

        link = self.empty_field_checker(self.soup.find('link'))
        title_dict['link'] = link

        description = self.empty_field_checker(self.soup.find('description'))
        title_dict['description'] = description

        copyright_field = self.empty_field_checker(self.soup.find('copyright'))
        title_dict['copyright'] = copyright_field

        return title_dict

    def title_view(self):
        """
        Method fulfils viewer functionality, prints hardcoded tags of xml 'title' in a human readable way in a command
        line
        :return: None
        """
        title = self.title_parser()

        print(f'Feed: {title["title"]}')
        print(f'Site link: {title["link"]}')
        print(f'Description: {title["description"]}')
        print(f'Copyright: {title["copyright"]}')

    def items_view(self):
        """
        Method works as viewer for all items in xml, calling for item_view(),  viewer method for single item, while
        iterating through all items in xml
        :return: None
        """
        for item_id, item in enumerate(self.soup.find_all('item')):
            self.item_view(item)
            print(f'{20 * "-"}')
            if item_id == (self.limit - 1):
                break

    def item_parser(self, item):
        """
        Method works with passed single 'item' of xml , parses hardcoded tags of 'item'
        :param item: bs4.element.Tag
        :return: dict
        """
        logger.info('Parsing single \'item\'...')
        item_dict = {}

        title = self.empty_field_checker(item.title)
        item_dict['title'] = title

        description = self.empty_field_checker(item.description)
        item_dict['description'] = description

        link = self.empty_field_checker(item.link)
        item_dict['link'] = link

        date = self.empty_field_checker(item.pubDate)
        item_dict['date'] = date

        return item_dict

    def item_view(self, single_item):
        """
        Method works as a viewer for a single 'item' element from xml, prints hardcoded 'item' tags in a human readable
        way
        :param single_item: bs4.element.Tag
        :return: None
        """
        item = self.item_parser(single_item)

        print(f'Title: {item["title"]}')
        print(f'Date: {item["date"]}')
        print(f'{item["description"]}')
        print(f'Link: {item["link"]}')

    @staticmethod
    def empty_field_checker(field):
        """
        Method checks if tag field exists, and in case it exists, checks field content. In each case it returns
        corresponding answer.
        :param field: bs4.element.Tag
        :return: str
        """
        if field:
            if field.text:
                return field.text
            else:
                return 'field is empty'
        else:
            return 'field is not defined'

    def feed_presentation(self):
        """
        Method prints title and items, by calling corresponding methods
        :return: None
        """
        print('\n')
        print(f'Source: {self.url}')
        print('\n')
        self.title_view()
        print(f'\n{60 * "-"}\n')
        self.items_view()

    def json_feed_generation(self):
        """
        Method is called if 'json_flag' is True. Prints title and items as a json structure
        :return: None
        """
        logger.info('Generating json object...')
        title_dict = self.title_parser()

        items_dict = {}
        for item_id, item in enumerate(self.soup.find_all('item')):
            items_dict[str(item.title.text)] = self.item_parser(item)
            if item_id == self.limit - 1:
                break

        json_object = json.dumps({'source': self.url, 'header': title_dict, 'items': items_dict})
        return json_object

    def json_feed_presentation(self):
        json_object = self.json_feed_generation()
        print(json_object)

    def caching(self):
        filename = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + '.json'
        if os.path.exists(CACHE_PATH) is False:
            os.makedirs(CACHE_PATH)

        path = os.path.join(CACHE_PATH, filename)
        with open(path, 'w') as file:
            file.write(self.json_feed_generation())


class CacheReader:
    def __init__(self, datetime_date, limit=-1, json_flag=False, source=None):
        self.date = datetime_date.strftime('%a, %d %b %Y')
        self.limit = limit
        self.json_flag = json_flag
        self.source = source

    def view_output(self):
        """
        Method defines how data will be presented, based on passed arguments. If json_flag was passed, data will be
        presented in a json format, otherwise - in a human readable way.
        :return: None
        """
        if self.json_flag is False:
            logger.info('Getting output in a human readable way...')
            self.feed_presentation()
        else:
            logger.info('Getting output in a JSON format...')
            self.json_news_presentation()

    def news_getter(self):
        """
        Method parses directory looking for news
        :return: dict
        """
        logger.info('Getting news from cache...')
        news_counter = 0
        news_dict = {}
        if os.path.exists(CACHE_PATH) is False:
            raise DirectoryNotFoundError('No cache directory was found')

        for filename in sorted(os.listdir(CACHE_PATH), reverse=True):
            single_file_news = self.single_file_date_checker(filename)
            if bool(single_file_news) is False:
                continue

            title = single_file_news['source_title']['title']
            if single_file_news['source_title']['title'] not in news_dict.keys():
                news_dict[title] = {}
                news_dict[title]['header'] = single_file_news['source_title']
                news_dict[title]['news'] = {}

            for _ in single_file_news['news'].keys():
                if _ in news_dict[title]['news'].keys():
                    continue
                else:
                    news_dict[title]['news'][_] = single_file_news['news'][_]
                    news_counter += 1

                    if news_counter == self.limit:
                        return news_dict

        return news_dict

    def single_file_date_checker(self, filename):
        """
        Method parses single json file looking for news with date corresponding to one passed
        :param filename: str
        :return: dict
        """
        news_dict = {}
        path = os.path.join(CACHE_PATH, filename)
        with open(path, 'r') as file:
            content = json.load(file)

        source = content['source']
        if self.source is not None:
            logger.info('Filtering news by source...')
            if source == self.source:
                pass
            else:
                return news_dict

        title = content['header']
        items = content['items']
        for _ in list(items.keys()):
            date = items[_]['date']
            if self.date in date:
                if bool(news_dict) is False:
                    news_dict['source_title'] = title
                    news_dict['news'] = {}
                news_dict['news'][_] = items[_]

        return news_dict

    def feed_presentation(self):
        """
        Method prints source, title and news for corresponding date
        :return: None
        """
        news_dict = self.news_getter()
        if bool(news_dict) is False:
            raise NewsNotFoundError('No news were found for provided date')

        for source_title in news_dict.keys():
            print('\n')
            source = news_dict[source_title]['header']
            self.title_presentation(source)
            print(f'\n{60 * "-"}\n')

            news = news_dict[source_title]['news']
            self.news_presentation(news)

    @staticmethod
    def title_presentation(title):
        """
        Method prints title
        :param title: dict
        :return: None
        """
        print(f'Feed: {title["title"]}')
        print(f'Site link: {title["link"]}')
        print(f'Description: {title["description"]}')
        print(f'Copyright: {title["copyright"]}')

    def news_presentation(self, news):
        """
        Method prints news
        :param news: dict
        :return: None
        """
        for _ in news.keys():
            self.single_news_presentation(news[_])
            print(f'{20 * "-"}')

    @staticmethod
    def single_news_presentation(item):
        """
        Method prints single news
        :param item: dict
        :return: None
        """
        print(f'Title: {item["title"]}')
        print(f'Date: {item["date"]}')
        print(f'{item["description"]}')
        print(f'Link: {item["link"]}')

    def json_feed_generation(self):
        """
        Method generates json objects
        :return: str
        """
        logger.info('Generating JSON structure...')
        news_dict = self.news_getter()
        if bool(news_dict) is False:
            raise NewsNotFoundError('No news were found for provided date')

        json_object = json.dumps(news_dict)
        print(type(json_object), ' json object')
        return json_object

    def json_news_presentation(self):
        """
        Method prints json object
        :return: None
        """
        print(self.json_feed_generation())


def args_checker():
    """
    Function defines arguments, that will be read from command line input.
    Function first looks only for optional arguments, so that if optional argument '--date' was passed, program will not
    stop, and will work with corresponding logic, if '--date' was not found in passed arguments, than non-optional
    argument is added to arg parser and passed args are parsed once again
    :return: list
    """
    arg_parser = argparse.ArgumentParser(description='Python command-line RSS parser')

    arg_parser.add_argument('--date', help='get news from cache by date',
                            type=lambda d: datetime.strptime(d, '%Y%m%d'))
    arg_parser.add_argument('--json', help='print result in JSON format in stdout', action='store_true')
    arg_parser.add_argument('--verbose', help='outputs verbose status messages', action='store_true')
    arg_parser.add_argument('--limit', help='limit news topics if parameter is provided', type=int, default=-1)

    options, remainder = arg_parser.parse_known_args()
    if options.date:
        arg_parser.add_argument('--source', help='RSS URL that will be used as a filter for cached news')
    else:
        arg_parser.add_argument('url', help='RSS URL')
        arg_parser.add_argument('-v', '--version', help='print version info', action='version', version='1.1')

    args_list = arg_parser.parse_args()
    return args_list


def main():
    """
    Function that runs whole app loop. Was implemented for setuptools, for 'entry_points'
    :return: None
    """
    # parser = RSSParser('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')

    args = args_checker()
    if args.verbose:
        logger.addHandler(stream_handler)

    logger.info(f'{20 * "-"}Starting session{20 * "-"}')

    if args.date:
        cache_reader = CacheReader(args.date, args.limit, args.json, args.source)
        try:
            cache_reader.view_output()
        except DirectoryNotFoundError as err:
            logger.error(err)
        except NewsNotFoundError as err:
            logger.error(err)
    else:
        parser = RSSParser(args.url, args.limit, args.json)
        parser.view_output()
        parser.caching()

    # parser = RSSParser()
    # parser.view_output()

    logger.info(f'{20 * "-"}Session finished{20 * "-"}\n')


if __name__ == '__main__':
    main()
