# test_futurecrypto.py
"""
Tests for FutureCrypto module.
"""

import unittest
from futurecrypto import FutureCrypto

class TestFutureCrypto(unittest.TestCase):
    """Test cases for FutureCrypto class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FutureCrypto()
        self.assertIsInstance(instance, FutureCrypto)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FutureCrypto()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
