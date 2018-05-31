#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from assertpy import assert_that

from src.line_breaker import LineBreaker

class TestLineBreaker(unittest.TestCase):
    def test_split_text_into_lines_with_empty_text(self):
        assert_that(LineBreaker.to_lines('')).is_empty()

    def test_split_text_into_lines_with_string_with_length_one(self):
        assert_that(LineBreaker.to_lines('a')).is_equal_to(['a'])

    def test_split_text_into_lines_with_large_string(self):
        target = 'Mussum Ipsum, cacilds vidis litro abert. Praesent vel'
        expected = [
            'Mussum Ipsum, cacilds vidis litro abert.',
            'Praesent vel'
        ]
        actual = LineBreaker.to_lines(target, 40)
        assert_that(actual).is_equal_to(expected)


    def test_justify_larger_then_max_length(self):
        target = 'Tenna norna ela ar, mitya atacar sá úvë, loc téra caila larca ve'
        assert_that(LineBreaker.justify).raises(ValueError).when_called_with(target)

    def test_justify_length_equals_to_max_length(self):
        target = 'Tenna norna ela ar, mitya atacar sá úvë'
        actual = LineBreaker.justify(target, 39)
        assert_that(actual).is_equal_to(target)

    def test_justify_empty_string(self):
        assert_that(LineBreaker.justify).raises(ValueError).when_called_with('')

    def test_justify_shorter_then_max_length(self):
        target = 'Fëa ninwa hravan up'
        expected = 'Fëa        ninwa        hravan        up'
        actual = LineBreaker.justify(target, 40)
        assert_that(actual).is_equal_to(expected)

    @unittest.skip('')
    def test_justify_lines_text_with_length_120(self):
        target = 'Mussum Ipsum, cacilds vidis litro abertis. Em pé sem cair, deitado sem dormir, sentado sem cochilar'
        actual = LineBreaker.justify_lines(LineBreaker.to_lines(target, 40))
        assert_that(actual).has_length(3)

        for line in actual:
            assert_that(line).has_length(40)
