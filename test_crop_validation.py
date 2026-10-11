
import unittest
from crop_validation import validate_crop_input


class TestCropValidation(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            "N": 90,
            "P": 42,
            "K": 43,
            "temperature": 20.8,
            "humidity": 82.0,
            "ph": 6.5,
            "rainfall": 202.9
        }

    def test_valid_crop_input(self):
        self.assertTrue(validate_crop_input(self.valid_data))

    def test_missing_feature(self):
        data = self.valid_data.copy()
        del data["N"]
        self.assertFalse(validate_crop_input(data))

    def test_negative_value(self):
        data = self.valid_data.copy()
        data["N"] = -10
        self.assertFalse(validate_crop_input(data))

    def test_non_numeric_value(self):
        data = self.valid_data.copy()
        data["temperature"] = "hello"
        self.assertFalse(validate_crop_input(data))


if __name__ == "__main__":
    unittest.main()
