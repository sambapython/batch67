import unittest
from app import fun
class FunTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("sign in code")
	@classmethod
	def tearDownClass(cls):
		print("signout")

	def setUp(self):
		print("RESOURCE ALLOCATE")

	def tearDown(self):
		print("RESOURCE DEALLOCATE")

	def test_1(self):
		act = fun(10,20)
		exp = 30
		self.assertTrue(act==exp,"test_1 failed")

	def test_2(self):
		act = fun(1.2,3.4)
		exp = 4.6
		self.assertTrue(act==exp,"test_2 failed")

	def test_3(self):
		act = fun(10,1.2)
		exp = 11.2
		self.assertTrue(act==exp,"test_3 failed")

	def test_4(self):
		act = fun("str1","py")
		exp = "str1py"
		self.assertTrue(act==exp,"test_4 failed")

	def test_5(self):
		act = fun(10,"str1")
		exp = None
		self.assertTrue(act==exp,"test_5 failed")



unittest.main()
