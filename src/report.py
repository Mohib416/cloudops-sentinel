import json
from pathlib import Path


def create_report(system_info):
    report_directory = Path("reports")
    report_directory.mkdir(exist_ok=True)

    report_file = report_directory / "system_report.json"

    with open(report_file, "w") as file:
        json.dump(system_info, file, indent=4)

    return report_file
