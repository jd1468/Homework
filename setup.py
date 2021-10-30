import setuptools
setuptools.setup(
    name='rss_reader',
    version='1.3',
    packages=setuptools.find_packages(),
    description='RSS-Reader is a program for news xml parsing and presentin it in a human readable way. Additional '
                'feature is a JSON presentation, which allow to present news as a json structure',
    install_requires=['beautifulsoup4==4.10.0', 'bs4==0.0.1', 'certifi==2021.5.30', 'charset-normalizer==2.0.6',
                      'colorama==0.4.4', 'colorlog==6.5.0', 'cssselect==1.1.0', 'fpdf2==2.4.5', 'html2epub==1.2',
                      'idna==3.2', 'Jinja2==3.0.2', 'lxml==4.6.3', 'MarkupSafe==2.0.1', 'Pillow==8.4.0',
                      'pyquery==1.4.3', 'requests==2.26.0', 'soupsieve==2.2.1', 'urllib3==1.26.7'],
    package_date={'': ['data']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rss_reader =rss_parser.rss_parser:main'
        ]
    },
)
