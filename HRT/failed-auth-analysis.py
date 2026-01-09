'''
🎯 Problem Context (Very Realistic)

You are on the Security Operations team.

You receive a log file containing authentication events from multiple applications. Each line is a JSON object.

Your goal is to detect suspicious failed login activity.
'''

from pathlib import Path
import json

SCRIPT_DIR = Path(__file__).resolve().parent
logs_file_path = SCRIPT_DIR / "auth_logs.json"

def failed_auth_analysis(logs_file_path: Path) -> dict:
    
    with open(logs_file_path, "r", encoding="utf-8") as file:
        fail_logs = json.load(file)
        fail_counts_db = {}

        for log in fail_logs:
            
            if log.get("status") == "FAIL" and "ip" in log:
                ip = log["ip"]

                if log["ip"] in fail_counts_db:
                    fail_counts_db[log["ip"]] += 1
                else:
                    fail_counts_db[log["ip"]] = 1

    sorted_fail_counts_db = dict(
        sorted(fail_counts_db.items(), key=lambda item: item[1], reverse=True)[:3]
    )

    return sorted_fail_counts_db.keys()

if __name__ == "__main__":
    result  = failed_auth_analysis(logs_file_path)
    print(result)

