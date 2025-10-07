class Patient:
    def __init__(self, pid, name, age, problem, severity):
        self.pid = pid
        self.name = name
        self.age = age
        self.problem = problem
        self.severity = severity

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
            print("No patients waiting.")
            return
        for p in self.q:
            print(f"ID: {p.pid}, Name: {p.name}, Age: {p.age}, Problem: {p.problem}")

class PriorityQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, p):
        self.q.append(p)
        self.q.sort(key=lambda x: x.severity, reverse=True)

    def dequeue(self):
        if self.q:
            return self.q.pop(0)
        return None

    def display(self):
        if not self.q:
            print("No emergency patients waiting.")
            return
        for p in self.q:
            print(f"ID: {p.pid}, Name: {p.name}, Age: {p.age}, Problem: {p.problem}, Severity: {p.severity}")

class Hospital:
    def __init__(self):
        self.normal = Queue()
        self.emergency = PriorityQueue()

    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        problem = input("Enter Problem Type: ")
        severity = int(input("Enter Severity Level (1-10): "))
        p = Patient(pid, name, age, problem, severity)
        if severity >= 7:
            self.emergency.enqueue(p)
            print("Emergency patient added to Priority Queue.")
        else:
            self.normal.enqueue(p)
            print("Normal patient added to Queue.")

    def attend_patient(self):
        if self.emergency.q:
            p = self.emergency.dequeue()
            print(f"Attending Emergency Patient: {p.name}, Problem: {p.problem}")
        elif self.normal.q:
            p = self.normal.dequeue()
            print(f"Attending Normal Patient: {p.name}, Problem: {p.problem}")
        else:
            print("No patients waiting.")

    def display_patients(self):
        print("\n--- Emergency Patients ---")
        self.emergency.display()
        print("\n--- Normal Patients ---")
        self.normal.display()

h = Hospital()
while True:
    print("\n1. Add Patient")
    print("2. Attend Patient")
    print("3. Display Patients")
    print("4. Exit")
    ch = input("Enter your choice: ")
    if ch == '1':
        h.add_patient()
    elif ch == '2':
        h.attend_patient()
    elif ch == '3':
        h.display_patients()
    elif ch == '4':
        break
    else:
        print("Invalid choice")
