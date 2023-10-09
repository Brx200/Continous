class Student():
    def __init__(self, name, Class, teacher):
        self.name = name
        self.Class = Class
        self.teacher = teacher
    def get_name(self):
        return self.name
    def get_Class(self):
        return self.Class
    
    def __str__(self):
        return f"{self.name} is a student, {self.name} is in {self.Class}. {self.name} best teacher is {self.teacher}"
    
it_baby = Student('John','ss3', 'Okem')
print(it_baby)