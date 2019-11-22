"""
web crawler using beautiful soup
"""
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def simple_get(url):
    """
       Attempts to get the content at `url` by making an HTTP GET request.
       If the content-type of response is some kind of HTML/XML, return the
       text content, otherwise return None.
       """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def desoup(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    print('DocTitle: {0}'.format(soup.title))
    print('Title text {0}'.format(soup.title.string))
    print('Title name {0}'.format(soup.title.name))


if __name__ == '__main__':
    res = simple_get('https://www.cricbuzz.com/cricket-series/2330/indian-premier-league-2015/matches')
    desoup(res)
