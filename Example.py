# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 01:25:10 2024

@author: vorontsova
"""

class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Должность: {self.position}")

def calculate_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

def apply_bonus(salary, bonus_percentage):
    return salary * (1 + bonus_percentage / 100)

def generate_payslip(employee, salary, bonus):
    print(f"Имя: {employee.name}")
    print(f"Базовая ЗП: {salary}")
    print(f"ЗП с бонусом: {bonus}")

if __name__ == "__main__":
    employee1 = Employee("Иван Иванов", 30, "Разработчик")
    employee1.display_info()
    hours_worked = 160
    hourly_rate = 100
    salary = calculate_salary(hours_worked, hourly_rate)
    bonus_percentage = 10
    bonus = apply_bonus(salary, bonus_percentage)
    generate_payslip(employee1, salary, bonus)
