#write a function that converts number to roman numerals
# function mySample(298) --> CCXCVIII

x=298
x=str(x)
print(len(x))
print(x[0])

def roman_numeral_converter(num):
    num=str(num)
    length_of_num = len(num)
    f=num[1] + length_of_num
    digitValue=[1000,900,600,500,400,100,90,60,50,40,11,10,9,8,7,6,5,4,3,2,1]

    romanDict={
        1000 : "M",
        900 : "CM",
        600 : "DC",
        500: "D",
        400 : "CD",
        100 : "C",
        90 : "XC",
        60 : "LX",
        50 : "L",
        40 : "XL",
        11 : "XI",
        10 : "X",
        9 : "IX",
        8 : "VIII",
        7 : "VII",
        6 : "VI",
        5 : "V",
        4 : "IV",
        3 : "III",
        2 : "II",
        1 : "I"
    }







