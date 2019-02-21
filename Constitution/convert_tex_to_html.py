#!/usr/bin/env python3

import string
import datetime
import argparse

from subprocess import Popen, PIPE
from collections import Counter

import lxml.html
from lxml import etree
import roman

a = argparse.ArgumentParser()
a.add_argument('-f', '--file', dest='texfile', type=argparse.FileType('r'), default='./Articles-of-Association.tex')
args = a.parse_args()

cmd = r"sed '/^%%%%%%/,/^%%%%%%/{/^%%%%%%/!{/^%%%%%%/!d;};}' | sed 's/\\part/\\chapter/' | pandoc -f latex -t html5 --section-divs --email-obfuscation=none"
process = Popen(cmd, shell=True, stdout=PIPE, stdin=args.texfile)
data = process.communicate()[0].decode()
text = open('template.html').read() % data
doc = lxml.html.fromstring(text)

last_id = ""
last_article = 1
last_subarticle = 1
last_paragraph = 1
ready = False
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
footnote_count = 1

def create_part_link(doc, node, id_attr=None):
    a = doc.makeelement('a')
    a.attrib['href'] = "#" + (id_attr or node.attrib['id'])
    a.attrib['class'] = 'pilcrow'
    a.text = "¶"
    node.append(a)

def create_article_link(doc, node, id_attr=None):
    a = doc.makeelement('a')
    a.attrib['href'] = "#" + (id_attr or node.attrib['id'])
    a.attrib['class'] = 'pilcrow'
    a.text = "¶"
    node.append(a)

def create_subarticle_link(doc, node, id_attr=None):
    a = doc.makeelement('a')
    a.attrib['href'] = "#article-" + str(last_article - 1) + "." + str(last_subarticle)
    a.attrib['class'] = 'pilcrow'
    a.text = "¶"
    node.append(a)

def create_paragraph_link(doc, node, id_attr=None):
    a = doc.makeelement('a')
    a.attrib['href'] = "#article-" + str(last_article - 1) + "." + str(last_subarticle - 1) + "("+ alpha[last_paragraph -1] + ")"
    a.attrib['class'] = 'pilcrow'
    a.text = "¶"
    node.append(a)

for node in doc.body.iter():
    if not ready:
        if node.tag == "hr":
            ready = True
            node.getparent().remove(node)
        else: continue

    if node.tag == "section":
        last_section = node
        if node.attrib["class"] == "level2":
            new_id = str(last_article) + "-" + node.attrib['id']
            node.attrib['id'] = new_id

    if node.tag == "section":
        if node.attrib['class'] == "footnotes":
            node.attrib['id'] = "footnotes"

    if node.tag == "h1":
        create_part_link(doc, node, last_section.attrib['id'])

    if node.tag == "h2":
        create_article_link(doc, node, last_section.attrib['id'])
        last_article += 1
        last_subarticle = 1

    if node.tag == "ol" and node.getparent().tag == "section":
        if node.getparent().attrib["class"] == "footnotes":
            node.attrib["class"] = "footnote-list"

    if node.tag == "li":
        if node.getparent().getparent().tag == "section":
            if node.getparent().getparent().attrib["class"] == "footnotes":
                node.attrib["id"] = "fn" + str(footnote_count)
                footnote_count += 1
            else:
                node.attrib['id'] = "article-" + str(last_article - 1) + "." + str(last_subarticle)
                create_subarticle_link(doc, node[0], last_section.attrib['id'])
                last_subarticle += 1
                last_paragraph = 1
        else:
            node.attrib['id'] = "article-" + str(last_article - 1) + "." + str(last_subarticle - 1) + "(" + alpha[last_paragraph - 1] + ")"
            create_paragraph_link(doc, node[0], last_section.attrib['id'])
            last_paragraph += 1

    if node.tag in ["dt"]:
        node.attrib['id'] = "article-" + str(last_article - 1) + "." + str(last_subarticle)
        create_subarticle_link(doc, node, last_section.attrib['id'])
        last_subarticle += 1
        last_paragraph = 1

open('output.html', 'w').write(lxml.html.tostring(doc, pretty_print=True).decode())
