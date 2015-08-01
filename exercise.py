import re # Library for regex
import unittest # Unit Testing (for testing students solutions)

class TestExercise(unittest.TestCase):

    # Do the initial setup by reading the file
    # and storing its result in a string
    def setUp(self):
        pass

    # Fill in the regex to group by Area code (INCLUDING PARENS)!!!
    # Trick question, since () is a special symbol in regex!
    def test_groupByAreaIncludingParens(self):
        phoneNumRegex = re.compile(r'abc')
        mo = phoneNumRegex.search('My phone number is (123) 456-7890.')
        self.assertEqual(mo.group(1), '(123)')
        self.assertEqual(mo.group(2), '456-7890')

    # Fill in the regex such that the area code can be optional
    def test_optionalAreacode(self):
        phoneNumRegex = re.compile(r'abc')
        mo = phoneNumRegex.search('My phone number is 123-456-7890.')
        self.assertEqual(mo.group(), '123-456-7890')
        mo = phoneNumRegex.search('My phone number is 456-7890.')
        self.assertEqual(mo.group(), '456-7890')

    # Assume date is of following format and numbers are within range (01-12) for months etc.
    # : MM/DD/YYYY (Example:- 07/02/1994)
    # If so, capture the groups by SYMBOLIC NAMES rather than NUMBERS
    # (for example, mo.group('month') should give 07, mo.group('day') should give 02, etc.)
    # Notice that you are using symbolic names instead of numbers like mo.group(1) or mo.group(2)
    # LOOK AT THE DOCUMENTATION ON HOW TO DO THIS.
    def test_groupDateBySymbolicName(self):
        dateRegex = re.compile(r'abc')
        mo = dateRegex.search('The date today is 07/31/2015')
        self.assertEqual(mo.group('month'), '07')
        self.assertEqual(mo.group('day'), '31')
        self.assertEqual(mo.group('year'), '2015')

    # Fill in the Regex that matches a sentence (CASE-INSENSITIVE) where:
    # the first word is either Superman, Batman, Flash AND
    # the second word is either protects, saves, rescues AND
    # the third word is Metropolis, Gotham, CentralCity
    # Ex:- Valid Sentences:- SUPErMaN saves centralcity, FLASH rescues Gotham, batman protects Gotham etc.
    # Invalid Sentences:- Joker saves Gotham, Batman destroys Gotham, Superman rescues NewYork
    def test_superheroAdventures(self):
        superheroRegex = re.compile(r'abc')
        
        # Test cases for valid sentences
        mo = superheroRegex.search('SUPErMaN saves centralcity')
        self.assertEqual(mo.group(1), 'SUPErMaN')
        self.assertEqual(mo.group(2), 'saves')
        self.assertEqual(mo.group(3), 'centralcity')

        mo = superheroRegex.search('FLASH RESCUES GOTHAM')
        self.assertEqual(mo.group(1), 'FLASH')
        self.assertEqual(mo.group(2), 'RESCUES')
        self.assertEqual(mo.group(3), 'GOTHAM')

        mo = superheroRegex.search('bAtMaN pRoTeCtS gOtHaM')
        self.assertEqual(mo.group(1), 'bAtMaN')
        self.assertEqual(mo.group(2), 'pRoTeCtS')
        self.assertEqual(mo.group(3), 'gOtHaM')

        # Cases for invalid sentences
        mo = superheroRegex.search('Joker saves Gotham')
        self.assertIsNone(mo)
        mo = superheroRegex.search('Batman destroys CentralCity')
        self.assertIsNone(mo)
        mo = superheroRegex.search('Superman rescues NewYork')
        self.assertIsNone(mo)

    # Fill in the code for the compile() and sub() functions
    # to hide credit card information such that only the last four digits are displayed
    # Do, the same for social security number
    def test_censorCreditCardAndSSN(self):
        creditRegex = re.compile(r'abc')
        subString = creditRegex.sub(r'abc', 'Harry Credit Card #: 4024007187034615, Ron Credit Card #: 5407253822842707, Hermoine Credit Card #: 6011100558881985, Snape Credit Card Number: 3414921614261991')
        self.assertEqual(subString, 'Harry Credit Card #: *************4615, Ron Credit Card #: *************2707, Hermoine Credit Card #: *************1985, Snape Credit Card Number: *************1991')

        ssnRegex = re.compile(r'abc')
        subString = ssnRegex.sub(r'abc', 'Harry SSN #: 402-40-4615, Ron SSN #: 540-72-2707, Hermoine SSN #: 601-10-1985, Snape SSN Number: 341-49-2161')
        self.assertEqual(subString, 'Harry SSN #: ***-**-4615, Ron SSN #: ***-**-2707, Hermoine SSN #: ***-**-1985, Snape SSN Number: ***-**-2161')
    
    # Fill in the regex such that the list is splitted for every number
    def test_splitOrderedList(self):
        self.assertEqual(re.split(r'1', '1.First list 2.Second list 3.Third list'), ['', 'First list ', 'Second list ', 'Third list'])

    # In Part I of the Regex Workshop, you found all the words which end with "ly".
    # Now apart from finding those words, find the positions in which they occur
    # and create a tuple where you have (the word, the positions which they occur). Finally, create
    # a list which has those tuples. See the below test on the general idea.
    # There is a really useful function which can find the positions. Look at the documentation for this.
    def test_findPositions(self):
        f = open('taletwocities.txt', 'r')
        textData = f.read()
        # This is the list you will be modifying
        wordsPositionsTupleList = []
        self.assertEqual(wordsPositionsTupleList, [('only', '2241-2245'), ('recently', '2760-2768'), ('only', '3033-3037'), ('supernaturally', '3138-3152'), ('earthly', '3219-3226'), ('lately', '3247-3253'), ('likely', '4072-4078'), ('likely', '4367-4373'), ('unceasingly', '4747-4758'), ('silently', '4765-4773'), ('scarcely', '4973-4981'), ('publicly', '5167-5175'), ('gallantly', '5458-5467'), ('strongly', '8220-8228'), ('violently', '8661-8670'), ('unusually', '8718-8727'), ('intensely', '9075-9084'), ('visibly', '9149-9156'), ('instantly', '11868-11877'), ('nimbly', '12373-12379'), ('audibly', '13380-13387'), ('furiously', '13544-13553'), ('suddenly', '13673-13681'), ('distrustfully', '14119-14132'), ('mildly', '14389-14395'), ('swiftly', '14769-14776'), ('politely', '14782-14790'), ('immediately', '14824-14835'), ('hoarsely', '15106-15114'), ('slowly', '15411-15417'), ('curtly', '15950-15956'), ('expeditiously', '16743-16756'), ('occasionally', '17477-17489'), ('only', '17505-17509'), ('softly', '17680-17686'), ('only', '17978-17982'), ('heavily', '18178-18185'), ('darkly', '18932-18938'), ('vainly', '19319-19325'), ('exactly', '20322-20329'), ('singly', '21094-21100'), ('nearly', '21285-21291'), ('only', '21385-21389'), ('raggedly', '21868-21876'), ('jaggedly', '21918-21926'), ('strongly', '22056-22064'), ('dimly', '23252-23257'), ('feebly', '23821-23827'), ('principally', '24464-24475'), ('prematurely', '24793-24804'), ('reply', '25262-25267'), ('suddenly', '25761-25769'), ('ghostly', '26362-26369'), ('securely', '26637-26645'), ('distinctly', '26971-26981'), ('successfully', '27729-27741'), ('only', '28041-28045'), ('nicely', '28640-28646'), ('heavily', '29159-29166'), ('Consequently', '29375-29387'), ('formally', '29588-29596'), ('orderly', '30042-30049'), ('habitually', '30886-30896'), ('principally', '31292-31303'), ('easily', '31407-31413'), ('only', '31760-31764'), ('wildly', '33341-33347'), ('madly', '33505-33510'), ('particularly', '33797-33809'), ('unaccountably', '33922-33935'), ('busily', '34389-34395'), ('elderly', '34750-34757'), ('extremely', '35226-35235'), ('immediately', '35280-35291'), ('gloomily', '35764-35772'), ('merely', '36702-36708'), ('heavily', '36979-36986'), ('highly', '38638-38644'), ('gratefully', '39018-39028'), ('naturally', '39240-39249'), ('Naturally', '39309-39318'), ('thoughtfully', '40068-40080'), ('truly', '40526-40531'), ('wilfully', '40657-40665'), ('usually', '40775-40782'), ('entirely', '41505-41513'), ('curiously', '42043-42052'), ('only', '42170-42174'), ('confidingly', '42303-42314'), ('truly', '42707-42712'), ('daily', '43195-43200'), ('suddenly', '44062-44070'), ('silently', '44075-44083'), ('collectedly', '44941-44952'), ('intensely', '45221-45230'), ('intensely', '45424-45433'), ('kindly', '45916-45922'), ('directly', '46123-46131'), ('gently', '46192-46198'), ('particularly', '47325-47337'), ('Greatly', '47476-47483'), ('quietly', '47993-48000'), ('Only', '48399-48403'), ('designedly', '48732-48742'), ('openly', '49138-49144'), ('Perfectly', '49394-49403'), ('utterly', '49485-49492'), ('loudly', '49752-49758'), ('fly', '50291-50294'), ('really', '50334-50340'), ('simultaneously', '50407-50421'), ('softly', '50843-50849'), ('indignantly', '51082-51093'), ('exceedingly', '51311-51322'), ('only', '51383-51387'), ('likely', '51972-51978')])
    
    # Called at the end of each test method
    def tearDown(self):
        pass

# Call unittest's main to test all the functions
if __name__ == '__main__':
    unittest.main()
