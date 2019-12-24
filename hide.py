from PIL import Image

def message2bin(input_message):
    # stores each letter as an ascii representation in a list
    message = list(map(ord, list(input_message))) 
    
    # convert the ascii data to binary
    bin_message = ['{:08b}'.format(i) for i in message]

    return ''.join(bin_message) # returns the converted string to binary

def num_modifier(num, option):
    # for even numbers
    if option == '0':
        return num if num%2 == 0 else num-1
    
    # for odd numbers
    elif option == '1':
        return num if num%2 != 0 else num-1

# convert an unpacked list filled with rgb data into
# an object that can be saved with PIL
def convertion(color_data): 
    # 75//3 = 25 ; width*heigth*3//3, so essentially just width*height lol
    l = []
    multip = 0
    for i in range(len(color_data)//3):
        rgb = (color_data[multip], color_data[multip+1], color_data[multip+2])
        l.append(rgb)
        multip += 3

    return l

def hide(filename, message):
    img = Image.open(filename)
    stream = []     
    new_data = []

    # unpacking the data to a single list
    for pixel_value in list(img.getdata()):
        for color_value in pixel_value: 
            # stores the unpacked rgb values on each pixels
            stream.append(color_value)

    # hiding
    count = 0
    for i in stream:
        # if there's no data left to hide then 
        # put the rest of the raw_data into new_data
        if count >= len(message):
            new_data = new_data+stream[count:]
            break
        else:
            new_data.append(num_modifier(i, message[count]))

        count += 1

    img.putdata(convertion(new_data))
    img.save('encrypted.png')
    img.close()

delimiter = '1111111111111110' # 2 bytes/16 bits
raw_data = message2bin('batman')+delimiter # batman

hide('untitled.png', raw_data)







