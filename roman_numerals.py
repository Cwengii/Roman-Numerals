
def to_roman_numeral(number):

    value = [1000, 500, 100, 50, 10, 5, 1]
    symbol = ["M", "D", "C", "L", "X", "V", "I"]

    roman_number = " "   
    i = 0
 
    # while number > 0:
    for i in range(len(symbol)):
        while number >= number[i]:
            roman_number += symbol[i]
        number -= value[i]  
    # if value[i] <= number:
        
    # else:
    #     i += 1
        
    return roman_number
print(to_roman_numeral(8))