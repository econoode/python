class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

anna = WorkingStudent('Anna', 'Binus', 20)
anna.marks.append(56)
anna.marks.append(79)
anna.marks.append(80)

print(anna.average())

friend = WorkingStudent.friend(anna, 'Greg', 17.50)
print(friend.name)
print(friend.school)
print(friend.salary)