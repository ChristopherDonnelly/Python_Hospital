'''
You're going to build a hospital with patients in it! Create a hospital class.

Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?

# Patient:
Attributes:
• Id: an id number
• Name
• Allergies
• Bed number: should be none by default

# Hospital
Attributes:
• Patients: an empty array
• Name: hospital name
• Capacity: an integer indicating the maximum number of patients the hospital can hold.

Methods:
• Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
• Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.

This is a challenging assignment. Ask yourself what input each method requires and what output you will need.
'''

class Patient(object):
    def __init__(self, uniqueId, name, allergies, bed_num="none"):
        self.uniqueId = uniqueId
        self.name = name
        self.allergies = allergies
        self.bed_num = bed_num
    def info(self):
        print '~~~ Patient Information ~~~\n\tPatient ID: {}\n\tPatient Name: {}\n\tAllergies: {}\n\tBed Number: {}\n'.format(self.uniqueId, self.name, self.allergies, self.bed_num)
        return self

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.patientIds = 0
        # Create dictionary of bed numbers associated with maximum capacity for Hospital
        self.bed_numbers = dict.fromkeys(range(1, capacity+1), 0)
    def admit(self, patientName, allergies):
        # Before Admintion verify that the Number of admitted patients is less than the capacity of the Hospital
        if len(self.patients) < self.capacity:
            # Iterate Unique Patient ID
            self.patientIds += 1
            # Loop through key, value pairs of Bed Numbers available and return first available bed number
            tempBed = next(key for key, value in self.bed_numbers.items() if value == 0)
            # Set bed number to occupied (1)
            self.bed_numbers[tempBed] += 1
            # Insert new patient into patients array at index of associated bed number
            self.patients.insert(tempBed-1, Patient(self.patientIds, patientName, allergies, tempBed))
            # Print Addmission details
            print '~~~ Admission Information ~~~\n\tHospital: {}\n\tConfirm admission for {}\n\tAssigned Bed Number: {}\n'.format(self.name, patientName, tempBed)
            # Print current patient information
            self.patients[tempBed-1].info()
        # If Hospital at Capacity then deny admission
        else:
            print '~~~ Admission Information ~~~\n\tDenied admission for {}\n\tReason: {} Hospital full\n'.format(patientName, self.name)

        return self

    # Lookup and remove patient from self.patients array
    def discharge(self, patientName):
        dischargeSuccessful = False

        for idx, patient in enumerate(self.patients):
            # if patient exist in list
            if patient.name == patientName:
                # Set Hospitals Bed Number to unoccupied (0)
                self.bed_numbers[self.patients[idx].bed_num] = 0
                # Print discharge information
                print "~~~ Discharge Information ~~~\n\tPatient {} has been discharged\n".format(patientName)
                # Remove Patient from self.patients list
                self.patients.pop(idx)
                # List all remaining patients in the Hospital
                self.listAllPatients()
                dischargeSuccessful = True
                break
        # If Discharge was not successful then print appropriate message
        if not dischargeSuccessful:
            print "~~~ Discharge Information ~~~\n\tPatient {} not found at {}'s Hospital\n".format(patientName, self.name)

        return self
    def listAllPatients(self):
        print '~~~ Currently Admitted Patients ~~~'
        for patient in self.patients:
            patient.info()

        return self

myHospital = Hospital('St. Claire', 10)

myHospital.admit('Chris', ['Pollen', 'Penicillin'])
myHospital.admit('Tom', ['Cats', 'Dogs'])
myHospital.admit('Harry', ['Horses', 'Trolls'])
myHospital.admit('Sally', ['Pine', 'Peanuts'])
myHospital.admit('Tammy', ['Eggs', 'Milk'])
myHospital.admit('Mark', ['Bees', 'Nuts', 'Gluten'])
myHospital.admit('Tim', ['None'])
myHospital.admit('Carrie', ['Pepper', 'Shellfish'])
myHospital.admit('Terry', ['Wheat', 'Sulfonamides'])
myHospital.admit('Berry', ['Aspirin', 'Monoclonal'])
myHospital.admit('Paul', ['Atracurium', 'Succinylcholine'])

myHospital.discharge('Bob').discharge('Mark')

myHospital.admit('Paul', ['Atracurium', 'Succinylcholine'])