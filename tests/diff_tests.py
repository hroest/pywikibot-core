# -*- coding: utf-8  -*-
"""Tests for diff module."""
#
# (C) Pywikibot team, 2009-2014
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, unicode_literals

__version__ = '$Id$'

from pywikibot import diff

from tests import join_xml_data_path
from tests.aspects import unittest, TestCase


class DiffTestCase(TestCase):

    """Diff module test cases."""

    def __init__(self):
        pass

class HunkTestCase(TestCase):

    """Hunk test."""

    net = False

    def test_HunkDiffText1(self):
        text_a = ['some text'] 
        text_b = ['some_text'] 
        groups = [('replace', 0, 1, 0, 1)]

        hunk = diff.Hunk(text_a, text_b, groups)

        self.assertEqual(2, len(hunk.diff_text.splitlines()))

        self.assertEqual(u'\x03{lightred}-\x03{default} some\x03{lightred} \x03{default}text', hunk.diff_text.splitlines()[0])
        self.assertEqual(u'\x03{lightgreen}+\x03{default} some\x03{lightgreen}_\x03{default}text', hunk.diff_text.splitlines()[1])

class PatchManagerTestCase(TestCase):

    """PatchManager test."""

    net = False


    def test_PatchManager1(self):

        a = 'some text'
        b = 'some_text'
        pm = diff.PatchManager(a, b)

        self.assertEqual(1, len(pm._super_hunks))
        self.assertEqual(1, len(pm.hunks))
        superhunk = pm._super_hunks[0]

        self.assertEqual(1, len(pm.hunks))
        hunk = pm.hunks[0]

        expected = u'\x03{aqua}@@ -1 +1 @@\x03{default}\n'
        expected += u'\x03{lightred}-\x03{default} some\x03{lightred} \x03{default}text\n'
        expected += u'\x03{lightgreen}+\x03{default} some\x03{lightgreen}_\x03{default}text\n'
        self.assertEqual(expected, pm._generate_diff(superhunk))

    def test_PatchManager2(self):
        # This is a more advanced test, taken from the example of difflib.ndiff
        a = 'one\ntwo\nthree\n'
        b = 'ore\ntree\nemu\n'
        pm = diff.PatchManager(a, b)

        self.assertEqual(1, len(pm._super_hunks))
        self.assertEqual(1, len(pm.hunks))
        superhunk = pm._super_hunks[0]

        expected = u'\x03{aqua}@@ -1,3 +1,3 @@\x03{default}\n\x03{lightred}-\x03{default} o\x03{lightred}n\x03{default}e\n\x03{lightgreen}+\x03{default} o\x03{lightgreen}r\x03{default}e\n\x03{lightred}- two\n\x03{default}\x03{lightred}-\x03{default} t\x03{lightred}h\x03{default}ree\n\x03{lightgreen}+\x03{default} tree\n\x03{lightgreen}+ emu\n\x03{default}'
        self.assertEqual(expected, pm._generate_diff(pm._super_hunks[0]))


if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
