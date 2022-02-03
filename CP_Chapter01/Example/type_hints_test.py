from typing import Dict


if __name__ == "__main__":
    dict_var01: Dict[str, str] = {'name', '12345678'}
    # error < python 3.9
    # Type Hinting Generics in Standard Collections
    # https://docs.python.org/3.9/whatsnew/3.9.html
    # dict_var02: dict[str, str] = {'name', '12345678'}
    dict_var02: dict = {'name', '12345678'}

    print(dict_var01)
    print(dict_var02)
