import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'

    def get_photo_file_ext(self):
        CarBase.get_photo_file_ext(self)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'
        list_whl = self.body_whl.split('x')
        if len(list_whl) == 1:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0
        else:
            self.body_length = float(list_whl[0])
            self.body_width = float(list_whl[1])
            self.body_height = float(list_whl[2])

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width

    def get_photo_file_ext(self):
        CarBase.get_photo_file_ext(self)


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'

    def get_photo_file_ext(self):
        CarBase.get_photo_file_ext(self)


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        i = 0
        for row in reader:
            if len(row) < 7:
                continue
            if row[0] == 'car':
                car_list.append(1)
                car_list[i] = Car(row[1], row[3], row[5], row[2])
                i += 1
            if row[0] == 'truck':
                car_list.append(1)
                car_list[i] = Truck(row[1], row[3], row[5], row[4])
                i += 1
            if row[0] == 'spec_machine':
                car_list.append(1)
                car_list[i] = SpecMachine(row[1], row[3], row[5], row[6])
                i += 1
    return car_list


