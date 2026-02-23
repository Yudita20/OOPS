class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


# Inheritance
# Cannot inherit private data members and methods
class Student(User):
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

std = Student()

std.enroll()
std.login()
std.review()
std.register()