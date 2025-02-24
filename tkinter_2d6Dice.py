# 2D6

from tkinter import *

class Application(Frame):
    """ A gui application with three buttons. """
    def __init__(self , master):
        """ Initialise the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create three buttons that do nothing. """
        # Create first button
        self.bttn1 = Button(self, text="1D6 ")
        self.bttn1.grid()

        # create second button
        self.bttn2 = Button(self, text="2D6 ")
        self.bttn2.grid()        

        # Create third button
        self.bttn3 = Button(self, text="1D3 ")
        self.bttn3.grid()
       
        # Create fourth button
        self.bttn4 = Button(self, text="D66 ")
        self.bttn4.grid()

        # Create fifth button
        self.bttn5 = Button(self, text="XDX ")
        self.bttn5.grid()

        # Create sixth button
        self.bttn6 = Button(self, text="Create room ")
        self.bttn6.grid()
        
        # Create seventh button
        self.bttn7 = Button(self, text="Battle menu ")
        self.bttn7.grid()

# Main
root = Tk()
root.title("2D6")
root.geometry("200x300")
app = Application(root)

# kick off the window's event loop
root.mainloop()