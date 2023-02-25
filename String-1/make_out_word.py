String-1 > make_out_word
prev  |  next  |  chance
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'

Sol : 

def make_out_word(out, word):
  d=out[:2]
  e=out[2:]
  return d+word+e
