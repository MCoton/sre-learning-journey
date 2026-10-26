def parse_system_logs() -> None:
    # Simulated raw log stream from an IT support environment
    log_stream = [
        "INFO: User password reset successfully",
        "WARNING: Disk space utilization at 85%",
        "ERROR: Failed to connect to authentication server",
        "INFO: Service heartbeat normal",
        "CRITICAL: Database node unreachable - failover triggered"
    ]
    print("\n" + "=" * 50)
    print("SRE LOG PARSER & INCIDENT FILTER")
    print("=" * 50)

    error_count = 0
    warning_count = 0

    # Loop throughn each lg line in the stream
    for log in log_stream:
        # Check condition using flow control
        if "CRITICAL" in log or "ERROR" in log:
            print(f" [ALERT] {log}")
            error_count += 1
        elif "WARNING" in log:
            print(f" [WARN] {log}")
            warning_count += 1
        else:
            print(f" [INFO] {log}")

    print("=" * 50)
    print(f" Summary: {error_count} Errors/Criticals | {warning_count} Warnings found.")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    parse_system_logs()