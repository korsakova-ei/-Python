salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
# Инициализируем переменную для подушки безопасности
total_needed = 0

for month in range(months):
    # Рассчитываем дефицит для текущего месяца
    deficit = spend - salary
    if deficit > 0:
        total_needed += deficit

    # Увеличиваем расходы на 5% для следующего месяца
    spend *= (1 + increase)

# Округляем до целого числа
total_needed = round(total_needed)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {total_needed}")



