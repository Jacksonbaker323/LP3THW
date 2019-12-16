from nose.tools import assert_equal, assert_raises
from ex48 import parser


def test_parser():
    sentence = [('verb', 'run'), ('direction', 'north')]
    x = parser.parse_sentence(sentence)
    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'run')
    assert_equal(x.object, 'north')


def test_exception():
    assert_raises(parser.ParserError, parser.parse_verb, ('direction', 'north'))
