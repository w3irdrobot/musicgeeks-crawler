BOT_NAME = 'musicgeeks'

LOG_LEVEL = 'DEBUG'

SPIDER_MODULES = ['musicgeeks.spiders']
NEWSPIDER_MODULE = 'musicgeeks.spiders'

DEFAULT_ITEM_CLASS = 'musicgeeks.items.SongPage'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'

# Export settings
FEED_URI = './songs.csv'
FEED_FORMAT = 'csv'
FEED_STORE_EMPTY = True