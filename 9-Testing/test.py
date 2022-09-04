import unittest
import script 

class Testscript(unittest.TestCase):
	def setUp(self):
		print('about to test a function')
		
	def test_do_stuff(self):
		test_param = 10
		result= script.do_stuff(test_param)
		self.assertEqual(result,15)  #try putting value other than 15 then it will show an error

	def test_do_stuff2(self):
		test_param = 'qwerty'
		result= script.do_stuff(test_param)
		#self.assertEqual(result,TypeError)
		# self.assertTrue(isinstance(result,ValueError))
		#OR use assertIsInstance(a, b) method like: 
		self.assertIsInstance(result,ValueError)

	def test_do_stuff3(self):
		test_param = None
		result= script.do_stuff(test_param)
		self.assertEqual(result,'please enter a number')

	def test_do_stuff4(self):
		test_param = ''
		result= script.do_stuff(test_param)
		self.assertEqual(result,'please enter a number')

	def test_do_stuff5(self):
		test_param = 0
		result= script.do_stuff(test_param)
		self.assertEqual(result,'please enter a number')

	def tearDown(self):
		print('cleaning up')

if __name__ == '__main__':
	unittest.main()