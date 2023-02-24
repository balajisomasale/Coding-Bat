Warmup-1 > not_string
prev  |  next  |  chance
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

Sol : 

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3 
  
  
or 

def not_string(str):
  if "not" in str:
    return str
  else:
    return "not "+str
