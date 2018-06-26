class Tag(object):

    def __init__(self, name, content):
        self._content = content
        self._starting_tag = '<{}>'.format(name)
        self._end_tag = '</{}>'.format(name)

    def __str__(self):
        return "{0._starting_tag} {0._content} {0._end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__("!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\""
                         "\"http://www.w3.org/TR/html4/strict.dtd\"", '')
        self._end_tag = ''
        # Doc type doesn't have closing tag


class Head(Tag):
    def __init__(self, title):
        super(Head, self).__init__("HEAD", '')
        self.head_content = list()
        self.title = title
        
    def display(self, file=None):
        self._content = '<TITLE>{0.title}</TITLE>'.format(self) 
        super(Head, self).display(file=file)


class Body(Tag):
    def __init__(self):
        super(Body, self).__init__("BODY", '')
        self.body_content = list()

    def add_tag(self, name, content):
        new_tag = Tag(name, content)
        self.body_content.append(new_tag)

    def display(self, file=None):
        for tag in self.body_content:
            self._content += str(tag)
        
        super(Body, self).display(file=file)


class HtmlDoc(object):
    # # ***************For Composition************
    # def __init__(self, tittle):
    #     self._doc_type = DocType()
    #     self._head = Head(tittle)
    #     self._body = Body()
    #
    # def add_tag(self, name, content):
    #     self._body.add_tag(name, content)
    #
    # def display(self, file=None):
    #     self._doc_type.display(file=file)
    #     print('<html>', file=file)
    #     self._head.display(file=file)
    #     self._body.display(file=file)
    #     print('</html>', file=file)

    # **********FOR Aggregation*************
    # Aggregation too creates 'has A relationship'

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    # ***********For Composition**************
    # html = HtmlDoc('INDEX')
    # html.add_tag('H1', 'This is heading 1')
    # html.add_tag('H2', 'This is heading 3')
    # html.add_tag('p', 'This is a paragraph.')
    # with open('index.html','w') as html_file:
    #     html.display(html_file)

    # **************************Aggregation*********************
    head = Head("Aggregation")
    new_body = Body()
    new_body.add_tag('H1', 'AGGREGATION')
    new_body.add_tag('p', "Unlike <strong>COMPOSITION</strong>, aggregation uses existing instances "
                          "of the object to build up the another object")
    new_body.add_tag('p', "The composed object doesn't actually own the objects that its composed of"
                          "- if its destroyed those object continue to exist")
    doc_type = DocType()

    html = HtmlDoc(doc_type, head, new_body)

    with open('IMPLEMENTING Aggregation.html', 'w') as html_file:
        html.display(html_file)


