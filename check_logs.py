import re
from datetime import datetime

log_file = 'app.log'

def parse_log_line(line):
    match = re.match(r'^(.*?) - (.*?) - (.*?) - (.*?) - (.*?)$', line)
    if match:
        timestamp_str, name, level, message, hostname = match.groups()
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
        return timestamp, name, level, message, hostname
    return None

def check_logs():
    with open(log_file, 'r') as file:
        logs = file.readlines()

    previous_timestamp = None
    for line in logs:
        parsed_line = parse_log_line(line)
        if parsed_line:
            timestamp, name, level, message, hostname = parsed_line
            print(f"{timestamp} - {name} - {level} - {message} - {hostname}")
            if previous_timestamp and timestamp < previous_timestamp:
                print("Log order error: Log messages out of order")
            previous_timestamp = timestamp
        else:
            print("Log format error")

if __name__ == "__main__":
    check_logs()
