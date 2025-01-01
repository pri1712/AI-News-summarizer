

def log_to_file(file_path,data):
    """Logs data to a specified file."""
    with open(file_path, "a") as file:
        file.write(f"{data}\n")


