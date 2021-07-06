from math import sqrt, pi

print("Welcome to your Shape Calculator!")

asking_for_input = True
while asking_for_input:
    inp = input("Up to what place do you want pi to be rounded? ")
    if inp.lower() == "exit":
        exit()
    else:
        try: 
            math_pi = round(pi, int(inp))
            asking_for_input = False 
            break
        except:
            print("Please enter a number.")

def user_setup(): 
    answer = input("What would you like to calculate? (2D, 3D, exit) ").lower()
    if answer == "2d":
        answer1 = input("What would you like to do? (area, perimeter) ").lower()
        if answer1 == 'area':
            area_2D()
        elif answer1 == 'perimeter':
            perimeter_2D()  
    
    elif answer == "3d":
        answer1 = input("What would you like to do? (volume, surface area) ").lower()
        if answer1 == 'volume':
            volume_3D()
        elif answer1 == 'surface area':
            surface_area_3D()
    elif answer == "exit":
        exit()
    else:
        print ("We didn't get that. Please try again.")
        exit()

def area_2D():
    area_of_shape = 0
    answer = input("Which shape would you like to find the area of? ").lower() 
    if answer == "triangle":
        base = float(input("Input Base: "))
        height= float(input("Input Height: "))
        area_of_shape = ((base*height)/2)

    elif answer == "circle":
        radius = float(input("Input Radius: "))
        area_of_shape = (math_pi*radius**2)

    elif answer == "rectangle":
        length = float(input("Input Length: "))
        width = float(input("Input Width: "))
        area_of_shape = (length*width)

    elif answer == "square":
        side = float(input("Input The Dimension Of One Side: "))
        area_of_shape = (side**2)

    elif answer == "trapezoid":
        base1 = float(input("Input Base 1: "))
        base2 = float(input("Input Base 2: "))
        height = float(input("Input Height: "))
        area_of_shape = (((base1+base2)/2)*height)

    elif answer == "parallelogram":
        base = float(input("Input Base: "))
        height = float(input("Input Height: "))
        area_of_shape = (base*height)

    elif answer == "Try Again":
        user_setup()
    else:
        print ("We didn't get that. Please try again.")
        exit()        
    unit_of_measurement = input("What is the unit of measurement? ")
    print(f"The area is {str(area_of_shape)}{unit_of_measurement}^2")  

    try_again = input("Would you like to use the Shape Calculator again? (yes or no) ").lower()
    if try_again == "yes":
        user_setup()
    if try_again == "no":
        exit()


def perimeter_2D(): 
    perimeter_of_shape = 0 
    answer = input("Is the shape regular or irregular? ").lower()
    regular_shapes = {"triangle":3, "square":4, "pentagon":5, "hexagon": 6, "heptagon":7, "octagon":8, "nonagon": 9, "decagon": 10, "dodecagon":12}
    if answer == "regular":
        inp = input("What shape: ").lower()
        if inp != "circle":
            dimension = float(input("What is the dimension of the shape: "))
            perimeter_of_shape = regular_shapes[inp] * dimension

        if inp == "circle":
            radius = float(input("Input Radius: "))
            perimeter_of_shape = (2*math_pi*radius)

    if answer == "irregular":
        shape = input("What shape are you trying to find the perimeter of? ").lower() 
        irregular_shapes = {"triangle":3, "parallelogram":4, "trapezoid":4, "pentagon":5, "hexagon":6, "heptagon":7, "octagon":8, "nonagon": 9, "decagon": 10, "dodecagon":12} 
        if shape == "rectangle":
            length = float(input("Input Length: "))
            width = float(input("Input Width: "))
            perimeter_of_shape = (2*length + 2*width)            
        elif shape != "rectangle":

            try:
                sides = int(irregular_shapes[shape])
            except:

                print("Isn't a valid shape.")
                exit()
            for i in range(sides):
                dimension = float(input(f"Side #{i+1}: ")) 
                perimeter_of_shape += dimension
        else: 
            print ("We didn't get that. Please try again.")
            exit()
    unit_of_measurement = input("What is the unit of measurement? ")
    print(f"The perimeter is {str(perimeter_of_shape)}{unit_of_measurement}")    
    try_again = input("Would you like to use the Shape Calculator again? (yes or no) ").lower()
    if try_again == "yes":
        user_setup()
    if try_again == "no":
        exit()   

def volume_3D():
    volume_of_shape = 0
    answer = input("Is this shape a prism, pyramid, cone, sphere? ").lower()
    if answer == "prism":
        prism = input("What prism? ")
        if prism == "cube":
            side = float(input("What is demnsion of 1 side? "))
            volume_of_shape = (side**3)

        elif prism == "rectangular prism" or prism == "cuboid":
            length = float(input("What is demension of the length? "))
            width = float(input("What is demension of the width? "))
            height = float(input("What is demension of the height? "))
            volume_of_shape = (length*width*height)      

        elif prism == "triangular prism":
            base = float(input("Dimension of base of triangle: "))
            triangle_height = float(input("Dimension of height of triangle: "))
            height = float(input("Dimension of height of prism"))
            volume_of_shape = (((base*triangle_height)/2)*height)  

        elif prism == "cylinder":
            radius = float(input("Input Radius: "))
            height = float(input("Input Height Of Cylinder: "))
            volume_of_shape = ((math_pi*radius**2) * height)
        else: 
            print ("We didn't get that. Please try again.")
            exit()

    elif answer == "pyramid":
        pyramid = input("What pyramid? ")
        if pyramid == "square based pyramid":
            base_side = float(input("Dimension of one side of the base? "))
            height = float(input("Dimension of height of pyramid: "))
            volume_of_shape = ((base_side**2)*(height/3))

        elif pyramid == "triangular based pyramid":
            base_triangle_base = float(input("Dimension of the base in the base triangle: ")) 
            base_triangle_height = float(input("Dimension of the base in the base triangle: "))
            height = float(input("Height of the pyramid: "))
            volume_of_shape = (((base_triangle_base*base_triangle_height)/2)*height/3)

        else: 
            area_of_base = float(input("What is the area of the base of the pyramid? "))
            height = float(input("Height of the pyramid: "))
            volume_of_shape = ((area_of_base*height)/3)
    
    elif answer == "cone":
        radius = float(input("What is the radius of the cone? "))
        height = float(input("What is the height of the cone? "))    
        volume_of_shape = (math_pi*(radius**2)*(height/3))

    elif answer == "sphere":
        radius = float(input("What is the radius of the sphere? "))     
        volume_of_shape = ((4/3)*math_pi*radius**3) 
    
    else:
        print ("We didn't get that. Please try again.")
        exit()

    unit_of_measurement = input("What is the unit of measurement? ")
    print(f"The volume is {str(volume_of_shape)}{unit_of_measurement}^3")  
    try_again = input("Would you like to use the Shape Calculator again? (yes or no) ").lower()
    if try_again == "yes":
        user_setup()
    if try_again == "no":
        exit()   


def surface_area_3D():
    surface_area_of_shape = 0
    answer = input("Is this shape a prism, pyramid, cone, sphere? ").lower()
    if answer == "prism":
        prism = input("What prism? ").lower()
        if prism == "cube":
            side = float(input("What is demnsion of 1 side? "))
            surface_area_of_shape = (6*(side**2))

        elif prism == "rectangular prism" or prism == "cuboid":
            length = float(input("What is dimension of the length? "))
            width = float(input("What is dimension of the width? "))
            height = float(input("What is dimension of the height? "))
            surface_area_of_shape = (2*(width*length+height*length+height*width))  

        if prism == "triangular prism": 
            base_side1 = float(input("Side 1 of triangle base of triangular prism: "))
            base_side2 = float(input("Side 2 of triangle base of triangular prism: "))
            base_side3 = float(input("Side 3 of base of triangular prism: "))
            triangle_height = float(input("Input Dimension of height of triangle: "))
            height = float(input("Input Dimension of height of 5hw triangular prism: "))
            surface_area_of_shape = ((base_side3*triangle_height)+(base_side1+base_side2+base_side3)*height)      

        elif prism == "cylinder":
            try:
                radius = float(input("Input Radius: "))
                height = float(input("Input Height Of Cylinder: "))
                surface_area_of_shape = (2*math_pi*radius*height+2*math_pi*radius**2)
            except:
                print("We couldn't quite catch that. Please try again!")
                exit()

    elif answer == "cone":
        radius = float(input("What is the radius of the cone? "))
        slant_height = input("What is the slant height of the cone?")      
        surface_area_of_shape = (math_pi*radius**2+math_pi*radius*slant_height)

    elif answer == "sphere":
        radius = float(input("What is the radius of the sphere? "))    
        surface_area_of_shape = (4*math_pi*radius**2) 
  
    elif answer == "pyramid":
        pyramid = input("What pyramid? ")
        if pyramid == "square based pyramid":
            base_side = float(input("Dimension of one side of the base? "))
            height = float(input("Dimension of height of pyramid: "))
            surface_area_of_shape = (base_side**2+2*side*(sqrt((base_side**2)/4+(height**2))))

        if pyramid == "triangular based pyramid":
            base_triangle_base = float(input("Dimension of the base in the base triangle: ")) 
            base_triangle_height = float(input("Dimension of the base in the base triangle: "))
            height = float(input("Height of the pyramid: "))
            surface_area_of_shape = (((base_triangle_base*base_triangle_height)/2)*height/3) 
    else:
        print ("We didn't get that. Please try again.")
        exit()

    unit_of_measurement = input("What is the unit of measurement? ")
    print(str(surface_area_of_shape) + unit_of_measurement + "^2")
    print(f"The surface area is {str(surface_area_of_shape)}{unit_of_measurement}^2") 
    try_again = input("Would you like to use the Shape Calculator again? (yes or no) ").lower()
    if try_again == "yes":
        user_setup()
    if try_again == "no":
        exit()   

if __name__ == "__main__":
    user_setup()