import unittest
from models import Pitch

class Pitch_Test(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        new_pitch=Pitch('test_pitch', 'sample_category', 'sample_author')

    def test_init(self):
        '''
        '''
        self.assertEqual(self.new_pitch.pitch_text,'test_pitch')
        self.assertEqual(self.new_pitch.pitch_category,'sample_category')
        self.assertEqual(self.new_pitch.pitch_author,'sample_author')

    def test_instance(self):
        self.assertIsInstance(self.new_pitch, Pitch)

if __name__ == '__main__':
    unittest.main() 