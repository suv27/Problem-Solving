events = [
    {"ip": "1.1.1.1", "action": "LOGIN_SUCCESS"},
    {"ip": "2.2.2.2", "action": "LOGIN_FAIL"},
    {"ip": "3.3.3.3", "action": "WAF_BLOCK"},
    {"ip": "2.2.2.2", "action": "LOGIN_FAIL"},
    {"ip": "4.4.4.4", "action": "BOT_DETECTED"},
    {"ip": "1.1.1.1", "action": "LOGIN_FAIL"},
]


def unique_suspicious_ips(events):

    suspicious_actions = {"LOGIN_FAIL", "WAF_BLOCK", "BOT_DETECTED"}

    suspicious_ips_set = set()

    for log in events:
        action = log["action"]
        ip = log["ip"]

        if action in suspicious_actions:
            suspicious_ips_set.add(ip)
        else:
            continue
    
    return suspicious_ips_set



print(unique_suspicious_ips(events))