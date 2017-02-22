import unittest
import os
import sys
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        os.system("echo off")
 
    def test_numbers_3_4(self):
        self.assertEqual( 12, 12)
 
    def test_strings_a_3(self):
        self.assertEqual('aaa', 'aaa')

    def test_Connected(self):
        self.assertEqual(os.system("ping -c 1 www.google.co.uk"),0)    
  
    
if __name__ == '__main__':
    unittest.main()