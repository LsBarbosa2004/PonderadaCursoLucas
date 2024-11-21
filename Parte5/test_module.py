import unittest
from sea_level_predictor import draw_plot

class SeaLevelPredictorTest(unittest.TestCase):
    def test_plot(self):
        self.assertTrue(draw_plot())

if __name__ == "__main__":
    unittest.main()
