import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    
    def test_emotion_detector_joy(self):
        
        result = emotion_detector("I am glad this happened")
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        
        self.assertIn('dominant_emotion', result, "Result should contain 'dominant_emotion' key")
        
        self.assertEqual(result['dominant_emotion'], 'joy', 
                         f"Expected 'joy' but got '{result['dominant_emotion']}'")
    
    def test_emotion_detector_anger(self):
       
        result = emotion_detector("I am really mad about this")
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertIn('dominant_emotion', result, "Result should contain 'dominant_emotion' key")
        self.assertEqual(result['dominant_emotion'], 'anger', 
                         f"Expected 'anger' but got '{result['dominant_emotion']}'")
    
    def test_emotion_detector_disgust(self):
        
        result = emotion_detector("I feel disgusted just hearing about this")
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertIn('dominant_emotion', result, "Result should contain 'dominant_emotion' key")
        self.assertEqual(result['dominant_emotion'], 'disgust', 
                         f"Expected 'disgust' but got '{result['dominant_emotion']}'")
    
    def test_emotion_detector_sadness(self):
        
        result = emotion_detector("I am so sad about this")
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertIn('dominant_emotion', result, "Result should contain 'dominant_emotion' key")
        self.assertEqual(result['dominant_emotion'], 'sadness', 
                         f"Expected 'sadness' but got '{result['dominant_emotion']}'")
    
    def test_emotion_detector_fear(self):
        
        result = emotion_detector("I am really afraid that this will happen")
        
        self.assertIsInstance(result, dict, "Result should be a dictionary")
        self.assertIn('dominant_emotion', result, "Result should contain 'dominant_emotion' key")
        self.assertEqual(result['dominant_emotion'], 'fear', 
                         f"Expected 'fear' but got '{result['dominant_emotion']}'")
    
    def test_emotion_detector_format(self):
        
        result = emotion_detector("Test statement")
        
        if 'error' in result:
            self.skipTest("API error occurred, skipping format test")0
        
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result, f"Result should contain '{key}' key")
        
        
        score_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for key in score_keys:
            self.assertIsInstance(result[key], (int, float), 
                                  f"'{key}' should be a number, got {type(result[key])}")

if __name__ == '__main__':
    unittest.main()