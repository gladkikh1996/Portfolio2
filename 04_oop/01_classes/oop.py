from enum import Enum


class RoomType(Enum):
    SINGLE = "одноместный"
    DOUBLE = "двухместный"
    TRIPLE = "трехместный"
    LUX = "люкс"


class Room:
    def __init__(self, room_number, room_type, price, is_booked=False):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self._is_booked = is_booked

    def book(self):
        self._is_booked = True

    def cancel_booking(self):
        self._is_booked = False

    def is_available(self):
        return not self._is_booked

    def __str__(self):
        status = "свободна" if self.is_available() else "занята"
        return f"Номер: {self.room_number}, тип: {self.room_type.value}, цена: {self.price}, статус: {status}"


class LuxuryRoom(Room):
    def __init__(self, room_number, price, jacuzzi_size, is_booked=False):
        super().__init__(room_number, RoomType.LUX, price, is_booked)
        self.jacuzzi_size = jacuzzi_size

    def __str__(self):
        status = "свободна" if self.is_available() else "занята"
        return f"Номер: {self.room_number}, тип: {self.room_type.value}, цена: {self.price}, джакузи: {self.jacuzzi_size}, статус: {status}"


class Hotel:
    def __init__(self, name, location, rooms=None):
        self.name = name
        self.location = location
        self.rooms = rooms if rooms is not None else []

    def add_room(self, room):
        self.rooms.append(room)

    def show_available_rooms(self):
        for room in self.rooms:
            if room.is_available():
                print(room)

    def calculate_total_available_price(self):
        total = 0
        for room in self.rooms:
            if room.is_available():
                total += room.price
        return total


hotel = Hotel("Морской берег", "Сочи")

room1 = Room(101, RoomType.SINGLE, 3000)
room2 = Room(102, RoomType.DOUBLE, 4500)
room3 = Room(103, RoomType.TRIPLE, 6000, True)
room4 = LuxuryRoom(201, 12000, "L")

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)
hotel.add_room(room4)

hotel.show_available_rooms()
print(hotel.calculate_total_available_price())