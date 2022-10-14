# Вар.5
# Kласс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер
# Функции-члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
# Создать список объектов. Вывести:
# a)	список автомобилей заданной марки;
# б) список автомобилей заданной модели, которые эксплуатируются больше n лет;

# Добавьте 5 магических метода к классу из предыдущего ДЗ.

import datetime
now = datetime.datetime.now()

class Car:

    car_list = []

    def get_car_id(self):
        return self.__car_id

    def get_car_brand(self):
        return self.__car_brand

    def get_car_model(self):
        return self.__car_model

    def get_car_year(self):
        return self.__car_year

    def get_car_color(self):
        return self.__car_color

    def get_car_price(self):
        return self.__car_price

    def get_car_regnumber(self):
        return self.__car_regnumber

    def set_car_id(self, car_id):
        if not self.is_car_id_exist(car_id):
            self.__car_id = car_id
        else:
            print('Авто с данным ID уже существует. Выберите другой ID')
            car_id = int(input('Введите ID авто: '))
            self.__car_id = self.set_car_id(car_id)
        return self.get_car_id()

    def is_car_id_exist(self, car_id):
        if Car.get_car_list():
            for i in range(len(Car.car_list)):
                if Car.car_list[i].get_car_id() == car_id:
                    return True
        else:
            return False

    def set_car_brand(self, car_brand):
        self.__car_brand = car_brand

    def set_car_model(self, car_model):
        self.__car_model = car_model

    def set_car_year(self, car_year):
        self.__car_year = car_year

    def set_car_color(self, car_color):
        self.__car_color = car_color

    def set_car_price(self, car_price):
        self.__car_price = car_price

    def set_car_regnumber(self, car_regnumber):
        self.__car_regnumber = car_regnumber

    @staticmethod
    def get_car_list():
        return Car.car_list

    @staticmethod
    def add_car_to_list(car):
        Car.car_list.append(car)

    @staticmethod
    def remove_car_from_list(car_id):
        flag = False
        index = 0
        for i in range(len(Car.car_list)):
            if Car.car_list[i].__car_id == car_id:
                index = i
                flag = True
        if flag == 0:
            print(f"Авто с ID {car_id} отсутствует в списке")
        else:
            Car.car_list.pop(index)
            print(f"Авто с ID {car_id} удален из списка")

    @staticmethod
    def print_car_list():
        if Car.car_list:
            for i in range(len(Car.car_list)):
                print(Car.car_list[i])
        else:
            print("Список авто пуст")

    @classmethod
    def find_car_by_brand(cls, brand_name):
        flag = False
        for i in range(len(cls.car_list)):
            if brand_name.casefold() in cls.car_list[i].__car_brand.casefold():
                print(cls.car_list[i])
                flag = True
        if flag == False:
            print(f"Запрошенное авто бренда \"{brand_name}\" в базе не найдено")

    @classmethod
    def find_car_by_model(cls, model, year):
        flag = False
        for i in range(len(cls.car_list)):
            if model.casefold() in cls.car_list[i].__car_model.casefold() and cls.car_list[i].__car_year < (now.year - year):
                print(cls.car_list[i])
                flag = True
        if flag == False:
            print(f"Запрошенное авто модели \"{model}\" в базе не найдено")


    def __str__(self):
        return 'ID авто ' + str(self.__car_id) + \
               '; Марка: ' + self.__car_brand + \
               '; Модель: ' + self.__car_model + \
               '; Год выпуска = ' + str(self.__car_year) + \
               '; Цвет = ' + self.__car_color + \
               '; Цена = ' + str(self.__car_price) + \
               '; Регистрационный номер = ' + (self.__car_regnumber)

    # def __setattr__(self, attr, value):
    #     if attr == 'car_id' or attr == 'car_brand' or attr == 'car_model' or attr == 'car_year' or attr == 'car_color' or attr == 'car_price' or attr == 'car_regnumber':
    #         self.__dict__[attr] = value
    #     else:
    #         print('Object Car doesn\'t have such attribute = ' + attr)
    #         raise AttributeError

    def __lt__(self, other):
        return self.__car_year < other.car_year

    def __gt__(self, other):
        return self.__car_year > other.car_year

    def __le__(self, other):
        return self.__car_year <= other.car_year

    def __ge__(self, other):
        return self.__car_year >= other.car_year

    def __eq__(self, other):
        return self.__car_year == other.car_year

    def __ne__(self, other):
        return self.__car_year != other.car_year

def add_new_car():
    car = Car()
    car.set_car_id(int(input('Введите ID авто: ')))
    car.set_car_brand(input('Введите марку: '))
    car.set_car_model(input('Введите модель: '))
    car.set_car_year(int(input('Введите год выпуска: ')))
    car.set_car_color(input('Введите цвет: '))
    car.set_car_price(int(input('Введите цену: ')))
    car.set_car_regnumber(input('Введите регистрационный номер: '))
    Car.add_car_to_list(car)
    print("Авто добавлено в список")
    print(car)

def add_new_cars():
    car = Car()
    car.set_car_id(int(11))
    car.set_car_brand('WV')
    car.set_car_model('Polo')
    car.set_car_year(int(2022))
    car.set_car_color('Grey')
    car.set_car_price(int(22000))
    car.set_car_regnumber('2022-7')
    Car.add_car_to_list(car)
    car = Car()
    car.set_car_id(int(12))
    car.set_car_brand('KIA')
    car.set_car_model('Rio')
    car.set_car_year(int(2017))
    car.set_car_color('Red')
    car.set_car_price(int(14000))
    car.set_car_regnumber('2017-7')
    Car.add_car_to_list(car)
    car = Car()
    car.set_car_id(int(13))
    car.set_car_brand('Renault')
    car.set_car_model('Clio')
    car.set_car_year(int(2020))
    car.set_car_color('Blue')
    car.set_car_price(int(15000))
    car.set_car_regnumber('2020-7')
    Car.add_car_to_list(car)

option = 1
while option != 0:
    print('\nМеню')
    print('1 - Добавить авто')
    print('2 - Удалить авто')
    print('3 - Список авто')
    print('4 - Список авто, заданной марки')
    print('5 - Список авто, заданной модели и старше возраста')
    print('6 - Добавить авто автоматически')
    print('0 - Выход')
    option = int(input('\nВыберите нужный пункт: '))
    if option == 1:
        print('Добавление авто')
        add_new_car()
    elif option == 2:
        car_id = int(input('\nВведите Id удаляемого авто: '))
        Car.remove_car_from_list(car_id)
    elif option == 3:
        print('\nСписок авто: ')
        Car.print_car_list()
    elif option == 4:
        findbrand = input('Введите марку авто: ')
        Car.find_car_by_brand(findbrand)
    elif option == 5:
        findmodel = input('Введите модель авто: ')
        findyear =  int(input('Введите возраст авто: '))
        Car.find_car_by_model(findmodel, findyear)
    elif option == 6:
        add_new_cars()
        print('\nАвто добавлены')
    elif option == 0:
        print("Программа завершена")
        option = 0
    else:
        print("Данный пункт недоступен. Выберите другой")
        continue

