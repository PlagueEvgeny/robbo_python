class Employee:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    def work(self):
        print(f"{self.name} Works")
        


class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    def study(self):
        print(f"Student: {self.name}")


class WorkingStudents(Employee, Student):
    pass

tom = WorkingStudents('Mark')
tom.work()
tom.study()
