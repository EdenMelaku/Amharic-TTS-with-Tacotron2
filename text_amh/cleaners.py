

from .Amh_cleaner import Cleaner


def amharic_cleaners(text):
  '''Pipeline for amharic  text, including number and abbreviation expansion.'''
  clr = Cleaner(text)
  text= clr.clean()

  return text
