money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month_to_live = 1
while money_capital >= spend:
    money_capital += salary
    money_capital -= spend
    spend *= 1 + increase
    month_to_live += 1
print("Количество месяцев, которое можно протянуть без долгов:", month_to_live)
