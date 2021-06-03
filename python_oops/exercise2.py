class Smith:
    surname ="chinnu"
    profession="minu"

    def __init__(self,name,profession=None):
        self.name=name
        if profession is not None:
            self.profession=profession


person2 = Smith("df","hlh")
print(person2.name)
print(person2.profession)


# class Average:
#
#     def __init__(self,lst=None):
#         self.lst = self.get_numbers()
#
#     def get_numbers(self):
#         a = int(input("first number"))
#         b = int(input("first number"))
#         c = int(input("first number"))
#         return [a,b,c]
#
#     def get_avg(self):
#         avg = sum(self.lst)/len(self.lst)
#         print(avg)
#
# fg=Average()
# fg.get_avg()
