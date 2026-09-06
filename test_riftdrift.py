# test_riftdrift.py
"""
Tests for RiftDrift module.
"""

import unittest
from riftdrift import RiftDrift

class TestRiftDrift(unittest.TestCase):
    """Test cases for RiftDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RiftDrift()
        self.assertIsInstance(instance, RiftDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RiftDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
