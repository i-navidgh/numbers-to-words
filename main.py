from num2words import num2words

def number_to_word(number: int):
    return num2words(number, lang="fa")


print(number_to_word(12345))
