import pulp

# Створення моделі
model = pulp.LpProblem("Максимізація_виробництва_напоїв", pulp.LpMaximize)

# Задамо змінні
x1 = pulp.LpVariable("Лимонад", lowBound=0,
                     cat='Integer')  # Кількість лимонаду
x2 = pulp.LpVariable("Фруктовий_сік", lowBound=0,
                     cat='Integer')  # Кількість фруктового соку

# Цільова функція (Максимізація кількості вироблених продуктів)
model += x1 + x2

# Обмеження води - Лимонад - 2 од., сік - 1 од.
model += 2 * x1 + 1 * x2 <= 100, "Обмеження_води"
# Обмеження цукру - Лимонад - 1 од.
model += 1 * x1 <= 50, "Обмеження_цукру"
# Обмеження лимонного соку - Лимонад - 1 од.
model += 1 * x1 <= 30, "Обмеження_лимонного_соку"
# Обмеження фруктового пюре - Сік - 2 од.
model += 2 * x2 <= 40, "Обмеження_фруктового_пюре"

model.solve()

print("Результати оптимізації:")
print(f"Кількість лимонаду: {x1.varValue}")
print(f"Кількість фруктового соку: {x2.varValue}")