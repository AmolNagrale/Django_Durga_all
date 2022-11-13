from django.test import TestCase
from crudfbvApp.models import Employee

# Create your tests here.

class EmployeeTestCase(TestCase):
    def setUp(self):
        print('setUp activity')
        Employee.objects.create(eno=100,ename='amol',esal=1000,eaddr='nagpur')
        Employee.objects.create(eno=200,ename='amit',esal=2000,eaddr='pune')

def test_employee_info(self):
    print('testing Employee information')
    qs=Employee.objects.all()
    self.assertEqual(qs.count(),2)
    e1=Employee.objects.get(ename='amol')
    e2=Employee.objects.get(ename='amit')
    self.assertEqual(e1.get_salary(),1000)
    self.assertEqual(e2.get_salary(),2000)