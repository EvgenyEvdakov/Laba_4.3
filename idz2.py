#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# необходимо реализовать абстрактный базовый класс, определив в нем абстрактные методы и свойства. Эти методы
# определяются в производных классах. В базовых классах должны быть объявлены абстрактные методы ввода/вывода, которые
# реализуются в производных классах.
# Вызывающая программа должна продемонстрировать все варианты вызова переопределенных абстрактных методов. Написать
# функцию вывода, получающую параметры базового класса по ссылке и демонстрирующую виртуальный вызов.
# Создать абстрактный базовый класс Pair с виртуальными арифметическими операциями. Создать производные классы
# FazzyNumber (нечеткое число) и Complex (комплексное число).


from abc import ABC, abstractmethod


# Абстрактный базовый класс Pair (S из SOLID — один класс выполняет одну задачу)
class Pair(ABC):
    @abstractmethod
    def input(self):
        """Абстрактный метод для ввода данных."""
        pass

    @abstractmethod
    def output(self):
        """Абстрактный метод для вывода данных."""
        pass

    @abstractmethod
    def add(self, other):
        """Абстрактный метод для сложения."""
        pass

    @abstractmethod
    def subtract(self, other):
        """Абстрактный метод для вычитания."""
        pass

    @abstractmethod
    def multiply(self, other):
        """Абстрактный метод для умножения."""
        pass


# Класс FuzzyNumber (S и O — один класс выполняет одну задачу и открыт для расширения)
class FuzzyNumber(Pair):
    def __init__(self, a=0.0, b=0.0):
        """Инициализация нечеткого числа с двумя параметрами."""
        self.a = a  # Нижний предел нечеткого числа
        self.b = b  # Верхний предел нечеткого числа

    def input(self):
        """Ввод нечеткого числа с клавиатуры."""
        self.a = float(input("Введите нижний предел нечеткого числа: "))
        self.b = float(input("Введите верхний предел нечеткого числа: "))

    def output(self):
        """Вывод нечеткого числа."""
        print(f"Нечеткое число: [{self.a}, {self.b}]")

    def add(self, other):
        """Сложение двух нечетких чисел."""
        if isinstance(other, FuzzyNumber):
            return FuzzyNumber(self.a + other.a, self.b + other.b)
        raise TypeError("Операция сложения поддерживается только между FuzzyNumber")

    def subtract(self, other):
        """Вычитание двух нечетких чисел."""
        if isinstance(other, FuzzyNumber):
            return FuzzyNumber(self.a - other.a, self.b - other.b)
        raise TypeError("Операция вычитания поддерживается только между FuzzyNumber")

    def multiply(self, other):
        """Умножение двух нечетких чисел."""
        if isinstance(other, FuzzyNumber):
            return FuzzyNumber(self.a * other.a, self.b * other.b)
        raise TypeError("Операция умножения поддерживается только между FuzzyNumber")


# Класс Complex (S и O — один класс выполняет одну задачу и открыт для расширения)
class Complex(Pair):
    def __init__(self, real=0.0, imag=0.0):
        """Инициализация комплексного числа."""
        self.real = real
        self.imag = imag

    def input(self):
        """Ввод комплексного числа с клавиатуры."""
        self.real = float(input("Введите действительную часть: "))
        self.imag = float(input("Введите мнимую часть: "))

    def output(self):
        """Вывод комплексного числа."""
        print(f"Комплексное число: {self.real} + {self.imag}i")

    def add(self, other):
        """Сложение двух комплексных чисел."""
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        raise TypeError("Операция сложения поддерживается только между Complex")

    def subtract(self, other):
        """Вычитание двух комплексных чисел."""
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        raise TypeError("Операция вычитания поддерживается только между Complex")

    def multiply(self, other):
        """Умножение двух комплексных чисел."""
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        raise TypeError("Операция умножения поддерживается только между Complex")


# Функция демонстрации полиморфизма через виртуальные вызовы методов базового класса (D - Dependency Inversion)
def demo_virtual_call(pair_obj: Pair):
    """Функция для демонстрации виртуальных вызовов методов базового класса."""
    pair_obj.output()
    print("Результат виртуального вызова метода сложения:")
    # Вызов метода сложения для объекта с самим собой, результат также выводится через виртуальный вызов
    pair_obj.add(pair_obj).output()


# Демонстрация работы
if __name__ == '__main__':
    print("Работа с нечеткими числами (FuzzyNumber):")
    fuzzy1 = FuzzyNumber(1.0, 2.0)
    fuzzy2 = FuzzyNumber(0.5, 1.5)

    fuzzy1.output()
    fuzzy2.output()

    result_fuzzy = fuzzy1.add(fuzzy2)
    print("Результат сложения нечетких чисел:")
    result_fuzzy.output()

    print("\nРабота с комплексными числами (Complex):")
    complex1 = Complex(2.0, 3.0)
    complex2 = Complex(1.0, -1.0)

    complex1.output()
    complex2.output()

    result_complex = complex1.add(complex2)
    print("Результат сложения комплексных чисел:")
    result_complex.output()

    print("\nДемонстрация полиморфизма:")
    demo_virtual_call(fuzzy1)  # Виртуальный вызов метода базового класса с объектом FuzzyNumber
    demo_virtual_call(complex1)  # Виртуальный вызов метода базового класса с объектом Complex