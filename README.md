#RSS READER

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


##Format Converters

All export results (created files) are placed in 'cwd/data/export/format_name'

###PDF Converter
PdfConverter works for docs without cyrillic letters, generates links, but not convert images, embedded in description tag as links into actual images

###HTML Converter
HTML Converter creates html tags structure, that is than written into 'filename'.html. Links work through <a href=""></a>. Images embedded in description as links are automatically represented as actual images

###EPUB Converter
EPUB Converter uses html structure from html converter and converts html structure string into epub file with side library
