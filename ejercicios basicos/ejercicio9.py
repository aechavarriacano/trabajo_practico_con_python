from datetime import datetime
birthdate = (input("enter your date of birth AAAA-MM-DD: "))
#fecha_nacimiento = "1988-05-24"
today = str(datetime.today().strftime('%Y-%m-%d'))
d1 = datetime.strptime(birthdate, "%Y-%m-%d")
d2 = datetime.strptime(today, "%Y-%m-%d")
print("date of birth: ", d1, " today: ", d2)
print("quantity of months: ", abs((d1.year - d2.year) * 12 + d1.month - d2.month))


