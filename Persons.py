

class Person:
    def __init__(self, fio, age, passport, weight):
        if self.verify_fio(fio):
            self.__fio = fio
        if self.verify_age(age):
            self.__age = age
        if self.verify_ps(passport):
            self.__passport = passport
        if self.verify_weight(weight):
            self.__weight = weight

    @classmethod
    def verify_fio(cls, name):
        if type(name) != str:
            raise TypeError('ФИО должно быть строкой')
        if len(name) < 5:
            raise TypeError('В ФИО должен быть хотя бы один символ')
        if name.count(' ') != 2:
            raise TypeError('Неверный формат записи ФИО')
        if not name.replace(' ','').isalpha():
            raise TypeError('В ФИО можно использовать только буквенные символы')
        else:
            return True

    @classmethod
    def verify_age(cls, num):
        if type(num) != int:
            raise TypeError('Возраст должен быть целым числом')
        if 150 <= num:
            raise TypeError('Возраст должен быть от 14 до 150')
        if num <= 14:
            raise TypeError('Возраст должен быть от 14 до 150')
        else:
            return True

    @classmethod
    def verify_ps(cls, pswd):
        if type(pswd) != str:
            raise TypeError('Паспорт должен быть строкой')
        if pswd[4] != ' ':
            raise TypeError('Неверный формат паспорта')
        if not pswd.replace(' ','').isdigit():
            raise TypeError('Серия и номер паспорта должны содержать только числа')
        else:
            return True

    @classmethod
    def verify_weight(cls, kg):
        if type(kg) != float:
            raise TypeError('Вес должен быть вещественным числом от 25 и выше')
        if 25 > kg:
            raise TypeError('Вес должен быть вещественным числом от 25 и выше')
        else:
            return True

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_ps(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    def set_data(self, fio, age, passport, weight):
        self.__fio = fio
        self.__age = age
        self.__passport = passport
        self.__weight = weight

    def get_data(self):
        return self.__fio, self.__age, self.__passport, self.__weight



p = Person("Petrov Roman Galinovich", 19, '4321 557891', 56.0)
p2 = Person('Багров Данила Братович', 25, '2589 654123', 75.2)
print(p2.get_data())
print(p.get_data())
p.fio = "Пушкин Александр Серг"
print(p.get_data())