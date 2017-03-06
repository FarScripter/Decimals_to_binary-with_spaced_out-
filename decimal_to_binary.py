def get_converted_bin(u_i, adding):
    b_number = bin(int(u_i))[2:]
    length = len(b_number)
    # check if the length of binary number == 4 * n
    if length % 4 == 0:
        length -= 1

    # calculating the maximum char amount in our bin number
    # for example:
    # 12 in decimal = 1100 in binary
    # the length of binary is 4
    # and maximum char amount is 4
    # -----------------------------
    # 19 in decimal = 1 0011 in binary
    # the length of binary is 5     (1 0011)
    # and maximum char amount is 8  (0001 0011)
    max_char = (length - length % 4 - 4 * (length // 4 - 1)) * (length // 4) + 4
    iterations = max_char // 4
    out = ''

    # for each 4 symbols in out binary number we should add a space
    # for example:
    # if our binary is 00010011
    # we should make it like 0001 0001
    for i in range(0, iterations):
        result = b_number.rjust(max_char, '0')
        result = result[i * 4:i*4 + 4]
        out += result + adding

    return out.rstrip()


def main():
    user_input = input('Enter decimal number: \n')

    print('Answer with spaces: ')
    print(str(user_input) + ' in decimal = ' + get_converted_bin(user_input, ' ') + ' in binary\n')
    print('Answer without spaces: ')
    print(str(user_input) + ' in decimal = ' + get_converted_bin(user_input, '') + ' in binary\n')
    print('bin() function result: ')
    print(str(user_input) + ' in decimal = ' + bin(int(user_input)) + ' in binary\n')

if __name__ == '__main__':
    main()