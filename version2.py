"""
This code implements a simple task management system that allows users to add, view, complete, and delete tasks.
The system also provides recommendations based on the task's name using a predefined list of keywords.
Users interact with the system via a graphical user interface (GUI) created with the Tkinter library.
"""

import tkinter as tk  # Import the Tkinter module, which is the standard Python interface to create GUIs.
from tkinter import messagebox  # Import the messagebox module from Tkinter, used to display message boxes.
from tkinter import simpledialog  # Import the simpledialog module from Tkinter, used to prompt the user for input.

# The Task class represents a task with a name, deadline, and completion status.
class Task:
    def __init__(self, name, deadline):
        self.name = name  # The name of the task
        self.deadline = deadline  # The deadline for the task
        self.completed = False  # Initially, the task is not completed

    # This method marks the task as completed by setting the 'completed' attribute to True.
    def mark_completed(self):
        self.completed = True

# The SelfManagementSystem class manages a list of tasks and provides methods to add, view, complete, and delete tasks.
class SelfManagementSystem:
    def __init__(self):
        self.tasks = []  # Initialize an empty list to store tasks

    # This method adds a new task to the system and shows a recommendation based on the task name.
    def add_task(self, name, deadline):
        task = Task(name, deadline)  # Create a new Task object
        self.tasks.append(task)  # Add the new task to the list of tasks
        recommendation = get_recommendation(name)  # Get a recommendation based on the task name
        # Display a message box with task details and the recommendation
        messagebox.showinfo("Task Added", f"Task '{name}' added with a deadline of {deadline}.\nRecommendation: {recommendation}")

    # This method displays all the tasks currently in the system.
    def view_tasks(self):
        if not self.tasks:  # Check if there are no tasks in the list
            messagebox.showinfo("View Tasks", "No tasks available.")
        else:
            tasks_str = ""  # Initialize an empty string to accumulate task details
            for i, task in enumerate(self.tasks, 1):  # Loop through each task with an index starting from 1
                status = "Completed" if task.completed else "Not Completed"  # Determine the task's status
                # Append task details to the string
                tasks_str += f"{i}. Task: {task.name}, Deadline: {task.deadline}, Status: {status}\n"
            # Display the accumulated task details in a message box
            messagebox.showinfo("View Tasks", tasks_str)

    # This method marks a specific task as completed.
    def mark_task_completed(self, task_number):
        if 0 <= task_number < len(self.tasks):  # Check if the task number is valid
            self.tasks[task_number].mark_completed()  # Mark the task as completed
            messagebox.showinfo("Mark Task", f"Task '{self.tasks[task_number].name}' marked as completed.")
        else:
            messagebox.showerror("Error", "Invalid task number.")

    # This method deletes a specific task from the system.
    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):  # Check if the task number is valid
            task_name = self.tasks.pop(task_number).name  # Remove the task from the list and get its name
            messagebox.showinfo("Delete Task", f"Task '{task_name}' deleted.")
        else:
            messagebox.showerror("Error", "Invalid task number.")

# Define keywords and their corresponding recommendations for task management.
keywords = ["time management", "productivity", "focus", "wash car"]
recommendations = [
    "Use a calendar to schedule your tasks.",  # Recommendation for "time management"
    "Take regular breaks to maintain high productivity levels.",  # Recommendation for "productivity"
    "Eliminate distractions to improve focus.",  # Recommendation for "focus"
    "Remember to wash your car every two weeks."  # Recommendation for "wash car"
]

# This function returns a recommendation based on the provided keyword.
def get_recommendation(keyword):
    if keyword in keywords:  # Check if the keyword exists in the keywords list
        index = keywords.index(keyword)  # Get the index of the keyword
        return recommendations[index]  # Return the corresponding recommendation
    else:
        return "No recommendation found for this keyword."  # Return a default message if no recommendation is found

# The TaskManagementApp class sets up the graphical user interface for managing tasks.
class TaskManagementApp:
    def __init__(self, root):
        self.system = SelfManagementSystem()  # Initialize the task management system
        self.root = root  # Reference to the main application window
        self.root.title("Task Management System")  # Set the window title

        # Create and place the "Add Task" button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        # Create and place the "View Tasks" button
        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_button.pack(pady=10)

        # Create and place the "Mark Task as Completed" button
        self.complete_button = tk.Button(root, text="Mark Task as Completed", command=self.mark_task_completed)
        self.complete_button.pack(pady=10)

        # Create and place the "Delete Task" button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=10)

    # This method prompts the user to enter a new task and adds it to the system.
    def add_task(self):
        name = simpledialog.askstring("Task Name", "Enter task name:")  # Ask for the task name
        if name:
            deadline = simpledialog.askstring("Task Deadline", "Enter task deadline (YYYY-MM-DD):")  # Ask for the task deadline
            if deadline:
                self.system.add_task(name, deadline)  # Add the task to the system

    # This method displays the list of tasks.
    def view_tasks(self):
        self.system.view_tasks()  # Call the view_tasks method from the system

    # This method prompts the user to enter the number of a task to mark as completed.
    def mark_task_completed(self):
        task_number = simpledialog.askinteger("Task Number", "Enter the task number to mark as completed:") - 1  # Subtract 1 to convert to 0-based index
        if task_number is not None:
            self.system.mark_task_completed(task_number)  # Mark the task as completed

    # This method prompts the user to enter the number of a task to delete.
    def delete_task(self):
        task_number = simpledialog.askinteger("Task Number", "Enter the task number to delete:") - 1  # Subtract 1 to convert to 0-based index
        if task_number is not None:
            self.system.delete_task(task_number)  # Delete the task from the system

# The entry point of the application. Initializes the Tkinter main loop.
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = TaskManagementApp(root)  # Create an instance of the TaskManagementApp class
    root.mainloop()  # Start the Tkinter event loop
