class Editor(object):
    password = input('Enter password to achieve pro features: ')

    def __new__(cls):
        if Editor.password == 'pro':
            return ProEditor()
        else:
            return object.__new__(cls)

    def __init__(self, document='Empty Document'):
        self.document = document

    def view_document(self):
        print(self.document)

    def edit_document(self):
        print('You have not permission to edit the document')


class ProEditor(Editor):

    def __new__(cls):
        return object.__new__(cls)

    def __init__(self, document='Empty Document'):
        self.document = document

    def view_document(self):
        print(self.document)

    def edit_document(self):
        print('Write down the new version of doc')
        new_ver = input()
        self.document = new_ver
        print('Document changed:')
        print(self.document)

ed1 = Editor()
ed1.view_document()
ed1.edit_document()