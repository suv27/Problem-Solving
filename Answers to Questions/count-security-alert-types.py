alerts = [
    "WAF_BLOCK",
    "BOT_DETECTED",
    "WAF_BLOCK",
    "LOGIN_FAIL",
    "BOT_DETECTED",
    "WAF_BLOCK",
    "LOGIN_FAIL",
    "LOGIN_FAIL"
]

structure_alert = [
    {"type": "WAF_BLOCK", "severity": "high"},
    {"type": "BOT_DETECTED", "severity": "medium"},
    {"type": "WAF_BLOCK", "severity": "high"},
    {"type": "LOGIN_FAIL", "severity": "low"},
    {"type": "LOGIN_FAIL", "severity": "low"},
    {"type": "BOT_DETECTED", "severity": "medium"},
]

high_sev_alerts = [
    {"type": "WAF_BLOCK", "severity": "high"},
    {"type": "BOT_DETECTED", "severity": "medium"},
    {"type": "WAF_BLOCK", "severity": "high"},
    {"type": "LOGIN_FAIL", "severity": "low"},
    {"type": "LOGIN_FAIL", "severity": "low"},
    {"type": "BOT_DETECTED", "severity": "medium"},
    {"type": "LOGIN_FAIL", "severity": "HIGH"},
]

top_k_high_sev_alerts = [
    {"type": "WAF_BLOCK", "severity": "high"},
    {"type": "BOT_DETECTED", "severity": "medium"},
    {"type": "WAF_BLOCK", "severity": "high"},
    {"type": "LOGIN_FAIL", "severity": "high"},
    {"type": "LOGIN_FAIL", "severity": "high"},
    {"type": "BOT_DETECTED", "severity": "medium"},
    {"type": "LOGIN_FAIL", "severity": "low"},
    {"type": "SQL_INJECTION", "severity": "high"},
]


class SecurityAlerts:

    def count_security_alert_types(alerts) -> dict:
        
        alert_type_counter = {}

        for alert in alerts:
            if alert not in alert_type_counter:
                alert_type_counter[alert] = 1
            else:
                alert_type_counter[alert] += 1

        return alert_type_counter
            

    def count_structure_security_alert_types(alerts) -> dict:

        structure_alert_type_counter = {}

        for alert in alerts:
            if alert["type"] not in structure_alert_type_counter:
                structure_alert_type_counter[alert["type"]] = 1
            else:
                structure_alert_type_counter[alert["type"]] += 1
        
        return structure_alert_type_counter

    def count_alert_with_high_severity(alerts) -> dict:

        high_sev_alert_counter = {}

        for alert in alerts:
            if alert["severity"] == "high" or alert["severity"] == "HIGH":
                if alert["type"] not in high_sev_alert_counter:
                    high_sev_alert_counter[alert["type"]] = 1
                else:
                    high_sev_alert_counter[alert["type"]] += 1
        
        return high_sev_alert_counter

    def count_top_k_high_sev_alerts(alerts) -> dict:

        top_2_high_sev_alert_counter = {}

        for alert in alerts:
            if alert["severity"].lower() == "high":
                if alert["type"] not in top_2_high_sev_alert_counter:
                    top_2_high_sev_alert_counter[alert["type"]] = 1
                else:
                    top_2_high_sev_alert_counter[alert["type"]] += 1
        
        return dict(sorted(top_2_high_sev_alert_counter.items(), key=lambda alert: alert[1], reverse=True)[:2])


# print(SecurityAlerts.count_security_alert_types(alerts))
# print(SecurityAlerts.count_structure_security_alert_types(structure_alert))
# print(SecurityAlerts.count_alert_with_high_severity(high_sev_alerts))
# print(SecurityAlerts.count_top_k_high_sev_alerts(top_k_high_sev_alerts))
