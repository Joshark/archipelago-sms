def extract_bits(input_byte, input_offset):
    byte_list = []
    temp = str(bin(input_byte))
    for x in range(0, len(temp)):
        print(temp[x])
        if temp[x] == "1":
            byte_list.append((input_offset * 8) + int(x))
    return byte_list
