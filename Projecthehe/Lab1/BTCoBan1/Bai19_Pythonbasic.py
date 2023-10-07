#19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
def chuoimoi(text):
  if len(text) >= 2 and text [:2] == "Is":
    return text
  return "Is" + text
print(chuoimoi("Array"))
print(chuoimoi("IsEmpty")) 
