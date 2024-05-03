import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_strip(self):
        s = '  hello  '
        self.assertEqual(s.strip(), 'hello')

    def test_startswith(self):
        s = 'hello world'
        self.assertTrue(s.startswith('hello'))
        self.assertFalse(s.startswith('world'))

    def test_endswith(self):
        s = 'hello world'
        self.assertTrue(s.endswith('world'))
        self.assertFalse(s.endswith('hello'))

    def test_replace(self):
        s = 'hello world'
        self.assertEqual(s.replace('world', 'python'), 'hello python')

    def test_in(self):
        s = 'hello world'
        self.assertIn('hello', s)
        self.assertNotIn('python', s)

    def test_index(self):
        s = 'hello world'
        self.assertEqual(s.index('world'), 6)
        with self.assertRaises(ValueError):
            s.index('python')

    def test_count(self):
        s = 'hello world'
        self.assertEqual(s.count('l'), 3)
        self.assertEqual(s.count('python'), 0)

    def test_join(self):
        lst = ['hello', 'world']
        self.assertEqual(' '.join(lst), 'hello world')
        with self.assertRaises(TypeError):
            ' '.join(123)

    def test_lower(self):
        self.assertEqual('HELLO'.lower(), 'hello')

    def test_title(self):
        self.assertEqual('hello world'.title(), 'Hello World')

    def test_capitalize(self):
        self.assertEqual('hello world'.capitalize(), 'Hello world')

    def test_swapcase(self):
        self.assertEqual('HeLlO WoRlD'.swapcase(), 'hElLo wOrLd')

    def test_endswith_multiple_suffixes(self):
        s = 'hello.txt'
        self.assertTrue(s.endswith(('.txt', '.pdf')))
        self.assertFalse(s.endswith(('.jpg', '.png')))

    def test_partition(self):
        s = 'hello world'
        self.assertEqual(s.partition(' '), ('hello', ' ', 'world'))

    def test_rsplit(self):
        s = 'hello world'
        self.assertEqual(s.rsplit(' ', 1), ['hello', 'world'])

    def test_center(self):
        s = 'hello'
        self.assertEqual(s.center(10), '  hello   ')

    def test_zfill(self):
        s = '42'
        self.assertEqual(s.zfill(5), '00042')

    def test_strip_characters(self):
        s = '....hello....'
        self.assertEqual(s.strip('.'), 'hello')

    def test_palindrome(self):
        s = 'racecar'
        self.assertTrue(s == s[::-1])

    def test_anagram(self):
        s1 = 'listen'
        s2 = 'silent'
        self.assertTrue(sorted(s1) == sorted(s2))

    def test_longest_common_prefix(self):
        def longest_common_prefix(strs):
            if not strs:
                return ""
            min_str = min(strs)
            max_str = max(strs)
            for i, char in enumerate(min_str):
                if char != max_str[i]:
                    return min_str[:i]
            return min_str

        strings = ["flower", "flow", "flight"]
        self.assertEqual(longest_common_prefix(strings), "fl")

    def test_reverse_words(self):
        s = "hello world"
        self.assertEqual(' '.join(s.split()[::-1]), "world hello")

    def test_fibonacci_sequence(self):
        def generate_fibonacci(n):
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[i-1] + fib[i-2])
            return fib

        self.assertEqual(generate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    test_result = unittest.TextTestRunner().run(test_suite)
    if test_result.wasSuccessful():
        print('\x1b[32mBUILD SUCCESSFUL\x1b[0m')
    else:
        print('\x1b[31mBUILD FAILED\x1b[0m')