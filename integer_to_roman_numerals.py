# Write program that converts the given number (between 1 and 3999) to the roman numerals. 
# The program should convert only from numbers to Roman numerals, not vice versa and during the conversion 
# following notes should be taken into consideration.
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# When finding roman equivalent of the integer, we check the number to find the largest number which is bigger than 1000 in the integer.
# Because the largest Roman number is 1000.

print (''' This program converts decimal numbers to Roman Numerals ''')
print ('To exit the program, please type "exit"')

def convert_romans(n):
    num_list = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    romans = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
    i = 12  
    roman_numeral = ''
    while n != 0:
        if num_list[i] <= n:    
            roman_numeral += romans[i] 
            n = n - num_list[i]
        else:
            i -= 1 
    return roman_numeral
     

while True:
    n= input(" Please enter a number between 1 and 3999, inclusively : ")
    if n=="exit":
        print("Exiting the program... Good Bye")
        break
    elif n.isdecimal()==False or int(n)<= 0 or int(n) >= 3999:
        print("Not Valid Input !!!")
        print("Please enter a valid digit")
    else:
        n=int(n)
        print(convert_romans(n))   
        break    