from app import say_hello
import unittest


class testapp(unittest.TestCase):
    def test_say_hello(self):
        return self.assertEqual(say_hello('aws') , ('hello, aws'))
    



if __name__ ==" __main__":
    unittest.main()