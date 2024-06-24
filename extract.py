"""
Program to extract useful data from a raw data stream obtained from a sensor.
The data from the sensor contains a block with the format: 
... BEGIN temp_press:Xcoordinate,Ycoordinate emanetiS END .. 
Ntobeko Mhlongo
02 April 2024
"""

def get_block(data):
    # Slicing out the block of data from the given input
    block_start = data.find("BEGIN")
    block_end = data.find("END")
    block_function = data[block_start : block_end + 3]
    return block_function

def location(block, block_end, space):# Passing variables block_end and space to the function to be able to use them in this part of code
    # Slicing out location form the data
    location_function = block[space : block_end - 1]
    location_function = location_function[::-1].title() # Writing the location in reverse and capitilizing the first letter of each word
    return location_function
    
def pressure(block, underscore, collon):# Passing variables underscore and collon to the function to be able to use them in this part of code
    # Slicing out pressure from the data
    pressure_function = block[underscore + 1 : collon]
    pressure_function = float(pressure_function)# Converting the pressure to a float
    return pressure_function

def temperature(block):
    # Slicing out temperature from the block 
    underscore = block.find("_")
    temperature_function = block[6 : underscore]
    temperature_function = float(temperature_function) # Convertin temperature to a float
    return temperature_function
    
def y_coordinate(block, collon, comma): # Passing collon and comma to the fuction to be able to use them in this part of code
    # Slicing out the y coordinate from the data
    space = block.find(" ", collon)
    y_function = block[comma + 1 : space]
    return y_function

def x_coordinate(block):
    # Slicing out the x cooordinate from the data
    collon = block.find(":")
    comma = block.find(",")
    x_function = block[collon + 1 : comma]
    return x_function
    

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    collon = block.find(":")
    comma = block.find(",")
    underscore = block.find("_")
    block_end = block.find("END")
    space = block.find(" ", comma) + 1
    print('Site information:')
    print('Location:', location(block, block_end, space))
    print('Coordinates:', y_coordinate(block, collon, comma), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block, underscore, collon)))

if __name__=='__main__':
    main()

