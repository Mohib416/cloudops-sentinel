import unittest
import json
from pathlib import Path

from src.report import create_report


class TestReport(unittest.TestCase):

    def test_create_report(self):
        system_info = {
            "hostname": "test-machine",
            "disk_used_percent": 50,
            "disk_status": "OK"
        }

        report_file = create_report(system_info)

        self.assertTrue(Path(report_file).exists())

        with open(report_file, "r") as file:
            report = json.load(file)

        self.assertEqual(report["hostname"], "test-machine")
        self.assertEqual(report["disk_used_percent"], 50)
        self.assertEqual(report["disk_status"], "OK")


if __name__ == "__main__":
    unittest.main()
