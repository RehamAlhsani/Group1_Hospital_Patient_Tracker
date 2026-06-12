from classes import Patient , Doctor , GeneralDoctor , Specialist


class Hospital :
    def __init__(self) :
        self.patients = {}
        self.doctors = {}
        self.blood_types = set()

    # System Features  1 : Register a New Patient 
    def register_patient(self) :
        name = input(" What's your name ? ")
        national_id = input(" What's your national ID ? ")

        if national_id in self.patients :
            print(" Patient already exists ! ")
            return

        try :
            age = int(input(" How old are you ? "))
        except ValueError :
            print("Please, Enter a number for age !")
            return

        blood_type = input(" What's your blood type ? ")

        patient = Patient(name , national_id , age , blood_type)

        self.patients[national_id] = patient
        self.blood_types.add(blood_type)

        print("Patient registered")

    # System Features  2 : Add a New Doctor  
    def add_doctor(self) :
        name = input(" What's the doctor's name ? ")
        doctor_id = input(" What's the doctor ID ? ")
        doc_type = input(" What's the type : general or specialist ? ").lower()
        department = input(" What's the department ? ")

        match doc_type :
            case "general" :
                doctor = GeneralDoctor(name , doctor_id , department)

            case "specialist" :
                specialty = input("Specialty ? ")
                doctor = Specialist(name , doctor_id , department , specialty)

            case _ :
                print("Invalid type")
                return

        self.doctors[doctor_id] = doctor
        print("Doctor added")

    # System Features  3 : Book an Appointment  
    def book_appointment(self) :
        patient_id = input("What's the patient ID ? ")
        doctor_id = input("What's the doctor ID ? ")

        if patient_id not in self.patients or doctor_id not in self.doctors:
           print("Not found !")
           return

        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]

        date = input("Date (YYYY-MM-DD) ? ")
        time = input("Time ? ")

        for appt in doctor.appointments :
            if appt[0] == date and appt[1] == time :
              print("Doctor busy")
              return

        appointment = (date, time, doctor.name, patient.name)

        doctor.add_appointment(appointment)
        patient.add_note(f"Booked with Dr {doctor.name}")

        print(f"Booked - Fee: {doctor.consultation_fee()} SAR")
        print("Appointment booked successfully")