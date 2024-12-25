class QueueOfCall:
    def __init__(self):
        self.queue = []
        self.size = -1

    def add_call(self, call):
        print(f"Adding call from '{call}' to the queue")
        self.queue.append(call)
        self.size += 1
    def process_call(self):
        if self.size == -1:
            print("No calls to process")
        else:
            print(f"Processing call from '{self.queue[0]}'")
            self.queue.remove(self.queue[0])
            self.size -= 1
    def view_queue(self):
        if self.size == -1:
            print("No calls to view")
        else:
            print(self.queue)
    def exit(self):
        print("Thank you for using call center simulator!")
