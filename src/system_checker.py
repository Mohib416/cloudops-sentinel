import subprocess

from src.config import load_config


def get_disk_status(used_percent, warning_threshold, critical_threshold):
    if used_percent >= critical_threshold:
        return "CRITICAL"
    elif used_percent >= warning_threshold:
        return "WARNING"
    else:
        return "OK"


def get_system_info():
    config = load_config()

    warning_threshold = config["disk_warning"]
    critical_threshold = config["disk_critical"]

    try:
        hostname = subprocess.run(
            ["hostname"],
            capture_output=True,
            text=True,
            check=True
        ).stdout.strip()

        disk_output = subprocess.run(
            ["df", "-h", "/"],
            capture_output=True,
            text=True,
            check=True
        ).stdout

        disk_lines = disk_output.splitlines()
        disk_values = disk_lines[1].split()

        disk_used_percent = int(
            disk_values[4].replace("%", "")
        )

        disk_status = get_disk_status(
            disk_used_percent,
            warning_threshold,
            critical_threshold
        )

        system_info = {
            "hostname": hostname,
            "disk_used_percent": disk_used_percent,
            "disk_status": disk_status
        }

        return system_info

    except (subprocess.CalledProcessError, IndexError, ValueError):
        return {
            "hostname": "unknown",
            "disk_used_percent": 0,
            "disk_status": "ERROR"
        }
