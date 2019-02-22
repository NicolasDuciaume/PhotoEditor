""" SYSC 1005 A Fall 2018.

Filters for a photo-editing application.
"""

from Cimpl import *
import random

def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
        
    return new_image

def weighted_grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a weighted grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = weighted_grayscale(image)
    >>> show(gray_image)
    """    
    new_image = copy(image)
    for x, y, (r, g, b) in image:    
        brightness = r * 0.299 + g * 0.587 + b * 0.114
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
         
    return new_image         


def extreme_contrast(image):
    """ (Cimpl.Image) -> Cimpl.Image 
     
        Return a copy of image, maximizing the contrast between     
        the light and dark pixels. 
     
        >>> image = load_image(choose_file())     
        >>> new_image = extreme_contrast(image)     
        >>> show(new_image) 
        """    
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        if(0 <= r <= 127):
            r = 0
        else:
            r = 255
        if(0 <= g <= 127):
            g = 0
        else:
            g = 255        
        if(0 <= b <= 127):
            b = 0
        else:
            b = 255        
        color = create_color(r,g,b)
        set_color(new_image,x,y,color)
    return new_image


def sepia_tint(image):     
    """ (Cimpl.Image) -> Cimpl.Image 
 
    Return a copy of image in which the colours have been   
    converted to sepia tones. 
 
    >>> image = load_image(choose_file())    
    >>> new_image = sepia_tint(image)    
    >>> show(new_image)    
    """ 
    new_image = copy(image)
    gimage = weighted_grayscale(new_image)
    
    for x, y, (r, g, b) in gimage:
        if(r < 63):
            new_b = b * 0.9
            new_r = r * 1.1
        elif(63 <= r <= 191):
            new_b = b * 0.85
            new_r = r * 1.15
        else:
            new_b = b * 0.93
            new_r = r * 1.08
        color = create_color(new_r,g,new_b)
        set_color(gimage,x,y,color)
    return gimage

def _adjust_component(amount):
    """ (int) -> int 
     
        Divide the range 0..255 into 4 equal-size quadrants,     
        and return the midpoint of the quadrant in which the     
        specified amount lies. 
     
        >>> _adjust_component(10)     
        31     
        >>> _adjust_component(85)    
        95     
        >>> _adjust_component(142)    
        159     
        >>> _adjust_component(230)     
        223    
        """    
    if(amount <= 63):
        mid = 31
    elif(64 <= amount <= 127):
        mid = 95
    elif(128 <= amount <= 191):
        mid = 159
    else:
        mid = 223
        
    return mid


def posterize(image):     
    """ 
    (Cimpl.Image) -> Cimpl.Image 
 
    Return a "posterized" copy of image. 
 
    >>> image = load_image(choose_file())     
    >>> new_image = posterize(image)     
    >>> show(new_image)      
    """ 
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        new_r = _adjust_component(r)
        new_g = _adjust_component(g)
        new_b = _adjust_component(b)
        color = create_color(new_r,new_g,new_b)
        set_color(new_image,x,y,color)
    return new_image        


def detect_edges(image, threshold):     
    """ (Cimpl.Image, float) -> Cimpl.Image       
    Return a new image that contains a copy of the original image     
    that has been modified using edge detection. 
 
    >>> image = load_image(choose_file())     
    >>> filtered = detect_edges(image, 10.0)     
    >>> show(filtered)     
    """
    new_image = copy(image)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            r1, g1, b1 = get_color(image, x, y)
            r2, g2, b2 = get_color(image, x, y + 1)
            ta = (r1 + g1 + b1)/ 3
            tb = (r2 + g2 + b2)/ 3
            
            if(abs(ta - tb) < threshold):
                color = create_color(255,255,255)
            else:
                color = create_color(0,0,0)
            set_color(new_image,x,y,color)
    return new_image
        

def detect_edges_better(image, threshold):     
    """ (Cimpl.Image, float) -> Cimpl.Image      
   Return a new image that contains a copy of the original image     
   that has been modified using edge detection.   
   
   >>> image = load_image(choose_file())     
   >>> filtered = detect_edges_better(image, 10.0)     
   >>> show(filtered)     
  
   """ 
    new_image = copy(image)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            r1, g1, b1 = get_color(image, x, y)
            r2, g2, b2 = get_color(image, x, y + 1)
            r3, g3, b3 = get_color(image, x + 1, y)
            ta = (r1 + g1 + b1)/ 3
            tb = (r2 + g2 + b2)/ 3
            tc = (r3 + g3 + b3)/ 3
            
            if((abs(ta - tb) < threshold) & (abs(ta - tc) < threshold)):
                color = create_color(255,255,255)
            else:
                color = create_color(0,0,0)
            set_color(new_image,x,y,color)
    return new_image


def blur(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of image.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(blurred)    
    """  
    target = copy(image)
    
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            rn1, gn1, bn1 = get_color(image, x - 1, y - 1)
            rn2, gn2, bn2 = get_color(image, x - 1, y + 1)
            rn3, gn3, bn3 = get_color(image, x + 1, y - 1)
            rn4, gn4, bn4 = get_color(image, x + 1, y + 1)
            center_red, center_green, center_blue = get_color(image, x, y)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + rn1 + rn2 + rn3 + rn4) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                                   right_green + center_green + gn1 + gn2 + gn3 + gn4) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                                   right_blue + center_blue + bn1 + bn2 + bn3 + bn4) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target


def scatter(image):
    """ (Cimpl.image) -> Cimpl.image
    
    Return a new image that looks like a copy of an image in which the pixels
    have been randomly scattered. 
    
    >>> original = load_image(choose_file())
    >>> scattered = scatter(original)
    >>> show(scattered)    
    """
    # Create an image that is a copy of the original.
    
    new_image = copy(image)
    
    # Visit all the pixels in new_image.
    
    for x,y,(r,g,b) in image:
        
        # Generate the row and column coordinates of a random pixel
        # in the original image. Repeat this step if either coordinate
        # is out of bounds.
        
        row_and_column_are_in_bounds = False
        while not row_and_column_are_in_bounds:
            
            # Generate two random numbers between -10 and 10, inclusive.
            
            rand1 = random.randint(-10,10)
            rand2 = random.randint(-10,10) 
            
            # Calculate the column and row coordinates of a
            # randomly-selected pixel in image.

            random_column = (x + rand1)
            random_row = (y + rand2)  
            
            # Determine if the random coordinates are in bounds.

            if random_column in range(get_width(image)) and random_row in range(get_height(image)):
                row_and_column_are_in_bounds = True
                    
        # Get the color of the randomly-selected pixel.
        
        col = get_color(image, random_column, random_row)
        
        # Use that color to replace the color of the pixel we're visiting.
        
        set_color(new_image, x, y, col)
                    
    # Return the scattered image.
    return new_image