import unittest
from apk_analyzer import APKAnalyzer

class TestAPKAnalyzer(unittest.TestCase):
    def setUp(self):
        self.apk_path = './nodeapi/base.apk' # Replace the apk path
        self.analyzer = APKAnalyzer(self.apk_path)
    
    def test_analyze(self):
        try:
            self.analyzer.analyze()
            self.assertIsNotNone(self.analyzer.get_package_name(), "Package name should not be None")
            self.assertIsNotNone(self.analyzer.get_version_code(), "Version code should not be None")
            self.assertIsNotNone(self.analyzer.get_version_name(), "Version name should not be None")
            self.assertIsInstance(self.analyzer.get_permissions(), list, "Permissions should be a list")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    unittest.main()
