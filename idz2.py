from abc import ABC, abstractmethod

# Абстрактный класс Pair
class Pair(ABC):
    @abstractmethod
    def input(self):
        """Абстрактный метод для ввода данных"""
        pass

    @abstractmethod
    def output(self):
        """Абстрактный метод для вывода данных"""
        pass

    @abstractmethod
    def add(self, other):
        """Абстрактный метод для сложения"""
        pass

    @abstractmethod
    def subtract(self, other):
        """Абстрактный метод для вычитания"""
        pass

    @abstractmethod
    def multiply(self, other):
        """Абстрактный метод для умножения"""
        pass


# Класс FuzzyNumber (нечеткое число)
class FuzzyNumber(Pair):
    def __init__(self, a=0.0, b=0.0):
        """Инициализация нечеткого числа с двумя параметрами"""
        self.a = a  # Низкий предел нечеткого числа
        self.b = b  # Высокий предел нечеткого числа

    def input(self):
        """Ввод нечеткого числа с клавиатуры"""
        self.a = float(input("Введите низкий предел нечеткого числа: "))
        self.b = float(input("Введите высокий предел нечеткого числа: "))

    def output(self):
        """Вывод нечеткого числа"""
        print(f"Нечеткое число: [{self.a}, {self.b}]")

    def add(self, other):
        """Сложение двух нечетких чисел"""
        if isinstance(other, FuzzyNumber):
            return FuzzyNumber(self.a + other.a, self.b + other.b)
        raise TypeError("Операция поддерживается только между FuzzyNumber")

    def subtract(self, other):
        """Вычитание двух нечетких чисел"""
        if isinstance(other, FuzzyNumber):
            return FuzzyNumber(self.a - other.a, self.b - other.b)
        raise TypeError("Операция поддерживается только между FuzzyNumber")

    def multiply(self, other):
        """Умножение двух нечетких чисел"""
        if isinstance(other, FuzzyNumber):
            return FuzzyNumber(self.a * other.a, self.b * other.b)
        raise TypeError("Операция поддерживается только между FuzzyNumber")


# Класс Complex (комплексное число)
class Complex(Pair):
    def __init__(self, real=0.0, imag=0.0):
        """Инициализация комплексного числа"""
        self.real = real
        self.imag = imag

    def input(self):
        """Ввод комплексного числа с клавиатуры"""
        self.real = float(input("Введите действительную часть: "))
        self.imag = float(input("Введите мнимую часть: "))

    def output(self):
        """Вывод комплексного числа"""
        print(f"Комплексное число: {self.real} + {self.imag}i")

    def add(self, other):
        """Сложение двух комплексных чисел"""
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        raise TypeError("Операция поддерживается только между Complex")

    def subtract(self, other):
        """Вычитание двух комплексных чисел"""
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        raise TypeError("Операция поддерживается только между Complex")

    def multiply(self, other):
        """Умножение двух комплексных чисел"""
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        raise TypeError("Операция поддерживается только между Complex")


# Функция для демонстрации полиморфизма
def demo_virtual_call(pair_obj):
    """Функция для демонстрации виртуальных вызовов методов базового класса"""
    pair_obj.output()  # Вызов метода вывода
    print("Метод сложения будет вызван виртуально:")
    pair_obj.add(pair_obj).output()  # Вызов метода сложения и вывод результата


# Демонстрация работы
if __name__ == '__main__':
    print("Работа с нечеткими числами (FuzzyNumber):")
    fuzzy1 = FuzzyNumber(1.0, 2.0)
    fuzzy2 = FuzzyNumber(0.5, 1.5)

    fuzzy1.output()
    fuzzy2.output()

    result = fuzzy1.add(fuzzy2)
    print("Результат сложения нечетких чисел:")
    result.output()

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
