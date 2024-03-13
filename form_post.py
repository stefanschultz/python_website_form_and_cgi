import urllib.request, urllib.parse


def form_submit_post(url: str, forename: str, surname: str) -> None:
    dc = {b"forename": forename.encode('utf-8'), b"surname": surname.encode('utf-8')}
    data = bytes(urllib.parse.urlencode(dc), 'utf-8')
    response = urllib.request.urlopen(url, data)

    li = response.readlines()
    response.close()

    for element in li:
        print(element.decode('utf-8'), end='')


if __name__ == '__main__':
    form_submit_post('http://localhost:84/python_form/submit_post.php', 'John', 'Doe')