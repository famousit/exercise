def read_log_lines(filepath):
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def parse_line(line):
    """Parse a single log line into a dictionary with 'timestamp', 'type', and 'message' keys."""
    # Example: '[2025-05-26 10:00:00] INFO - Started processing job 123'
    import re
    match = re.match(r'\[(.*?)\]\s+(\w+)\s*-\s*(.*)', line)
    if match:
        timestamp, log_type, message = match.groups()
        return {
            'timestamp': timestamp,
            'type': log_type,
            'message': message
        }
    else:
        return {
            'timestamp': '',
            'type': '',
            'message': line
        }


def filter_errors(log_entries):
    """Takes a list of parsed log entries and returns only those with type 'ERROR'."""
    return [entry for entry in log_entries if entry.get('type') == 'ERROR']


def main():
    filepath = 'log.txt'
    
    # Step 1: Read lines from the file
    lines = read_log_lines(filepath)

    # Step 2: Parse lines into structured data
    log_entries = [parse_line(line) for line in lines]

    # Step 3: Filter only error entries
    error_entries = filter_errors(log_entries)

    # Step 4: Print out the errors
    for error in error_entries:
        print(f"[{error['timestamp']}] {error['message']}")

if __name__ == "__main__":
    main()
