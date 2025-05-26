def read_log_lines(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file]


def parse_line(line):
    """Parse a single log line into a dictionary with 'timestamp', 'type', and 'message' keys.
    Example input: '[2025-05-26 10:00:00] INFO - Started processing job 123'
    Example output:
    {
        'timestamp': '2025-05-26 10:00:00',
        'type': 'INFO',
        'message': 'Started processing job 123'
    }
    """
    line_parts = line.split("] ")
    timestamp = line_parts[0][1:]
    line_parts2 = line_parts[1].split(" - ")
    type_text = line_parts2[0]
    message = line_parts2[1]
    return {"timestamp": timestamp, "type": type_text, "message": message}


def filter_errors(log_entries):
    """Takes a list of parsed log entries and returns only those with type 'ERROR'."""
    return [entry for entry in log_entries if entry["type"] == "ERROR"]


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
