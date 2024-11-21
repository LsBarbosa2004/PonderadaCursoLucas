import unittest
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class UnitTests(unittest.TestCase):
    def test_cat_plot(self):
        self.assertTrue(draw_cat_plot())

    def test_heat_map(self):
        self.assertTrue(draw_heat_map())

if __name__ == "__main__":
    unittest.main()
