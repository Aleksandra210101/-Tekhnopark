""""

"""

import unittest
from synonyms import  add
from synonyms import  check
from synonyms import  count

class NameTest(unittest.TestCase):
    """ Test for function of synonyms"""

    def test_add(self):
        """Test for function add """
        synonyms_add = {}
        add('sas', 'lol', synonyms_add)
        add('sas', 'lol', synonyms_add)
        self.assertEqual(len(synonyms_add), 2)
        add('kek', 'lol', synonyms_add)
        self.assertEqual(len(synonyms_add), 3)

    def test_check(self):
        """Test for function check """
        synonyms_check = {'sas': {'kek', 'lol'}}
        self.assertEqual(check('sas', 'lol', synonyms_check), True)
        self.assertEqual(check('sas', 'tre', synonyms_check), False)

    def test_count(self):
        """Test for function count """
        synonyms_count = {'sas': {'kek', 'lol', 'pop'}}
        self.assertEqual(count('sas', synonyms_count), 3)
        add('fef', 'sas', synonyms_count)
        self.assertEqual(count('sas', synonyms_count), 4)
        self.assertEqual(count('fef', synonyms_count), 1)

unittest.main()
