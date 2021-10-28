import setuptools
setuptools.setup(
    name='rss_reader',
    version='1.0',
    packages=setuptools.find_packages(),
    description='RSS-Reader is a program for news xml parsing and presentin it in a human readable way. Additional '
                'feature is a JSON presentation, which allow to present news as a json structure',
    install_requires=['beautifulsoup4>=4.10.0', 'bs4>=0.0.1', 'certifi>=2021.5.30', 'charset-normalizer>=2.0.6',
                      'idna>=3.2', 'lxml>=4.6.3', 'requests>=2.26.0', 'soupsieve>=2.2.1', 'urllib3>=1.26.7'],
    include_package_date=True,
    entry_points={
        'console_scripts': [
            'rss_reader =rss_parser.rss_parser:main'
        ]
    },
)
