import QueueOfCall

def main():
    print("CALL CENTER SIMULATOR")
    print("Welcome to call center simulator!")
    print("1.Add a call")
    print("2.Process a call")
    print("3.View Queue")
    print("4.Exit")
    CallQueue = QueueOfCall.QueueOfCall()
    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            caller_id = input("Enter caller id: ")
            CallQueue.add_call(caller_id)
        elif choice == "2":
            CallQueue.process_call()
        elif choice == "3":
            CallQueue.view_queue()
        elif choice == "4":
            CallQueue.exit()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
