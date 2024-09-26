"""
This code implements a simple task management system that allows users to add, view, complete, and delete tasks.
The system also provides recommendations based on the task's name using a predefined list of keywords.
Users interact with the system via a command-line interface where they can choose different actions.
"""

# Define the Task class to represent individual tasks within the system
class Task:
    def __init__(self, name, deadline):
        # Initialize the Task object with a name and deadline provided by the user
        # Also, set the completion status to False by default since the task is initially incomplete
        self.name = name
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        # A method to update the task's status to completed when the user indicates the task is done
        self.completed = True

# Define the SelfManagementSystem class to manage multiple tasks
class SelfManagementSystem:
    def __init__(self):
        # Initialize the system with an empty list to hold all the tasks created by the user
        self.tasks = []

    def add_task(self, name, deadline):
        # Create a new Task object using the provided name and deadline
        task = Task(name, deadline)
        # Add the newly created task to the list of tasks
        self.tasks.append(task)
        # Get a relevant recommendation for the task based on its name
        recommendation = get_recommendation(name)
        # Inform the user that the task has been added and display the recommendation
        print(f"Task '{name}' added with a deadline of {deadline}.")
        print(f"Recommendation: {recommendation}")

    def view_tasks(self):
        # Check if the list of tasks is empty before attempting to display them
        if not self.tasks:
            print("No tasks available.")
        else:
            # Loop through the list of tasks and print details for each task
            for i, task in enumerate(self.tasks, 1):
                # Determine the current status of the task (Completed or Not Completed)
                status = "Completed" if task.completed else "Not Completed"
                # Print the task's details including its name, deadline, and completion status
                print(f"{i}. Task: {task.name}, Deadline: {task.deadline}, Status: {status}")

    def mark_task_completed(self, task_number):
        # Mark the task at the specified index as completed
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_completed()
            print(f"Task '{self.tasks[task_number].name}' marked as completed.")
        else:
            # If the task number is out of range, notify the user that it's invalid
            print("Invalid task number.")

    def delete_task(self, task_number):
        # Remove the task at the specified index from the list of tasks
        if 0 <= task_number < len(self.tasks):
            task_name = self.tasks.pop(task_number).name
            print(f"Task '{task_name}' deleted.")
        else:
            # If the task number is out of range, notify the user that it's invalid
            print("Invalid task number.")

# Define a list of keywords and corresponding recommendations
# This is used to provide suggestions to the user based on the task name
keywords = ["time management", "productivity", "focus", "wash car"]
recommendations = [
    "Use a calendar to schedule your tasks.",
    "Take regular breaks to maintain high productivity levels.",
    "Eliminate distractions to improve focus.",
    "Remember to wash your car every two weeks."
]

def get_recommendation(keyword):
    # Check if the provided keyword is in the list of known keywords
    if keyword in keywords:
        # If found, return the corresponding recommendation based on the index
        index = keywords.index(keyword)
        return recommendations[index]
    else:
        # If the keyword is not found, return a default message
        return "No recommendation found for this keyword."

# Command-line interface for interacting with the task management system
def main():
    # Create an instance of SelfManagementSystem to manage the user's tasks
    system = SelfManagementSystem()
    while True:
        # Display the menu options to the user
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            # Prompt the user for task details and add a new task to the system
            name = input("Enter task name: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            system.add_task(name, deadline)
        elif choice == '2':
            # Display all tasks currently in the system
            system.view_tasks()
        elif choice == '3':
            # Prompt the user for a task number to mark as completed
            task_number = int(input("Enter the task number to mark as completed: ")) - 1
            system.mark_task_completed(task_number)
        elif choice == '4':
            # Prompt the user for a task number to delete from the system
            task_number = int(input("Enter the task number to delete: ")) - 1
            system.delete_task(task_number)
        elif choice == '5':
            # Exit the program when the user chooses to quit
            print("Exiting the system.")
            break
        else:
            # Handle invalid menu choices and prompt the user to try again
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    # Run the main function to start the program when the script is executed
    main()
