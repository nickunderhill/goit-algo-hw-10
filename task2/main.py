import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування


def f(x):
    return 5 - x ** 2


def draw_chart(lower, upper):
    # Створення діапазону значень для x
    range = np.linspace(lower, upper, 500)
    x = f(range)
    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(range, x, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(lower, upper)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([range[0], range[-1]])
    ax.set_ylim([0, max(x) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=lower, color='gray', linestyle='--')
    ax.axvline(x=upper, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = 5 - x^2 від ' +
                 str(lower) + ' до ' + str(upper))
    plt.grid()
    plt.show()


def monte_carlo(func, low, high, y_min_, y_max_, num_points):
    x = np.random.uniform(low, high, num_points)
    y = np.random.uniform(y_min_, y_max_, num_points)
    under_curve = np.sum(y < func(x))
    # print(under_curve)
    area = (high - low) * (y_max_ - y_min_) * (under_curve / num_points)
    return area


def monte_carlo_integral(lower, upper, size):
    x = np.random.uniform(lower, upper, size)
    y = f(x)
    integral = np.mean(y) * (upper - lower)
    return integral


def quad(lower, upper, x):
    return spi.quad(x, lower, upper)


def print_results(results):
    header = f"| {'Experiments':<20} | {'Integral value':<15} |"
    separator = "| " + "-"*20 + " | " + "-"*15 + " |"
    row_template = "| {key:<20} | {value:^15.5f} |"
    footer = "| " + "-"*38 + " |"

    print(header)
    print(separator)
    for key, value in results.items():
        print(row_template.format(key=key, value=value))
    print(footer)


if __name__ == "__main__":
    lower = 0  # Нижня межа
    upper = 5  # Верхня межа

    experiments = [10, 100, 1000]
    results = {}
    for experiment in experiments:
        result = monte_carlo_integral(lower, upper, experiments)
        results[experiment] = result
    results["quad"] = quad(lower, upper, f)[0]

    print('\n')
    print('\033[33m', 'Порівняльна таблиця результатів експериментів \n методом Монте-Карло з функцією quad пакета scipy:', '\033[0m')
    print('\n')
    print_results(results)
    print('\n')

    draw_chart(lower, upper)
