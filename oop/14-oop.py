# Mixin案例
#多態(單一類的多功能運用)
class Person():
    name = "liuying"
    age = 18

    def eat(self):
        print("EAT.......")

    def drink(self):
        print("DRINK......")

    def sleep(self):
        print("SLEEP.....")


class Teacher(Person):
    def work(self):
        print("Work")


class Student(Person):
    def study(self):
        print("Study")


class Tutor(Teacher, Student):
    pass


t = Tutor()

print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print("*" * 20)


class TeacherMixin():
    def work(self):
        print("Work")


class StudentMixin():
    def study(self):
        print("Study")


class TutorM(Person, TeacherMixin, StudentMixin):
    pass

#助教繼承老師與學生的功能
tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)