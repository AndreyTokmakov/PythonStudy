
def html_document(func):
    def wrapped():
        return "<html>" + func() + "</html>"

    return wrapped


def html_body(func):
    def wrapped():
        return "<body>" + func() + "</body>"

    return wrapped


@html_document
@html_body
def hello():
    return "Hello"


if __name__ == "__main__":
    text = hello()
    print(text)
