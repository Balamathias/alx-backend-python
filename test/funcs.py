"""DO some random stuffs right here."""


from typing import Union


def fibonnacci(num: Union[int, str]) -> int:
    if type(num) == str and not num.isnumeric():
        raise TypeError('Value must be a number')
    if int(num) == 0:
        raise ValueError('num cannot be zero')
    
    return 1 if (int(num) == 1) else int(num) + fibonnacci((int(num) - 1))
                                                           

a = 1

if a == 1: print(a + 1)
else: print(3)
