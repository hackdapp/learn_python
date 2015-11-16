#!/usr/bin/python

class Employee(object):
	"""docstring for Employee"""

	_empCount = 0


	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		self._empCount += 1

	def displayCount(self):
		print "Total Employee %d" % self._empCount

	def displayEmployee(self):
		return "Name : ", self.name, ", Salary: ", self.salary

