import unittest
from models import quote
Quote= quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote("Charles Babbage","8","On two occasions I have been asked, \u2018Pray, Mr. Babbage, if you put into the machine wrong figures, will the right answers come out?\u2019 I am not able rightly to apprehend the kind of confusion of ideas that could provoke such a question.\u201d","http://quotes.stormconsultancy.co.uk/quotes/8")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()
