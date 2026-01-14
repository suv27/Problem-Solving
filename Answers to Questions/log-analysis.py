logs_line = [
    "ERROR failed login from 1.1.1.1",
    "INFO user logged in",
    "WARN suspicious activity detected",
    "ERROR database connection failed",
    "ngix: ERROR database connection failed",
    "INFO startup complete ",
    "ERROR failed login again",
    "ERROR database down",
    "INFO recovery complete"
]
keyword = "ERROR"

message_logs_line = [
    {"timestamp": 1, "message": "ERROR failed login from 1.1.1.1"},
    {"timestamp": 3, "message": "INFO user logged in"},
    {"timestamp": 5, "message": "ERROR db connection failed"},
    {"timestamp": 8, "message": "INFO user logged out"},
    {"timestamp": 12, "message": "ERROR something else"},
    {"timestamp": 17, "message": "ERROR again"},
    {"timestamp": 21, "message": "ERROR at response time"},
]


class LogAnalysis:
    
    def simulate_grep(log_lines, keyword) -> list:

        result = []

        for log in log_lines:
            if keyword in log:
                result.append(log)
        
        return result
    
    def detect_burst_errors(logs_lines, keyword):

        error_counter = 0

        for log in logs_lines:
            
            if keyword in log:
                error_counter += 1
                if error_counter == 3 : return True
            else:
                error_counter = 0
            
        return False

    def ten_sec_error_logs(logs):

        keyword = "ERROR"
        ts_list = []

        for log in logs:
            message = log["message"]
            ts = log["timestamp"]

            if keyword in message:

                while len(ts_list) > 0 and (ts - ts_list[0]) > 10:
                    ts_list.pop(0)
                
                ts_list.append(ts)

            if len(ts_list) == 3 : return True
        return False




# print(LogAnalysis.simulate_grep(logs_line, keyword))
# print(LogAnalysis.detect_burst_errors(logs_line, keyword))
# print(LogAnalysis.ten_sec_error_logs(message_logs_line))
