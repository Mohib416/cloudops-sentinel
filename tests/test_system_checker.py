import unittest

from src.system_checker import get_disk_status


class TestSystemChecker(unittest.TestCase):

    def test_disk_status_ok(self):
        self.assertEqual(
            get_disk_status(50, 80, 90),
            "OK"
        )

    def test_disk_status_warning(self):
        self.assertEqual(
            get_disk_status(85, 80, 90),
            "WARNING"
        )

    def test_disk_status_critical(self):
        self.assertEqual(
            get_disk_status(95, 80, 90),
            "CRITICAL"
        )


if __name__ == "__main__":
    unittest.main()
