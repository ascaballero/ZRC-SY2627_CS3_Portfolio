#Parent Class
class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

#Child Class 1
class SeniorPatient(Patient):
    def __init__(self, name, bill_amount, ):
        super().__init__(name, bill_amount)


    def calculate_bill(self):
        discount = self.bill_amount * 0.2  
        return self.bill_amount - discount

#Child Class 2
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount,):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        coverage = self.bill_amount * 0.15
        return self.bill_amount - coverage

#sample patients
regular_patient = Patient("Juan Dela Crus", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

#sample output
for patient in patients:
    print("Hospital Billing System")
    print("-----")
    print(f"Patient: {patient.get_name()}")
    print(f"Bill Amount: {patient.get_bill_amount()}")
    print(f"Adjusted Bill: {patient.calculate_bill()}")
    print("-----")