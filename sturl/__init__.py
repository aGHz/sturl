try:
    from urllib3.util import parse_url
except ImportError:
    from sturl.lib.urllib3 import parse_url


class URL(object):
    def __init__(self, *args, **kwargs):
        pass
