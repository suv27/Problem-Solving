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

class HTTPStatus:

    def count_http_status(logs) -> dict:

        counter = {}

        for log in logs:
            status_code = log.get("status")
            if status_code not in counter:
                counter[status_code] = 1
            else:
                counter[status_code] += 1
        
        sorted_status_code = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True)[:1])
    
        return sorted_status_code


# print(HTTPStatus.count_http_status(logs))
