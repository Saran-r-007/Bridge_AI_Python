class studentdetails:
    college = "sns"
    year = "4th year"

    @staticmethod
    def func():
        print("hello guys")
    @staticmethod
    def func2():
        print("hello guys")

obj1 = studentdetails()
print(obj1.college)
obj1.func()
obj1.func2()