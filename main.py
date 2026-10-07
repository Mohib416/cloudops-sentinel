import logging

from src.system_checker import get_system_info
from src.report import create_report


logging.basicConfig(
    filename="logs/cloudops-sentinel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    logging.info("System check started")

    system_info = get_system_info()

    logging.info("System check completed")

    report_file = create_report(system_info)

    logging.info("Report created")

    print("System check completed.")
    print(f"Status: {system_info['disk_status']}")
    print(f"Report: {report_file}")


if __name__ == "__main__":
    main()
