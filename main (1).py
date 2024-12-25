from random import randint
number_guess = randint(1 , 10)
attempts = 3
while attempts > 0:
    us_numb = int (input("Введите число от 1 до 10: "))
    if us_numb == number_guess:
        print ("Победа")
        break
    else:
        attempts = attempts - 1
        print ("Ошибка")
