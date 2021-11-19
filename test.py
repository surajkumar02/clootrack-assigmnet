import unittest
import sys

sys.path.insert(0, 'tweets.py')
from tweets import tweet_count

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(tweet_count(),())
        # self.assertEqual(tweet_count(1)(4)('sachin tweet_id_1\nsehwag tweet_id_2\nsachin tweet_id_3\nsachin tweet_id_4'),'sachin 3\nsehwag 1')



if __name__ == '__main__':
    unittest.main()