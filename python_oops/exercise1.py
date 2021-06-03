import datetime


class Person:
    def __init__(self,name,birth_date,email):

        self.name = name
        self.birth_date = birth_date
        self.email = email
        self._age=None
        self._recalc_date=None
        self.recalc_age()

    def recalc_age(self):
        today = datetime.date.today()
        age = today.year-self.birth_date.year
        if today < datetime.date(today.year, self.birth_date.month, self.birth_date.day):
            age -= 1
        self._age=age
        self._recalc_date=today

    def age(self):
        if self._recalc_date < datetime.date.today():
            self.recalc_age()
            return self._age


if __name__ == "__main__":
    person = Person("chinnu",datetime.date(1994,9,28),"chinnu@gmail.com")
    print(person.name)
    print(person.email)
    print(person.age())

