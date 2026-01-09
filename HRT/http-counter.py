'''
You are given a list of HTTP log entries like this:

Task:
Return a dictionary showing how many times each status code appears.
'''
logs = [
    {"status": 200},
    {"status": 403},
    {"status": 200},
    {"status": 500},
    {"status": 403},
    {"status": 403},
    {"status": 202},
    {"status": 302},
    {"status": 403},
    {"status": 403},
    {"status": 200},
    {"status": 500},
    {"status": 403}
]

def count_http_status(logs) -> dict:

    counter = {}

    for log in logs:
        status_code = log.get("status")
        if status_code not in counter:
            counter[status_code] = 1
        else:
            counter[status_code] += 1
    
    sorted_status_code = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True)[:1])
    
    print(sorted_status_code)
    return sorted_status_code


count_http_status(logs)