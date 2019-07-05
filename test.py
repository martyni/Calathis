import unittest
import os
from random import choice
from string import ascii_lowercase
from main import take_picture

def random_string(length=5):
    '''
    Creates random lowercase string
    '''
    return ''.join([choice(ascii_lowercase) for _ in range(length)])


class TestCamera(unittest.TestCase):
    def test_take_picture(self):
      filename = random_string() 
      take_picture(filename)
      assert os.path.isfile(filename + '.png')
      os.remove(filename + '.png')



if __name__ == "__main__":
    unittest.main()
