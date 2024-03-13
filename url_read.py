import sys
import urllib.request


def read_url(url):
    try:
        with urllib.request.urlopen(url) as webpage:
            li = webpage.readlines()
            for line in li:
                print(line.decode('utf-8'), end='')
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(0)


def save_webpage(url, filename):
    print(urllib.request.urlretrieve(url, filename))


if __name__ == '__main__':
    read_url('http://localhost:84/python_form/url_read.html')
    save_webpage('http://localhost:84/python_form/url_read.html', './html_copy/url_read.html')