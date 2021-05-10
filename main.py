# This program converts Celsius temperatures to Fahrenheit

import tkinter
import tkinter.messagebox

class TempConverterGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a temperature in Celsuis:')
        self.cels_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.cels_entry.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert to F', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The convert method is a callback function for
    # the Calculate button.

    def convert(self):
        # Get the value entered by the user into the
        # cels_entry widget.
        cels = float(self.cels_entry.get())

        # Convert kilometers to miles.
        fahrenheit = (9/5)*cels + 32

        # Display the results in an info dialog box.
        tkinter.messagebox.showinfo('Results:', str(cels) + ' in Celsius is equal to ' + str(fahrenheit) + ' in Fahrenheit.')

# Create an instance of the TempConverterGUI class.
if __name__ == '__main__':
    temp_conv = TempConverterGUI()
