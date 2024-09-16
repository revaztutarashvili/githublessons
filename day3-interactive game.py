# # ___________________________rollerskate__________________________________
print("welcome to the rollerskate")
height = int(input("what is your height?"))
age = int(input("what is your age?"))
if height >= 120:
    # print("you can ride")
    if age < 12:
        print("please pay 5$")
    elif age <= 15:
        print("please pay 7$")
    elif age <= 17:
        print("please pay 9$")
    else:
        print("please pay 12$")
    print("Now you can ride")
else:
    print("Sorry, you have to grow taller before you can ride")
# # ___________________________rollerskate__________________________________


# # #     # > greater then  
# # #     # < less then   
# # #     # >= greater then or equal to  
# # #     # >=less yhen or equal to
# # #     # == equal to (ამ შემთხვევაში ვუთითებთ რომ იმენნო ეს რაოდენობა უნდა იყოს რომ დაბეჭდოს თანხმობა სრიალზე, სხვა შემთხვევაში(119, 121) დაბეჭდავს else-თვის მინიჭებულ მნიშვნელობას.
# # #     # != not equal to
          # if / elif /else    elif-ს მათ შორის აქვს განსაკუთრებული ფუნქცია, კერძოდ შეგვიძლია შეუზღუდავი რაოდენიბით გამოვიყენოთ if და else-ს შორის, რათა გვქონდეს სხვადასხვა ოფშენი.


# # # __________________________________ODD or EVEN ________________________________________________________
input_num = int(input("let's check out number is odd even. please type number to check"))
example = input_num % 2 
if example == 1:
    print("your number is odd")
else:
    print("your number is even")
# # # _________________________________________________________________________________________________________





# __________________________________BMI Calculator 2.0__________________________________




# __________________________________BMI Calculator 2.0__________________________________