def swap_case(s):
    string_swap = s.swapcase()
    return string_swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)