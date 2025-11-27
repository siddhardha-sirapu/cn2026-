def character_stuffing(data, flag='F', escape='E'):
    stuffed_data = "" 
    for char in data:
        if char == flag or char == escape:
            stuffed_data += escape + char
        else:
            stuffed_data += char    
    return flag + stuffed_data + flag

data = "HelloF, Eworld!"
stuffed_data = character_stuffing(data)
print("Original data:", data)
print("Stuffed data:", stuffed_data)
