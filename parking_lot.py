import heapq
from collections import defaultdict, OrderedDict


class Car:
    def __init__(self, registration_number, color):
        self.registration_number = registration_number
        self.color = color

    def __str__(self):
        return "Car (Registration No:{} Color:{})".format(self.registration_number, self.color)


class ParkingLot:
    def __init__(self):
        # Initialize all slots to be open and available for parking
        self.open_slots = []
        # Dictionary to map car registration number and slot no parked in
        self.registration_slot_mapping = dict()
        # Mapping data structure to assign list of registration numbers with same color
        self.color_registration_mapping = defaultdict(list)
        # we need to maintain the orders of cars while showing 'status'
        self.occupied_slots = OrderedDict()

    def create_parking_lot(self, total_slots):
        # Using min heap as this will always give minimum slot number in O(1) time
        print("Created a parking lot with {} slots".format(total_slots))
        for i in range(1, total_slots + 1):
            heapq.heappush(self.open_slots, i)
        return True

    def get_nearest_slot(self):
        # Retrieve the nearest slot available for parking
        return heapq.heappop(self.open_slots) if self.open_slots else None

    def park(self, car):
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        print("Allocated slot number: {}".format(slot_no))
        self.occupied_slots[slot_no] = car
        self.registration_slot_mapping[car.registration_number] = slot_no
        self.color_registration_mapping[car.color].append(car.registration_number)
        return slot_no

    def leave(self, slot_to_be_freed):
        found = None
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_be_freed:
                found = registration_no
        # Cleanup from all cache
        if found:
            heapq.heappush(self.open_slots, slot_to_be_freed)
            del self.registration_slot_mapping[found]
            car_to_leave = self.occupied_slots[slot_to_be_freed]
            self.color_registration_mapping[car_to_leave.color].remove(found)
            del self.occupied_slots[slot_to_be_freed]
            print("slot number {} is free".format(slot_to_be_freed))
            return True
        else:
            print("slot is not in use")
            return False

    def status(self):
        print("slot No.   Registration No    Colour")
        for slot, car in self.occupied_slots.items():
            print("{}           {}       {}".format(slot, car.registration_number, car.color))
        return True

    # Get registration numbers of all cars of a particular colour
    def registration_numbers_for_cars_with_colour(self, color):
        registration_numbers = self.color_registration_mapping[color]
        print(", ".join(registration_numbers))
        return self.color_registration_mapping[color]

    # Get all parking slots where cars of a particular color are parked
    def slot_numbers_for_cars_with_colour(self, color):
        registration_numbers = self.color_registration_mapping[color]
        slots = [self.registration_slot_mapping[registration_number] for registration_number in registration_numbers]
        print(", ".join(map(str, slots)))
        return slots

    # Get parking slot of a given car registration number
    def slot_number_for_registration_number(self, registration_number):
        slot_number = None
        if registration_number in self.registration_slot_mapping:
            slot_number = self.registration_slot_mapping[registration_number]
            print(slot_number)
        else:
            print('Not found')
        return slot_number
