"""Testing anything that comes my mind."""


import unittest


class TestAnything(unittest.TestCase):

    def test_upper_string(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertFalse('me'.isupper())
        self.assertGreater(len('FOOD'), len('FOO'))

    def test_lower_string(self):
        foo = 'FOO'
        self.assertEqual('FoO'.lower(), 'foo')
        self.assertNotEqual('fOO'.upper(), 'FOo')
        self.assertIn('foo', [foo.upper(), foo, foo.lower(), foo[0].lower() + foo[1:]])

    def test_list(self):
        array_items = [
            'foo',
            1,
            False,
            2.30,
            'class',
            '__doc__',
            [[2, 3]],
            {2,4,5},
            (3,3,3),
            {'dict': '__dict__', 'weird': '__weird__'}
        ]

        self.assertIn(type({}), [type(i) for i in array_items])
        self.assertAlmostEqual(array_items[6][0][1], 3.0000000004002001)
        self.assertNotEqual(len(array_items), 7)
