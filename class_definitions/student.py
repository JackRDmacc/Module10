class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

        if not self.last_name.isalpha():
            raise ValueError

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


# Driver
student = Student('Reser', 'Jack', 'CIS', 4.0)
print(str(student))
