import unittest
from Lab3_Ethan_Teigan import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    def test_trapezium_area_valid(self):
        self.assertEqual(trapezium_area(3,5,4),16)
        
        

    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-3,5,4)
        with self.assertRaises(ValueError):
            trapezium_area(3,-5,4)    
        with self.assertRaises(ValueError):
            trapezium_area(3,5,-4)

    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(3,2), 18.84955592153876)
        

    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(-1, 2)
        with self.assertRaises(ValueError):
            ellipse_area(1, -2)
        with self.assertRaises(ValueError):
            ellipse_area(0, 1)
        with self.assertRaises(ValueError):
            ellipse_area(1, 0)
      

    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(6, 8), 24)

     
    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(0, 8)
        with self.assertRaises(ValueError):
            rhombus_area(6,-8)
        
if __name__ == "__main__":
    unittest.main()