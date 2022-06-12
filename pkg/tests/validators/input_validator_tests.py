#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 Bhojpur Consulting Private Limited, India. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import unittest
from utils.validators.input_validator import is_valid_future_date, is_valid_input

class InputValidatorTest(unittest.TestCase):
    def test_is_input_valid_works_with_true(self):
        self.assertTrue(is_valid_input("ten_letter", 10))
        self.assertTrue(is_valid_input("h", 50))
        self.assertTrue(is_valid_input("testing", 100))
        self.assertTrue(is_valid_input("testing", 200))

    def test_is_input_valid_works_with_false(self):
        self.assertFalse(is_valid_input("testing", 1))
        self.assertFalse(is_valid_input("ten_letter", 5))
        self.assertFalse(is_valid_input(None, 100))
        self.assertFalse(is_valid_input("", 200))

    # test cases expires 2050 :)
    def test_is_valid_date_works_with_true(self):
        self.assertTrue(is_valid_future_date("2050-11-11 11:15"))
        self.assertTrue(is_valid_future_date("2050-01-01 17:00"))
        self.assertTrue(is_valid_future_date("2050-11-11 11:15"))
        self.assertTrue(is_valid_future_date("2052-02-29 15:00"))

    def test_is_valid_date_works_with_false(self):
        self.assertFalse(is_valid_future_date("2000-12-01 11:15"))
        self.assertFalse(is_valid_future_date("2022-01-01 17:00"))
        self.assertFalse(is_valid_future_date("1994-11-11 11:15"))
        self.assertFalse(is_valid_future_date(None))
        self.assertFalse(is_valid_future_date("not date"))