
def read_number(n):
    one_nine = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
               6: 'six', 7:'seven', 8: 'eight', 9: 'nine'}
    ten_nineteen = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
                    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 
                    19: 'nineteen'}
    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
            8: 'eighty', 9: 'ninety'}
    
    thousand_unit, remainder = divmod(n, 1000)
    hundred_unit, remainder = divmod(remainder, 100)
    ten_unit, remainder = divmod(remainder, 10)
    one_unit = remainder
    
    reading = ""
    if thousand_unit != 0:
        reading += one_nine[thousand_unit] + " thousand "
    if hundred_unit != 0 and (ten_unit != 0 or one_unit != 0):
        reading += one_nine[hundred_unit] + " hundred and "
    elif hundred_unit != 0:
        reading += one_nine[hundred_unit] + " hundred "
    if ten_unit >= 2:
        reading += tens[ten_unit] + ' '
    if ten_unit == 1:
        number = int(str(ten_unit) + str(one_unit))
        reading += ten_nineteen[number]
    elif one_unit != 0:
        reading += one_nine[one_unit]
    return reading

def reading_length(n):
    reading = read_number(n)
    a = reading.split()
    reading_length = 0
    for i in a:
        reading_length += len(i)
    return reading_length

def total_length(t):
    total_length = 0
    for i in range(1, t+1):    
        total_length += reading_length(i)
    return total_length


print total_length(1000)


        
    
    

    


