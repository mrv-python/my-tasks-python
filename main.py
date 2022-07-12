# My Tasks Demo

import json

# Main Program
def main():
  # Program Variables
  tasks = loadTasks()

  # Main Program Loop
  while True:
    # Get Menu Selection
    selection = getMenuSelection()

    if selection == "1":
      viewTasks(tasks)
    elif selection == "2":
      addTask(tasks)
    elif selection == "3":
      completeTask(tasks)
    elif selection == "4":
      removeTask(tasks)
    elif selection == "5":
      saveTasks(tasks)
      break
    else:
      print("Invalid Selection")

# Load Tasks from json file
def loadTasks():
  file = open("tasks.txt", "r")
  data = json.load(file)
  file.close()
  return data

# Print & Return User's Menu Selection
def getMenuSelection():
  print("\nMY TASKS MENU")
  print("1: View Tasks")
  print("2: Add a Task")
  print("3: Mark Task Completed")
  print("4: Remove a Task")
  print("5: Exit")
  return input("Selection (1-5): ")

# Display all tasks
def viewTasks(tasks):
  print("\nTASK LIST")
  for i in range(len(tasks)):
    task = tasks[i]
    if (task['completed']):
      print(f"{i}: \u2713 {task['task']} ({task['priority']} Priority)")
    else:
      print(f"{i}: \u2610 {task['task']} ({task['priority']} Priority)")

# Add a new task
def addTask(tasks):
  print("\nNEW TASK")
  task = input("Enter new task: ")
  priority = input("Enter task priority: ")
  tasks.append(newTask(task, priority))
  print("Task added")

# Return a dictionary for the given task
def newTask(task, priority):
  return {
    'task': task,
    'priority': priority,
    'completed': False
  }

# Mark a user defined task as completed
def completeTask(tasks):
  print("\nCOMPLETE TASK")
  index = int(input("Enter task #: "))
  tasks[index]['completed'] = True
  print(f"Task {index} completed")

# Remove a user defined tasks
def removeTask(tasks):
  print("\nREMOVE TASK")
  index = int(input("Enter task #: "))
  tasks.pop(index)
  print(f"Task {index} removed")

# Save tasks to json file
def saveTasks(tasks):
  # Save Tasks to file as json
  file = open("tasks.txt", "w")
  json.dump(tasks, file)
  file.close()

# Call main() to begin program
main()