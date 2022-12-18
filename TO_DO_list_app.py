import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a frame for the list
list_frame = tk.Frame(window)
list_frame.pack()

# Create a scrollbar
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox
listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure the scrollbar
scrollbar.config(command=listbox.yview)

# Create a frame for the input fields and buttons
input_frame = tk.Frame(window)
input_frame.pack()

# Create an entry field and a button
entry = tk.Entry(input_frame)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
button = tk.Button(input_frame, text="Add")
button.pack(side=tk.RIGHT)

# Define the button callback function
def add_item():
    # Get the text from the entry field
    item = entry.get()
    # Clear the entry field
    entry.delete(0, tk.END)
    # Add the item to the listbox
    listbox.insert(tk.END, item)

# Configure the button to call the callback function when clicked
button.config(command=add_item)

# Define a function to delete selected items from the list
def delete_items():
    # Get the indices of the selected items
    indices = listbox.curselection()
    # Iterate in reverse order to avoid index errors
    for index in reversed(indices):
        # Delete the item from the listbox
        listbox.delete(index)

# Create a delete button
delete_button = tk.Button(input_frame, text="Delete", command=delete_items)
delete_button.pack(side=tk.RIGHT)

# Define a function to toggle the checked state of an item
def toggle_item(event):
    # Get the index of the clicked item
    index = listbox.nearest(event.y)
    # Get the current text and checked state of the item
    text, checked = listbox.get(index)
    # Toggle the checked state
    checked = not checked
    # Update the item with the new checked state
    listbox.delete(index)
    listbox.insert(index, (text, checked))
    # Set the item color based on the checked state
    if checked:
        listbox.itemconfig(index, {'fg': 'gray'})
    else:
        listbox.itemconfig(index, {'fg': 'black'})

# Configure the listbox to call the toggle function when an item is clicked
listbox.bind('<Button-1>', toggle_item)

# Run the main loop
window.mainloop()
