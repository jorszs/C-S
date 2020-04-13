#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
import copy

class dict2xml(object):
    doc     = Document()

    def __init__(self, structure):
        if len(structure) == 1:
            rootName    = str(structure.keys()[0])
            self.root   = self.doc.createElement(rootName)

            self.doc.appendChild(self.root)
            self.build(self.root, structure[rootName])

    def build(self, father, structure):
        if type(structure) == dict:
            for k in structure:
                tag = self.doc.createElement(k)
                father.appendChild(tag)
                self.build(tag, structure[k])
        
        elif type(structure) == list:
            grandFather = father.parentNode
            tagName     = father.tagName
            grandFather.removeChild(father)
            for l in structure:
                tag = self.doc.createElement(tagName)
                self.build(tag, l)
                grandFather.appendChild(tag)
            
        else:
            data    = str(structure)
            tag     = self.doc.createTextNode(data)
            father.appendChild(tag)
    
    def display(self):
        print self.doc.toprettyxml(indent="  ")

if __name__ == '__main__':
    
    example = {'documents': [{'formats': [{'info': {'uri': 'http://www.python.org/newness-of-python.pdf', 'pages': '245'}, 'type': 'pdf'}, {'info': {'uri': 'http://www.python.org/newness-of-python.html'}, 'type': 'web'}], 'copyright': {'url': 'http://www.creativecommons.org/', 'date': 'June 24, 2009', 'type': 'CC'}, 'title': 'The Newness of Python', 'date': 'June 6, 2009', 'text': ['Python is very nice. Very, very nice.'], 'author': 'John Doe'}]}
    xml = dict2xml(example)
    xmlD = xml.doc.toprettyxml(indent="  ")
    #xml.display()
    print xmlD
    f1=open('output.xml', 'w+')
    f1.seek(0)
    f1.write(str(xmlD))
    f1.close()
