"""
The URL parsing code from urllib3, borrowed with gratitude.
"""

def split_first(s, delims):
    """
    Given a string and an iterable of delimiters, split on the first found
    delimiter. Return two split parts and the matched delimiter.

    If not found, then the first part is the full input string.

    Example: ::

        >>> split_first('foo/bar?baz', '?/=')
        ('foo', 'bar?baz', '/')
        >>> split_first('foo/bar?baz', '123')
        ('foo/bar?baz', '', None)

    Scales linearly with number of delims. Not ideal for large number of delims.
    """
    min_idx = None
    min_delim = None
    for d in delims:
        idx = s.find(d)
        if idx < 0:
            continue

        if min_idx is None or idx < min_idx:
            min_idx = idx
            min_delim = d

    if min_idx is None or min_idx < 0:
        return s, '', None

    return s[:min_idx], s[min_idx+1:], min_delim


def parse_url(url):
    # While this code has overlap with stdlib's urlparse, it is much
    # simplified for our needs and less annoying.
    # Additionally, this implementations does silly things to be optimal
    # on CPython.

    scheme = None
    auth = None
    host = None
    port = None
    path = None
    fragment = None
    query = None

    # Scheme
    if '://' in url:
        scheme, url = url.split('://', 1)

    # Find the earliest Authority Terminator
    # (http://tools.ietf.org/html/rfc3986#section-3.2)
    url, path_, delim = split_first(url, ['/', '?', '#'])

    if delim:
        # Reassemble the path
        path = delim + path_

    # Auth
    if '@' in url:
        # Last '@' denotes end of auth part
        auth, url = url.rsplit('@', 1)

    # IPv6
    if url and url[0] == '[':
        host, url = url.split(']', 1)
        host += ']'

    # Port
    if ':' in url:
        _host, port = url.split(':', 1)

        if not host:
            host = _host

        if port:
            # If given, ports must be integers.
            if not port.isdigit():
                raise ValueError("Failed to parse: %s" % url)
            port = int(port)
        else:
            # Blank ports are cool, too. (rfc3986#section-3.2.3)
            port = None

    elif not host and url:
        host = url

    if not path:
        return (scheme, auth, host, port, path, query, fragment)

    # Fragment
    if '#' in path:
        path, fragment = path.split('#', 1)

    # Query
    if '?' in path:
        path, query = path.split('?', 1)

    return (scheme, auth, host, port, path, query, fragment)
