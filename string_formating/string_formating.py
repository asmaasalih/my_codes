def print_formatted(number):
    # your code goes here
    w = len(str(bin(number))[2:]) +1
    for n in range(1,number+1):
        
        oct_n = str(oct(n))[2:]
        w_o = len(oct_n)
        hex_n = str(hex(n))[2:].upper()
        w_h = len(hex_n)
        bin_n = str(bin(n))[2:]
        w_b = len(bin_n)
        n = str(n)
        w_n = len(n)
        
        print(" " * (w - w_n -1) + n + " " * (w - w_o) + oct_n + " " * (w - w_h) + hex_n + " " *(w - w_b) + bin_n)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)