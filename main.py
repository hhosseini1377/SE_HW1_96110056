from tkinter import *

# globally declare the expression variable
expression = ""

# Driver code
if __name__ == "__main__":

	# set the background colour of GUI window
    gui.configure(background="light green")
 
    # set the title of GUI window
    gui.title("Simple Calculator")
 
    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    equation = StringVar()
 
    # create the text entry box for showing the expression .
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
 