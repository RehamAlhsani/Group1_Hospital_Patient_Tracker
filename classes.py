class Patient :
    def __init__(self , name , national_id , age , blood_type) :
        self.name = name
        self.national_id = national_id
        self.age = age
        self.blood_type = blood_type
        self._medical_history = []

    def add_note(self , text) :
        self._medical_history.append(text)

    def get_history(self) :
        return self._medical_history

    def display(self) :
        print(f"Name : {self.name}")
        print(f"ID : {self.national_id}")
        print(f"Age : {self.age}")
        print(f"Blood Type : {self.blood_type}")


class Doctor :
    def __init__(self , name , doctor_id , department):
        self.name = name
        self.doctor_id = doctor_id
        self.department = department
        self.appointments = []

    def consultation_fee(self) :
        return 0

    def add_appointment(self , appt):
        self.appointments.append(appt)

    def cancel_appointment(self , appt):
        if appt in self.appointments:
            self.appointments.remove(appt)

    def display(self):
        print(f"Doctor : {self.name}")
        print(f"ID : {self.doctor_id}")
        print(f"Department : {self.department}")


class GeneralDoctor(Doctor) :
    def consultation_fee(self) :
        return 100


class Specialist(Doctor) :
    def __init__(self , name , doctor_id , department , specialty) :
        super().__init__(name, doctor_id, department)
        self.specialty = specialty

    def consultation_fee(self) :
        return 250