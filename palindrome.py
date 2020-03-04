def func(x):
  return x[::-1]
  
string = "0110"
rev = func(string)

if string == rev :
   print("True")
   
else :
   print("False")