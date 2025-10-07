class Passenger:
    def __init__(self, name, age, gender, train_no, seat_pref):
        self.name = name
        self.age = age
        self.gender = gender
        self.train_no = train_no
        self.seat_pref = seat_pref
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.capacity = 5

    def count(self):
        c = 0
        t = self.head
        while t:
            c += 1
            t = t.next
        return c

    def add_passenger(self, passenger):
        if self.count() >= self.capacity:
            return False
        if not self.head:
            self.head = passenger
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = passenger
        return True

    def remove_passenger(self, name):
        t = self.head
        p = None
        while t:
            if t.name == name:
                if p:
                    p.next = t.next
                else:
                    self.head = t.next
                return True
            p = t
            t = t.next
        return False

    def display(self):
        t = self.head
        if not t:
            print("No booked tickets.")
            return
        while t:
            print(f"Name: {t.name}, Age: {t.age}, Gender: {t.gender}, Train No: {t.train_no}, Seat: {t.seat_pref}")
            t = t.next

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, p):
        self.q.append(p)

    def dequeue(self):
        if self.q:
            return self.q.pop(0)
        return None

    def display(self):
        if not self.q:
            print("Waiting list is empty.")
            return
        for p in self.q:
            print(f"Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Train No: {p.train_no}, Seat: {p.seat_pref}")

class RailwayBooking:
    def __init__(self):
        self.booked = LinkedList()
        self.waiting = Queue()

    def book_ticket(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        train_no = int(input("Enter Train No: "))
        seat_pref = input("Enter Seat Preference: ")
        p = Passenger(name, age, gender, train_no, seat_pref)
        if not self.booked.add_passenger(p):
            self.waiting.enqueue(p)
            print("No seats available. Added to waiting list.")
        else:
            print("Ticket booked successfully.")

    def cancel_ticket(self):
        name = input("Enter Name to Cancel Ticket: ")
        if self.booked.remove_passenger(name):
            print("Ticket cancelled.")
            w = self.waiting.dequeue()
            if w:
                self.booked.add_passenger(w)
                print(f"Seat assigned to {w.name} from waiting list.")
        else:
            print("Passenger not found in booked list.")

    def display_status(self):
        print("\n--- Booked Tickets ---")
        self.booked.display()
        print("\n--- Waiting List ---")
        self.waiting.display()

r = RailwayBooking()
while True:
    print("\n1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Display Status")
    print("4. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        r.book_ticket()
    elif ch == '2':
        r.cancel_ticket()
    elif ch == '3':
        r.display_status()
    elif ch == '4':
        break
    else:
        print("Invalid choice")
