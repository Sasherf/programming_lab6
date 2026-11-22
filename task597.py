arabic_to_roman = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

number = int(input("Enter a number: "))

roman_num = ""
for num in arabic_to_roman:
    while number - num >= 0:
        number -= num
        roman_num += arabic_to_roman[num]

print(roman_num)