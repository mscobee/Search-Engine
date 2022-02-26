from collections import deque


class My_Queue:
    def __init__(self) -> None:
        # linked list to be used to implement the queue
        self.l_list = deque()

    def push(self,data):
        self.l_list.append(data)
        
    def pop(self):
        return self.l_list.popleft()
    
    def print(self):
        print(self.l_list)
        
    def get_queue(self):
        return self.l_list
