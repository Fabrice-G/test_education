input_string = input ('Enter the string: ')
print(input_string[0:-2])

def undersorer (): 
   input_string1 = input ('Enter the string: ')
   out1= '_'
   out2= ""
   for chr in input_string1:
       out2 += chr + out1
   print (out2)
        
undersorer()  

def remove(string):
    return string.replace(" ", "")
 
 
# Driver Program
string = ' g e e k '
print(remove(string))