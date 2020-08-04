from student import *
import unittest

class TestStudent(unittest.TestCase):
            
            
    def test_hello_world(self):
        a = hello_world()
        b = "hello world"
        self.assertEqual(a, b, "hello world is not working")


    def test_summ(self):
        a = 3
        b = 8
        expected = 11
        actual = summ(a, b)
        self.assertEqual(actual, expected, "summ function is not working")
        

if __name__=="__main__":
    unittest.main()