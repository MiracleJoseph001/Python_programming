import datetime 
def write_log(file_path, message):
    """function that append logs to a file with time stamp"""
    try:
        with open(file_path, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} + {message} \n")
        print(f"log:{message}")
    except Exception as e:
        print(f"error written log: {e}")
def read_log(file_path):
    """functioon is meant to read content from the file"""
    try:
        with open(file_path, "r") as file:
            print(f"\n ----- log----------------")
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No logs found / 404 ")
    except Exception as e:
        print(f"error written log: {e}")        
if __name__== "__main__":
    log_file = "filename.txt"
    while True:
        print("\n Select log manager Option")
        print("1 Write log Entry")
        print("2 Read all log entry ")
        print("3 Exit")
          
        choice = input("Pick an Option:")
        if choice == "1":
            log_message = input("Enter your log message:")
            write_log(log_file, log_message)
        elif choice =="2":
            read_log(log_file)
        elif choice =="3":
            print("Bye bye")
            break
        else:
            print("Invalid Selection")


