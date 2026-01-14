'''


Task 2 
Find First Repeated IP

Given a list of IPs, return the first IP that appears more than once.
If none exist, return None.

Task 3
You expect logs from servers 1 → N, but some servers didnt report.
Given a list of server IDs that reported, return the missing IDs.

Input
expected_servers = 6
reported = [1, 2, 4, 6]

Output
[3, 5]
'''


logs = [
    "INFO 2024-01-01 IP=1.1.1.1 ACTION=LOGIN_FAIL",
    "WARN 2024-01-01 IP=2.2.2.2 ACTION=WAF_BLOCK",
    "INFO 2024-01-01 IP=1.1.1.1 ACTION=LOGIN_SUCCESS",
]

ips = [
    "1.1.1.1",
    "2.2.2.2",
    "3.3.3.3",
    "2.2.2.2",
    "1.1.1.1"
]

expected_servers = 6
reported_servers = [1, 2, 4, 6]

class StringParsing:
    
    def find_ip_in_logs(logs_events):

        found_str = {}

        for log in logs_events:
            split_log = log.split(" ")
            ip = split_log[2][3:]

            # feedback
            '''
            for part in split_log:
                if part.startswith("IP="):
                    ip = part.split("=")[1]
            '''

            if ip not in found_str:
                found_str[ip] = 1
            else:    
                found_str[ip] += 1
        
        return found_str


    def find_first_ip_repeated(ips):

        ips_found = set()

        for ip in ips:
            if ip not in ips_found:
                ips_found.add(ip)
            else:
                return ip
        
        return None
    
    
    def missing_server_collection(expected, reported):

        missing_servers = set()
        reported_set = set(reported)

        for server in range(1, expected + 1):
            
            if server not in reported_set:
                missing_servers.add(server)
        
        return missing_servers
    

# print(StringParsing.find_ip_in_logs(logs))
# print(StringParsing.find_first_ip_repeated(ips))
# print(StringParsing.missing_server_collection(expected_servers, reported_servers))
