from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from PIL import ImageTk, Image, ImageOps, ImageFilter, ImageChops
import matplotlib.pyplot as plt 


class imageCanvas():
    def __init__(self, parent):
        self.original_image = False
        self.current_image = False
        self.canvas = Canvas(parent, width=400, height=400, bg="gray")
        self.canvas.place(x = 200, y = 20)
       
    
    def load_image(self):
        # prompet the user to select an image only accept png and jpg 
        image_path = filedialog.askopenfilename(
                title = "Choose an image",
                filetypes=[("image files", ('.png', '.jpg'))]
                )
        
        # check if valid path is returned form the prompet 
        if image_path:
            # open the image and resize it and load it to the canvas
            self.current_image = Image.open(image_path).convert("RGB")
            self.current_image = self.current_image.resize((400, 400), Image.ANTIALIAS)
            self.original_image = self.current_image
            self.write_to_canvas(self.current_image)
    
    def write_to_canvas(self, image):
        imgtk = ImageTk.PhotoImage(image)
        self.canvas.image = imgtk
        self.canvas.create_image(0, 0, image = imgtk, anchor=NW)
    
    # convet the image to gray scale 
    def toGray(self):
        # if the image is uploaded
        if self.current_image:
            self.current_image = self.current_image.convert('LA')
            self.write_to_canvas(self.current_image)

    # conver image to binary 
    def toBinary(self):
        # if the image is uploaded
        if self.current_image:
            self.current_image = self.current_image.convert('1')
            self.write_to_canvas(self.current_image)

    # undo all the change by replac the image with th eoriginal one 
    def reset(self):
        # if the image is uploaded
        if self.current_image:
            self.current_image = self.original_image
            self.write_to_canvas(self.current_image)


    # display histogram of the image using matplotlib
    def histogram(self):
        # if the image is uploaded
        if self.current_image:
            # if its RBG then show the three colors histogram
            if self.current_image.mode == "RGB":
                r, g, b = self.current_image.split()
                r = r.histogram()
                g = g.histogram()
                b = b.histogram()
                plt.plot(range(len(r)), r , color = 'red')
                plt.plot(range(len(g)), g , color = 'green')
                plt.plot(range(len(b)), b , color = 'blue')
                plt.xlabel("Colors")
                plt.ylabel("Frequency")
                plt.title("Image Histogram")
                plt.show()
                
            else: # or show only single color histogram
                data = self.current_image.convert("LA").histogram()
                plt.plot( range(len(data)), data, color = 'blue')
                plt.xlabel("Colors")
                plt.ylabel("Frequency")
                plt.title("Image Histogram")
                plt.show()


    # invert the image
    def image_complement(self):
        # if the image is uploaded
        if self.current_image:
            self.current_image = ImageOps.invert(self.current_image)
            self.write_to_canvas(self.current_image)

    # detect all the images at the image after convert it to grayscale 
    def edge_detection(self):
        # if the image is uploaded
        if self.current_image:
            self.current_image = self.current_image.convert("L")
            self.current_image = self.current_image.filter(ImageFilter.FIND_EDGES)
            self.write_to_canvas(self.current_image)


    # rotate right
    def rotate_right(self):
        # if the image is uploaded
        if self.current_image:
            self.current_image = self.current_image.rotate(-90)
            self.write_to_canvas(self.current_image)

    # rotate left
    def rotate_left(self):
        # if the image is uploaded
        if self.current_image:
            self.current_image = self.current_image.rotate(90)
            self.write_to_canvas(self.current_image)

    

class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        parent.title('Image Proccessing Project Mahmoud Ramadan - 181029') 
        parent.geometry("640x580")
        parent.resizable(False, False)
        self.canvas = imageCanvas(parent)
        
        # create GUI elements [buttuns] of the program 

        # basic operation label
        Label(parent, width = 19, height = 5, anchor=CENTER, text="Basic Operation").place(x = 10, y = 10)

        # upload image button
        Button(parent, text="Upload Image", height=2, width=12, command=self.canvas.load_image).place(x = 30, y= 100)

        # convert to gray button 
        Button(parent, text="RGB to Gray", height=2, width=12, command=self.canvas.toGray).place(x = 30, y= 160)

        # convert tot binary button
        Button(parent, text="Convert to Binary", height=2, width=12, command=self.canvas.toBinary).place(x = 30, y= 220)

        # RESET button
        Button(parent, text="RESET", height=2, width=12, command=self.canvas.reset).place(x = 30, y= 280)

        # Advanced Operation Label
        Label(parent, width = 19, height = 5, anchor=CENTER, text="Advanced Operation").place(x = 15, y = 450)

        # Histogram button
        Button(parent, text="Histogram", height=2, width=12, command=self.canvas.histogram).place(x = 180, y= 450)

        # Complement image
        Button(parent, text="Complement Image", height=2, width=15, command=self.canvas.image_complement).place(x = 320, y= 450)

        # edge detection
        Button(parent, text="Edge Detection", height=2, width=14, command=self.canvas.edge_detection).place(x = 480, y= 450)

        # rotate clockwise
        Button(parent, text="Rotate Clockwise", height=2, width=14, command=self.canvas.rotate_right).place(x = 260, y= 510)

        # rotate Anti-clockwise
        Button(parent, text="Rotate Anti-Clockwise", height=2, width=16,command=self.canvas.rotate_left).place(x = 410, y= 510)




if __name__ == "__main__":
    root = Tk()
    MainApplication(root)
    root.mainloop()
