import numpy as np
import itertools

def random_matrix(dim):
    """
    Функція створює квадратну матрицю розміром dim x dim із випадкових цілих чисел від 0 до 9.
    """
    return np.random.randint(10, size=(dim, dim))

def generate_permutations(n):
    """
    Функція створює список усіх перестановок індексів для матриці розміром n x n.
    
    Аргументи:
        n: ціле число, яке представляє розмір матриці.
    
    Повертає:
        Список усіх перестановок індексів для рядків або стовпців.
    """
    return list(itertools.permutations(range(n)))

def calculate_products(matrix, permutations):
    """
    Функція обчислює добуток елементів для кожної перестановки з урахуванням знаку.
    
    Аргументи:
        matrix: квадратна матриця з випадкових чисел.
        permutations: список перестановок індексів.
    
    Повертає:
        Список добутків для кожної перестановки, помножених на знак перестановки.
    """
    def permutation_sign(permutation):
        """
        Визначає знак перестановки: повертає 1 для парної перестановки і -1 для непарної.
        
        Аргумент:
            permutation: список індексів перестановки.
        
        Повертає:
            Знак перестановки (1 або -1).
        """
        inversions = 0
        n = len(permutation)
        for i in range(n):
            for j in range(i + 1, n):
                if permutation[i] > permutation[j]:
                    inversions += 1
        return 1 if inversions % 2 == 0 else -1
    
    products = []
    for permutation in permutations:
        sign = permutation_sign(permutation)
        product = 1
        for i in range(len(matrix)):
            product *= matrix[i, permutation[i]]
        products.append(sign * product)
    return products

def calculate_determinant(products):
    """
    Функція обчислює загальну суму добутків, що відповідає визначнику.
    
    Аргумент:
        products: список добутків для кожної перестановки.
    
    Повертає:
        Визначник матриці.
    """
    return sum(products)

# Основна програма
while True:
    try:
        dim = int(input("Введіть розмірність матриці (натуральне число): "))
        if dim > 0:
            break
        else:
            print("Помилка: Введіть натуральне число більше 0.")
    except ValueError:
        print("Помилка: Введіть ціле число.")

# Створення матриці
matrix = random_matrix(dim)
print("Згенерована матриця:")
print(matrix)

# Обчислення визначника за допомогою композиції функцій
permutations = generate_permutations(dim)
products = calculate_products(matrix, permutations)
determinant = calculate_determinant(products)

print("Визначник матриці:", determinant)
