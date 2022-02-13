if __name__ == "__main__":
    print("bit string start from 0 and |= operator")
    bit_string: int = 0
    print(f"initialization: {bin(bit_string)}")
    bit_string <<= 2
    print(f"shift         : {bin(bit_string)}")
    bit_string |= 0b00
    print(f"or operation  : {bin(bit_string)}")
    print()
    
    # | 연산을 해야 값들이 보존됨
    print("bit string start from 1 and |= operator")
    bit_string: int = 1
    print(f"initialization: {bin(bit_string)}")
    bit_string <<= 2
    print(f"shift         : {bin(bit_string)}")
    bit_string |= 0b00
    print(f"or operation  : {bin(bit_string)}")
    print()

    print("bit string start from 1 and &= operator")
    bit_string: int = 1
    print(f"initialization: {bin(bit_string)}")
    bit_string <<= 2
    print(f"shift         : {bin(bit_string)}")
    bit_string &= 0b00
    print(f"or operation  : {bin(bit_string)}")
    print()