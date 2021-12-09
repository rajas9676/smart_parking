from parking_lot import ParkingLot, Car

parking_lot = ParkingLot()

cars = [
    Car('KA-01-HH-1234', 'White'),
    Car('KA-01-HH-9999', 'White'),
    Car('KA-01-BB-0001', 'Black'),
    Car('KA-01-HH-7777', 'Red'),
    Car('KA-01-HH-2701', 'Blue'),
    Car('KA-01-HH-3141', 'Black'),
]

assert parking_lot.create_parking_lot(6) is True

for i in range(0, len(cars)):
    assert parking_lot.park(cars[i]) == i + 1

assert parking_lot.leave(4) is True
assert parking_lot.status() is True

assert len(parking_lot.open_slots) == 1
assert parking_lot.park(Car('KA-01-P-333', 'White')) == 4

assert parking_lot.registration_numbers_for_cars_with_colour('White') == ['KA-01-HH-1234', 'KA-01-HH-9999', 'KA-01-P-333']
assert parking_lot.slot_numbers_for_cars_with_colour('White') == [1, 2, 4]
assert parking_lot.slot_number_for_registration_number('KA-01-HH-3141') == 6
assert parking_lot.slot_number_for_registration_number('MH-04-AY-1111') is None
