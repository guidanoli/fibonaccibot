
""" Commas module """

""" 
This module is responsible for converting NC and num
back and forth.

NC (short for Number with Commas) is a string s such that
nwc2num(num2nwc(s)) == s is true.
Objectively speaking, it is a string that represents
a number (int) with comma separators every 3th number
Example:
12345678 (number) --> '12,345,678' (nc)
'000,000,000' (nc) --> 0 (number)
'0' (nc) --> 0 (number)
"""

def nwc2num(x: str) -> int:
  """ Converts NumComma to Number """
  return int(x.replace(',',''))

def num2nwc(x: int) -> str:
  """ Convers Number to NumComma """
  return "{:,}".format(int(x))
