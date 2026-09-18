def extract_bits(input_byte, input_offset):
    bit_list = []
    temp = get_bitflag(input_byte)

    for x in range(0, len(temp)):
        if temp[x] == "1":
            bit_list.append(((input_offset + 1) * 8) - int(x+1))

    return bit_list


def get_bitflag(input_byte):
    input_byte = change_endian(input_byte)
    temp = str(bin(input_byte))
    temp = str.removeprefix(temp, "0b")
    while len(temp) < 8:
        temp = "0" + temp
    return temp


def bit_flagger(input_byte, flag_position, bool_setting):
    if bool_setting:
        bool_char = 1
    else:
        bool_char = 0
    return input_byte | (bool_char << flag_position)


def change_endian(byte):
    byte = int(byte)
    byte = byte.to_bytes(2, "big")
    return int.from_bytes(byte, "big")
