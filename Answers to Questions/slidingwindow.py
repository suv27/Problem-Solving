ip_logs = [
    {"ip": "1.1.1.1", "timestamp": 1},
    {"ip": "1.1.1.1", "timestamp": 5},
    {"ip": "1.1.1.1", "timestamp": 8},
    {"ip": "2.2.2.2", "timestamp": 10},
    {"ip": "1.1.1.1", "timestamp": 12},
    {"ip": "2.2.2.2", "timestamp": 21},
    {"ip": "1.1.1.1", "timestamp": 23},
    {"ip": "2.2.2.2", "timestamp": 24},
    {"ip": "2.2.2.2", "timestamp": 30},
]

logs = [
    {"ip": "1.1.1.1", "timestamp": 1},
    {"ip": "1.1.1.1", "timestamp": 3},
    {"ip": "2.2.2.2", "timestamp": 4},
    {"ip": "1.1.1.1", "timestamp": 7},
    {"ip": "2.2.2.2", "timestamp": 8},
    {"ip": "2.2.2.2", "timestamp": 9},
]

class SlidingWindow:

    def failed_login_rate_detection(logs) -> dict:

        ip_stored = {}
        suspicious_ip = []

        for log in logs:
            ip = log["ip"]
            ts = log["timestamp"]

            if ip not in ip_stored:
                ip_stored[ip] = []

            # while the IP exist in the store and new ts - old ts > 10
            while ip_stored[ip] and (ts - ip_stored[ip][0]) > 10:
                ip_stored[log["ip"]].pop(0)
            
            # Add ts into store
            ip_stored[ip].append(ts)

            # detect suspicious ip
            if len(ip_stored[ip]) >= 3 and ip not in suspicious_ip:
                suspicious_ip.append(ip)
        
        return suspicious_ip

    def three_second_window(logs) -> dict:

        ip_stored = {}
        suspicious_ip = []

        for log in logs:
            ip = log["ip"]
            ts = log["timestamp"]

            if ip not in ip_stored:
                ip_stored[ip] = []
            
            while ip_stored[ip] and (ts - ip_stored[ip][0]) > 5:
                ip_stored[ip].pop(0)
            
            ip_stored[ip].append(ts)

            if len(ip_stored[ip]) >= 2 and ip not in suspicious_ip:
                suspicious_ip.append(ip)
            
        return suspicious_ip

print(SlidingWindow.three_second_window(logs))