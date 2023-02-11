
def int_to_roman(number):
    global roman
    roman = ''
    for letter, value in roman_numbers.items():
        while number >= value:
            roman += letter
            number -= value
    


    
 
def roman_to_int():
    print('Введите число: ')
    roman=input()
    global result
    result = 0
    for i, c in enumerate(roman):
        if i+1<len(roman) and integers[roman[i]] < integers[roman[i+1]]:
            result-=integers[roman[i]]
        else:
            result+=integers[roman[i]]
    return str(result)
print('Напишите 1, для запуска программы по переводу арабских цифр в римские,\n или 2, для запуска программы по переводу римских цифр в арабские')
a=int(input())
if a==1:
    roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    roman=0
    number=int(input())
    
    int_to_roman(number)
    print(roman)
elif a==2:
    integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    roman_to_int()
    
    print(result)

