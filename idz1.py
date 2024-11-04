import math

# Базовый класс Triad
class Triad:
    def __init__(self, a=0, b=0, c=0):
        """Инициализация тройки чисел"""
        self.a = a
        self.b = b
        self.c = c

    def set_values(self, a, b, c):
        """Метод для изменения значений полей"""
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        """Метод для вычисления суммы трех чисел"""
        return self.a + self.b + self.c

    def display(self):
        """Метод для отображения значений тройки чисел"""
        print(f"Числа: {self.a}, {self.b}, {self.c}")


# Производный класс Triangle
class Triangle(Triad):
    def __init__(self, a=0, b=0, c=0):
        """Инициализация треугольника через тройку сторон"""
        # Вызов конструктора базового класса
        super().__init__(a, b, c)
        if not self.is_valid_triangle():
            raise ValueError("Стороны не могут образовать треугольник.")

    def is_valid_triangle(self):
        """Проверка, могут ли стороны a, b и c образовать треугольник"""
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def area(self):
        """Метод для вычисления площади треугольника по формуле Герона"""
        s = self.sum() / 2  # Полупериметр
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def angles(self):
        """Метод для вычисления углов треугольника в градусах по сторонам"""
        angle_a = math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)))
        angle_b = math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)))
        angle_c = 180 - angle_a - angle_b  # Третий угол
        return angle_a, angle_b, angle_c

    def display(self):
        """Переопределение метода вывода для отображения треугольника"""
        print(f"Стороны треугольника: a = {self.a}, b = {self.b}, c = {self.c}")

# Демонстрация работы классов
if __name__ == '__main__':
    # Пример использования класса Triad
    print("Пример работы с тройкой чисел:")
    triad = Triad(1, 2, 3)
    triad.display()
    print(f"Сумма чисел: {triad.sum()}")

    print("\nПример работы с треугольником:")
    try:
        triangle = Triangle(3, 4, 5)  # Создаем треугольник с заданными сторонами
        triangle.display()
        print(f"Сумма сторон (периметр): {triangle.sum()}")
        print(f"Площадь треугольника: {triangle.area()}")
        angles = triangle.angles()
        print(f"Углы треугольника: A = {angles[0]:.2f}°, B = {angles[1]:.2f}°, C = {angles[2]:.2f}°")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПопытка создать треугольник с некорректными сторонами:")
    try:
        invalid_triangle = Triangle(1, 2, 3)  # Невозможный треугольник
    except ValueError as e:
        print(f"Ошибка: {e}")
