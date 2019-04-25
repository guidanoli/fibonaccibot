
""" Comments module """

"""
This module is resposible for generating the comment
string for a given iteration.
"""

from mngSettings import getSetting

USE_COMMAS = getSetting("commas") == "true"
ALPHABET = [ chr(i) for i in range(ord('a'),ord('z')+1) ] + [ ' ' ]
ALPHABET_SIZE = len(ALPHABET)

def cvt(n: int) -> str:
  if USE_COMMAS:
    from commas import num2nwc
    return num2nwc(n)
  else:
    return str(n)

def intro(n: int) -> str:
  return "Some facts about F({}):".format(cvt(n))

def number_size(fn: int) -> int:
  size = len(str(fn))
  return size

def sum_of_digits(fn: int) -> int:
  sfn = str(fn)
  dsum = 0
  for c in sfn:
    dsum += int(c)
  return dsum

def digits(fn: int) -> str:
  sd = sum_of_digits(fn)
  ns = number_size(fn)
  ratio = sd/ns
  format_str = "Contains {} digits that add up to {}."
  format_str += "\nThus, its average digit is {}."
  return format_str.format(cvt(ns), cvt(sd), ratio)

def recFunc(num: int) -> str:
  if num < ALPHABET_SIZE:
    return ALPHABET[num]
  else:
    return recFunc(num//ALPHABET_SIZE) + ALPHABET[num%ALPHABET_SIZE]

def num2words(fn: int) -> str:
  return "Can be written in base 28 as... \"" + recFunc(fn) + "\"."

def getComment(n: int, fn: int) -> str:
  lines = [
    intro(n) ,
    num2words(fn) ,
    digits(fn) ,
  ]
  return "\n".join(lines)
