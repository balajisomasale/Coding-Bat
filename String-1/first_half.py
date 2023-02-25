String-1 > first_half
prev  |  next  |  chance
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'


Sol : 
  
  def first_half(str):
  return str[:len(str)/2]
