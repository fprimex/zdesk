#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-
# 
# Copyright 2010 Vojtech Rylko <vojta.rylko @ seznam.cz>
#

"""
Module for converting dict to xml.
"""
# inspired by http://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html.

__author__ = "xrylko00@stud.fit.vutbr.cz"

INDENTATION = 4     # for one level
ATTRIBUTE_PREFIX = "@"
TEXT = "#text"


def _test(dictionary):
    if not isinstance(dictionary, dict):
        raise TypeError("Type '%s' cannot be serialized." % \
                        type(dictionary).__name__)


def tostring(dictionary, pretty_print=False):
    """Convert dictionary to xml.
    
    Prefix `@` for attributes, `#text` for text.
    
    For examples see test/__main__.py

    @return: string
    """
    _test(dictionary)
    if dictionary == {}: return ''
    return "".join(_build_element(e, v, 0, pretty_print) for e, v in dictionary.items())
    
def to_etree(dictionary, etree):
    """Convert dictionary to etree structure.

    Prefix `@` for attributes, `#text` for text.
    
    For examples see test/__main__.py

    @return: string
    """
    _test(dictionary)
    if len(dictionary) > 1:
        raise TypeError("Dictionary can have only one root element.")
    if dictionary == {}: return etree.Element(None)
    r, v = dictionary.items()[0]
    return _build_element(r, v, etree=etree)
    
def _build_element(root, value, level=0, pretty_print=False, etree=None):
    """
    Make element with name `root` and with value `value`. It can
    contains attributes.
    
    Specials: starts with @ for attributes, #text for text.
    
    @return: string
    """
    if pretty_print: 
        newline = '\n'
        tabular = " "*(INDENTATION*level)
    else: 
        newline = ''
        tabular = ""

    if not value:
        if not etree : result = "<%s />%s" % (root, newline)
        else : result = etree.Element(str(root))
    elif isinstance(value, list):
        tabular = ""
        if not etree:
            return "".join([_build_element(root, r, level, pretty_print) for r in value])
        else:
            #raise ValueError("{root: [list,]} is not supported schema with etree")
            result = []
            for subelement in value:
                result.append(_build_element(root, subelement, etree=etree))
    elif isinstance(value, dict):
        values = []
        attribs = []
        for r, v in value.iteritems():
            if (isinstance(r, basestring) and r.startswith(ATTRIBUTE_PREFIX)):
                # its attribute
                attribs.append(_build_attrib(r,v, etree))
            else:
                # its content = element
                values.append(_build_element(r, v, level+1, pretty_print, etree))
        attr = ""
        if not etree:
            if attribs: 
                # prepare `attr` for attributes
                attr = " "+" ".join(attribs)
                
            if values:
                # result with content
                result = "<%s%s>%s%s</%s>%s" % \
                        (root, attr, newline, 
                         "".join(values), root, newline)
            else:
                # result without any content
                result = "<%s%s/>" % (root, attr)
        else: # etree
            result = etree.Element(str(root))
            for atr, val in attribs:
                result.attrib[atr] = val
            for value in values:
                if isinstance(value, basestring):
                    result.text = value
                elif isinstance(value, list):
                    for subval in value:
                        result.append(subval)
                else: result.append(value)

    elif root == TEXT:
        if value == '<\'">':
            result = quote_xml(value)
        else:
            result = quote_xml(value)
    else: 
        if not etree:
            result = "<%s>%s</%s>%s" % (root, quote_xml(value), root, newline)
        else:
            result = etree.Element(str(root))
            result.text = unicode(value)
    if etree : return result
    else : return  tabular + result


#
# Help Functions
#
def _build_attrib(name, value, etree=None):
    """
    Build attribute as 'name="value"'
    """
    if not etree: 
        return '%s=%s' % (name[1:], quote_attrib(value)) # remove first char @
    else:
        return (name[1:], unicode(value))

def quote_xml(inStr):
    """Author: dkuhlman@rexx.com, MIT Licence"""
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    """Author: dkuhlman@rexx.com, MIT Licence"""
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1
