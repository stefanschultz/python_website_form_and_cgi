import urllib.request


def form_submit_get(url: str, forename: str, surname: str) -> None:
    response = urllib.request.urlopen \
        (url + '?' + 'forename=' + forename + '&' + 'surname=' + surname)

    li = response.readlines()
    response.close()

    for element in li:
        print(element.decode('utf-8'), end='')


if __name__ == '__main__':
    form_submit_get('http://localhost:84/python_form/submit_get.php', 'John', 'Doe')