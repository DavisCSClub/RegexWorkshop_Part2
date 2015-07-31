import re # Library for regex
import unittest # Unit Testing (for testing students solutions)

class TestExercise(unittest.TestCase):

    # Do the initial setup by reading the file
    # and storing its result in a string
    def setUp(self):
        #self.f = open('taletwocities.txt', 'r') # Open the file for reading
        #self.textData = self.f.read() # Grab the entire string from the text file
        pass

    # Fill in the regex to group by Area code (INCLUDING PARENS)!!!
    # Trick question, since () is a special symbol in regex!
    def test_groupByAreaIncludingParens(self):
        phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
        mo = phoneNumRegex.search('My phone number is (123) 456-7890.')
        self.assertEqual(mo.group(1), '(123)')
        self.assertEqual(mo.group(2), '456-7890')

    # Fill in the code such that the area code can be optional
    def test_optionalAreacode(self):
        phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
        mo = phoneNumRegex.search('My phone number is 123-456-7890.')
        self.assertEqual(mo.group(), '123-456-7890')
        mo = phoneNumRegex.search('My phone number is 456-7890.')
        self.assertEqual(mo.group(), '456-7890')

    def 


    
    # Called at the end of each test method
    def tearDown(self):
        pass
        #self.f.close()

# Call unittest's main to test all the functions
if __name__ == '__main__':
    unittest.main()
