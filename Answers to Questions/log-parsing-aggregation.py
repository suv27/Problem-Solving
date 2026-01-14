logs = [
    {"ip": "1.1.1.1", "path": "/login", "status": 401},
    {"ip": "2.2.2.2", "path": "/login", "status": 403},
    {"ip": "1.1.1.1", "path": "/home", "status": 200},
    {"ip": "3.3.3.3", "path": "/login", "status": 500},
    {"ip": "2.2.2.2", "path": "/home", "status": 404},
    {"ip": "2.2.2.0", "path": "/password", "status": 404},
    {"ip": "2.2.2.0", "path": "/password", "status": 404},
]

class ParsingAggregation:

    def log_parsing_aggregation(logs):

        status_counter = {}

        for log in logs:
            status = log["status"]
            path = log["path"]

            if path not in status_counter:
                status_counter[path] = 0

            if status >= 400 and status < 600:
                status_counter[path] += 1
            
        return sorted(status_counter.items(), key=lambda status: status[1], reverse=True)[:2]


print(ParsingAggregation.log_parsing_aggregation(logs))