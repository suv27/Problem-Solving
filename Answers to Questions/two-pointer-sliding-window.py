provided_logs = [
    {"ip": "1.1.1.1", "timestamp": 1,  "status": 401},
    {"ip": "1.1.1.1", "timestamp": 4,  "status": 403},
    {"ip": "2.2.2.2", "timestamp": 5,  "status": 200},
    {"ip": "1.1.1.1", "timestamp": 8,  "status": 500},
    {"ip": "2.2.2.2", "timestamp": 9,  "status": 403},
    {"ip": "2.2.2.2", "timestamp": 12, "status": 404},
    {"ip": "2.2.2.2", "timestamp": 14, "status": 401},
]


class TwoPointerSlidingWindow:
    
    def queue_base_sliding_window(logs):
        '''
        Docstring for TwoPointerSlidingWindow
        How to Get it Done:
        - I will iterate over the list of logs once
        - check if the status value is ≥ 400
        - check if current timestamp minus the oldest timestamp in the window is greater than 10, pop and do it again
        - check if current timestamp minus the top timestamp is greater than 10, pop and do it again
        '''
        suspicious_ips = []
        temp_dict_ts = {}

        for log in logs:
            status = log["status"]
            ts = log["timestamp"]
            ip = log["ip"]

            if status >= 400:
                while temp_dict_ts[ip] and ts - temp_dict_ts[ip[0]] > 10:
                    temp_dict_ts[ip[0]].pop
                
                temp_dict_ts.append(ip)

                if len(temp_dict_ts[ip]) >= 3:
                    suspicious_ips.append(temp_dict_ts[ip])
                    

        return suspicious_ips

print(TwoPointerSlidingWindow.queue_base_sliding_window(logs=provided_logs))
