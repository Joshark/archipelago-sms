def extract_bits(input_byte, input_offset):
    byte_list = []
    temp = str(bin(input_byte))
    temp = str.removeprefix(temp, "0b")
    for x in range(0, len(temp)):
        if temp[x] == "1":
            byte_list.append((input_offset * 8) + int(x))
    return byte_list


def change_endian(byte):
    byte = byte.to_bytes(2, "big")
    return int.from_bytes(byte)
