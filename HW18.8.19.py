sum_tickets = 0
your_tickets = int(input("Сколько Вам необходимо билетов? - \n"))
for age in range(your_tickets):
    age = int(input("Какой возраст посетителя? - \n"))
    if age < 18:
        sum_tickets += 0
    elif 18 <= age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
print("Стоимость Ваших билетов:", "%.2f" % sum_tickets, "руб.")
if your_tickets > 3:
    discount = sum_tickets / 100 * 10
    print("Скидка составляет:", "%.2f" % discount, "руб.")
    print("К оплате с учетом скидки:", "%.2f" % (sum_tickets - discount), "руб.")
