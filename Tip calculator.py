print("welcome to the Tip calculator")
bill = float(input("what is the total bill? $"))
tip_percentage = float(input("what percentage would you like to give? 10, 12, 15?"))
collegues_count = input("how many people split to bill?")
bill_percentage = (int(bill) / 100) * tip_percentage
bill_plus_percentage = bill + bill_percentage
personal_pay = bill_plus_percentage / float(collegues_count)
personal_pay_round = round(personal_pay, 2)
final_amount = "{:.2f}".format(personal_pay_round)
print(f"each person should pay ${final_amount}")
# თუ ვერ ვამრგვალებთ ციფრს მითითებული ციფრების რაოდენობით, მაშინ არის ერთი ფუნქცია, რომელიც დაგვიმრგვალებს რიცხვს წინასწარ განსაზღვრულ ციფრების რაოდენობაზე რომელსაც ვუთითებთ წერტილის შემდგომ. personal_pay_round = "{:.2f}".format