import unittest
import sys
sys.path.insert(0, '..')

# Simple test to verify the app can be imported
class TestApp(unittest.TestCase):
    def test_imports(self):
        """Test that app module can be imported"""
        try:
            import app
            self.assertTrue(True)
        except ImportError:
            self.fail("app module not found")

    def test_dummy(self):
        """Dummy test to ensure tests run"""
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
