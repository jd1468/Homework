##JSON Structures
{'source': link,
'header':
    {'title': title.title,
     'link': title.link,
     'description': title.description,
     'copyright': title.copyright
    }
 'items':
    {item.title:
        {'title': item.title,
         'description': item.description,
         'link': item.link,
         'date': item.pubDate
        }
}
        
This JSON structure is used in iteration 1 for json presentation  and in iteration 3 for news caching


{title.title:
    {'source': link,
    'header':
        {'title': title.title,
         'link': title.link,
         'description': title.description,
         'copyright': title.copyright
        }
     'news':
        {item.title:
            {'title': item.title,
             'description': item.description,
             'link': item.link,
             'date': item.pubDate
            }
    }
}

This JSON structure was used for json presentation in iteration 3 for finding cached news by RSS Source. Link to rss was considered as  a source