#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо создать класс Triad (тройка чисел); определить методы изменения полей и вычисления суммы чисел.
# Определить производный класс Triangle с полями-сторонами. Определить методы вычисления углов и площади треугольника.

import math
from abc import ABC, abstractmethod


# Интерфейс для объектов, у которых можно вычислить сумму (I из SOLID).
class Summable(ABC):
    @abstractmethod
    def sum(self):
        """Абстрактный метод для вычисления суммы чисел."""
        pass


# Класс для представления тройки чисел, реализующий интерфейс Summable (S и I из SOLID).
class Triad(Summable):
    def __init__(self, a=0, b=0, c=0):
        """Инициализация тройки чисел."""
        self._validate_numbers(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def _validate_numbers(self, a, b, c):
        """Проверка, что значения чисел корректны."""
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
            raise ValueError("Все значения должны быть числами.")

    def set_values(self, a, b, c):
        """Метод для изменения значений полей."""
        self._validate_numbers(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        """Метод для вычисления суммы трех чисел."""
        return self.a + self.b + self.c

    def display(self):
        """Метод для отображения значений тройки чисел."""
        print(f"Числа: {self.a}, {self.b}, {self.c}")


# Интерфейс для объектов, представляющих геометрические фигуры (S и I из SOLID).
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Абстрактный метод для вычисления площади фигуры."""
        pass

    @abstractmethod
    def display(self):
        """Абстрактный метод для отображения информации о фигуре."""
        pass


# Класс для представления треугольника, унаследованный от Triad и реализующий интерфейсы Summable и Shape (D из SOLID).
class Triangle(Triad, Shape):
    def __init__(self, a=0, b=0, c=0):
        """Инициализация треугольника через тройку сторон."""
        super().__init__(a, b, c)
        if not self.is_valid_triangle():
            raise ValueError("Стороны не могут образовать треугольник.")

    def is_valid_triangle(self):
        """Проверка, могут ли стороны a, b и c образовать треугольник (L из SOLID)."""
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def area(self):
        """Метод для вычисления площади треугольника по формуле Герона."""
        s = self.sum() / 2  # Полупериметр
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def angles(self):
        """Метод для вычисления углов треугольника в градусах по сторонам."""
        angle_a = math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)))
        angle_b = math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)))
        angle_c = 180 - angle_a - angle_b  # Третий угол
        return angle_a, angle_b, angle_c

    def display(self):
        """Переопределение метода вывода для отображения треугольника."""
        print(f"Стороны треугольника: a = {self.a}, b = {self.b}, c = {self.c}")


# Фабрика для создания объектов Triad и Triangle (D из SOLID).
class ShapeFactory:
    @staticmethod
    def create_triad(a, b, c):
        """Создание объекта Triad."""
        return Triad(a, b, c)

    @staticmethod
    def create_triangle(a, b, c):
        """Создание объекта Triangle с проверкой на допустимость сторон."""
        return Triangle(a, b, c)


# Демонстрация работы классов
if __name__ == '__main__':
    # Пример использования класса Triad
    print("Пример работы с тройкой чисел:")
    triad = ShapeFactory.create_triad(1, 2, 3)
    triad.display()
    print(f"Сумма чисел: {triad.sum()}")

    print("\nПример работы с треугольником:")
    try:
        triangle = ShapeFactory.create_triangle(3, 4, 5)  # Создаем треугольник с заданными сторонами
        triangle.display()
        print(f"Сумма сторон (периметр): {triangle.sum()}")
        print(f"Площадь треугольника: {triangle.area()}")
        angles = triangle.angles()
        print(f"Углы треугольника: A = {angles[0]:.2f}°, B = {angles[1]:.2f}°, C = {angles[2]:.2f}°")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПопытка создать треугольник с некорректными сторонами:")
    try:
        invalid_triangle = ShapeFactory.create_triangle(1, 2, 3)  # Невозможный треугольник
    except ValueError as e:
        print(f"Ошибка: {e}")
