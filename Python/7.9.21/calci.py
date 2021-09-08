import unittest
from calsi import add,sub,mul,div

class LearnTest(unittest.TestCase):
    def setUp(self):
        self.a = 20
        self.b = 30
    def testsum(self):
        self.assertEqual(add(self.a,self.b), self.a+self.b)
    def testsub(self):
        self.assertEqual(sub(self.a, self.b), self.a - self.b)
    def testmul(self):
        self.assertEqual(mul(self.a, self.b), self.a * self.b)
    def testdiv(self):
        self.assertEqual(div(self.a, self.b), self.a / self.b)

if __name__ == '__main__':
    unittest.main(verbosity=2)