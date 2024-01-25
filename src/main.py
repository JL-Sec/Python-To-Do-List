# Main.py

from todo import todoManager

def main():

    # Create instance of TodoManager and set variables
    todo = todoManager()
    user_input = ''

    # Welcome Message
    print('Welcome To To Do List.')

    # Print Menu Options
    while user_input != '4':
        print('\nSelect from the following options:\n\n1. Create Task\n2. View Task\n3. Delete Task\n4. Quit Program\n')
        
        # Get User Input
        user_input = input('Enter Option Number: ')

        # Perform Actions Based on User Input
        if user_input == '1':
            newTask = input('\nWrite Task To Add To List: ')
            
            # Checks for blank task
            if not newTask:
                pass
            else:
                todo.add_task(newTask)
                todo.save_list_to_file()
                print('\n'+newTask, 'added to list')

        # If user selects list tasks
        elif user_input == '2':
            todo.list_tasks()   

        # If user selects delete task
        elif user_input == '3':
            print('\nCurrent List:\n')
            todo.list_tasks()
            print('\n')
            get_index = input('Enter Index Number for Complete Task: ')
            todo.complete_task(get_index)
            todo.save_list_to_file()

        # If user selects quit program
        elif user_input == '4':
            todo.quit_program()    


if __name__== "__main__":
    main()