try:
    from urllib3.util import parse_url
except ImportError:
    from sturl.lib.urllib3 import parse_url


class URL(object):
    """
    Usage: ::

        >>> URL('example.com/foo/bar')[0]
        'foo'

        >>> URL('example.com/foo/bar/')[:]
        ['foo', 'bar', '']

        >>> URL('example.com/foo/bar/?lot=exp')['lot']
        'exp'

        >>> URL('example.com/foo') + 'bar/?lot=exp'
        URL('example.com/foo/bar/?lot=exp')

        >>> URL('example.com/foo?lot=exp#hi') + 'bar'
        URL('example.com/foo/bar')

    """
    def __init__(self, *args, **kwargs):
        pass
