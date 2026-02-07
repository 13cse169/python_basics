"""Python OOP / classes examples.

This file demonstrates:
- simple class with __init__ and __repr__
- encapsulation (convention _private, name-mangling)
- properties (getter/setter)
- classmethod and staticmethod
- inheritance and method overriding
- composition (class using other class instances)
- dataclass example for lightweight classes

Run as a script to see example output.
"""

from dataclasses import dataclass
from typing import List


class Person:
	species = "Homo sapiens"  # class attribute

	def __init__(self, name: str, age: int):
		self.name = name
		self._age = int(age)  # "protected" by convention

	def greet(self) -> str:
		return f"Hello, my name is {self.name}."

	@property
	def age(self) -> int:
		"""Age exposed as a read-only property by default."""
		return self._age

	@age.setter
	def age(self, value: int) -> None:
		if value < 0:
			raise ValueError("age must be >= 0")
		self._age = int(value)

	@classmethod
	def species_name(cls) -> str:
		return cls.species

	@staticmethod
	def is_adult(age: int) -> bool:
		return age >= 18

	def __repr__(self) -> str:
		return f"Person(name={self.name!r}, age={self._age})"


class Employee(Person):
	def __init__(self, name: str, age: int, salary: float, role: str = "Employee"):
		super().__init__(name, age)
		self.salary = float(salary)
		self.role = role

	def greet(self) -> str:
		base = super().greet()
		return f"{base} I work as a {self.role}."

	def give_raise(self, amount: float) -> None:
		self.salary += float(amount)

	def __repr__(self) -> str:
		return f"Employee(name={self.name!r}, age={self._age}, role={self.role!r}, salary={self.salary})"


class Company:
	def __init__(self, name: str):
		self.name = name
		self._employees: List[Employee] = []

	def hire(self, emp: Employee) -> None:
		self._employees.append(emp)

	def payroll(self) -> float:
		return sum(e.salary for e in self._employees)

	def __repr__(self) -> str:
		return f"Company(name={self.name!r}, employees={len(self._employees)})"


@dataclass
class Point:
	x: float
	y: float


def main():
	print("--- Person / Employee examples ---")
	p = Person("Alice", 30)
	print(p)
	print(p.greet())
	print("species:", Person.species_name())
	print("is adult:", Person.is_adult(p.age))

	print("\n--- property setter (age) and validation ---")
	try:
		p.age = 35
		print("updated age ->", p.age)
		p.age = -5
	except ValueError as e:
		print("caught expected ValueError when setting invalid age:", e)

	print("\n--- Employee / inheritance ---")
	e = Employee("Bob", 28, salary=50000, role="Developer")
	print(e)
	print(e.greet())
	e.give_raise(2500)
	print("after raise ->", e)

	print("\n--- Company / composition ---")
	c = Company("Acme")
	c.hire(e)
	c.hire(Employee("Carol", 35, 70000, role="Manager"))
	print(c)
	print("payroll ->", c.payroll())

	print("\n--- dataclass example ---")
	p1 = Point(1.0, 2.0)
	p2 = Point(1.0, 2.0)
	print("p1, p2 ->", p1, p2)
	print("p1 == p2 ->", p1 == p2)


if __name__ == '__main__':
	main()

