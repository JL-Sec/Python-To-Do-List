# This is a python module that is to be imported into main.py

class todoManager:
    def __init__(self, to_do_file_path="data\\store_data.txt"):
        self.tasks = []
        self.to_do_file_path = to_do_file_path
        self.load_existing_data()

    # Load Existing Data, write code to read text file and load it into new list
    def load_existing_data(self):
        try:
            with open("data\\store_data.txt", "r") as myfile:
                for line in myfile:
                    line = line.strip()
                    self.tasks.append(line)
        except FileNotFoundError:
            print('File Not Found')
            pass

    # Save List To File
    def save_list_to_file(self):
        try:
            with open("data\\store_data.txt", "w") as myfile:
                for i in self.tasks:
                    myfile.write(f"{i}\n")

        except FileNotFoundError:
            print('File not found')
            pass
    
    # Adding a task
    def add_task(self, task):
        self.tasks.append(task)
    
    # Listing all tasks
    def list_tasks(self):
        for i in self.tasks:
            print('Task',self.tasks.index(i),'-',i)
    
    # Deleting a task
    def complete_task(self, index):
        try:
            self.tasks.pop(int(index))
            self.list_tasks()

        except:
            print('\nInvalid Index')

    # Quit Program
    def quit_program(self):
        return '3'

        
        

