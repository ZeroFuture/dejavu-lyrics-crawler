# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    install_requires = ['ScrapyElasticSearch'],
    entry_points = {'scrapy': ['settings = lyricsCrawler.settings']},
)
