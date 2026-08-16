import logging
logging.basicConfig(level=logging.INFO)

def analyze_log():
    try:
        error_counter = 0
        info_counter = 0
        with open("file.log") as file:
            for line in file:
                if "ERROR" in line:
                    error_counter += 1
                elif "INFO" in line:
                    info_counter += 1
            return error_counter, info_counter          
    except FileNotFoundError:
        print("file not found")
        return 0,0

def print_summary(error_count, info_count):

    logging.info(f"count is: {info_count}")
    logging.error(f"count is: {error_count}")

error, info = analyze_log()

print_summary(error, info)