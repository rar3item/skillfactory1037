ticket_value = int(input("Введите необходимое количество билетов "))
count = 0
ticket_less18, ticket_18_25, ticket_more25 = [], [], [] #списки для обработки стоимости
while count < ticket_value:
    age = int(input("Введите возраст посетителя "))
    if age < 18:
        ticket_less18.append(0)
    elif 18 <= age <= 25:
        ticket_18_25.append(990)
    else:
        ticket_more25.append(1390)
    count += 1
result = sum(ticket_18_25) + sum(ticket_more25) #общая стоимость билетов
if ticket_value >= 3:
    print("Вы приобрели " + str(ticket_value) + " билетов," + " стоимость составляет " + str((result * 0.9)) + " руб")
else:
    print("Вы приобрели " + str(ticket_value) + " билетов," + " стоимость составляет " + str(result) + " руб")
