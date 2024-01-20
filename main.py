def number_to_word(number: int):
    
    units = ['یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه']
    tens = ['ده', 'بیست', 'سی', 'چهل', 'پنجاه', 'شصت', 'هفتاد', 'هشتاد', 'نود']
    hundreds = ['صد', 'دویست', 'سیصد', 'چهارصد', 'پانصد', 'ششصد', 'هفتصد', 'هشتصد', 'نهصد']
    digits = len(str(number))
    array = [int(x) for x in str(number)]
    string = ""
    for i in range(digits):
        if(i <= 2):
            string += str(array[i])
        elif(i <= 5):
            pass
    return string


print(number_to_word(12345))
