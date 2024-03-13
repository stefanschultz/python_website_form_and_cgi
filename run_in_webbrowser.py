import webbrowser


def open_webbrowser() -> None:
    """
    Open webbrowser
    :return: None
    """
    webbrowser.open('http://www.python.org')
    return None


if __name__ == '__main__':
    open_webbrowser()