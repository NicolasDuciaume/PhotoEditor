#testing git!
import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().

#if __name__ == "__main__":
 #   img = get_image()
  #  show(img)
answer = ""
loaded = False
while(answer != "Q"):
    print("L)oad Image")
    print("B)lur  E)dge detect  P)osterize  S)catter  T)int sepia")
    print("W)eighted grayscale X)treme contrast")
    print("Q)uit")
    answer = str(input(": "))
    if answer in ["L", "B", "E", "P", "S", "T", "W", "X","Q"]:
        if(answer == "L"):
            img = get_image()
            loaded = True
            show(img)        
        if(loaded == True):
            if(answer == "B"):
                img = blur(img)
                show(img)
            elif(answer == "P"):
                img = posterize(img)
                show(img)
            elif(answer == "E"):
                t = int(input("Threshold?: "))
                img = detect_edges_better(img,t)
                show(img)          
            elif(answer == "S"):
                img = scatter(img)
                show(img)
            elif(answer == "T"):
                img = sepia_tint(img)
                show(img)  
            elif(answer == "W"):
                img = weighted_grayscale(img)
                show(img)       
            elif(answer == "X"):
                img = extreme_contrast(img)
                show(img)  
            elif(answer == "Q"):
                sys.exit                    
        else:
            if(answer == "Q"):
                sys.exit   
            else:
                print("No image loaded")
                print("")
        
    else:
        print("No such command")
        print("")        

