def do_stuff (num=0):
	try:
		if num:
			return int(num) + 5
		else:
			return 'please enter a number'
	except ValueError as err:
		return err


#when we get TypeError we try to fix our code from: return num + 5 to return int(num) + 5
#now we get VallueError , now we use try,except block. 
#now assertion error will come to fix it we will fix our code from : self.assertEqual(result,TypeError) to self.assertTrue(isinstance(result,ValueError))
#if we give None as a parameter it will throw error for it we used if else block and num=0.
