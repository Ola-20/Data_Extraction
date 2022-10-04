#The comment/explanation for this code can be found in the jupyter notebook
#Detail parser and prescription parser
#The code here needs to be refactored
import re
from backends_test.src.parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patients_name':self.get_patient_name(),
            'patients_phone':self.get_patient_phone(),
            'hepatitis_vacination':self.get_hepatitis_vacination_status(),
            'medical_problems':self.get_medical_problem()
        }
    def get_patient_name(self):
        pattern = 'Birth Date.*?([a-zA-Z]\D+)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            match = matches[0].strip()

        month_pattern = '(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|sep|Oct|Nov|Dec)'
        date = re.findall(month_pattern, match)
        if date:
            date = date[0]

        name = match.replace(date, '').strip()
        return name

    def get_patient_phone(self):
        pattern = 'Patient Information.*?(\(\d{3}\).\d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            patient_phone = matches[0].strip()
        return patient_phone

    def get_hepatitis_vacination_status(self):
        pattern = 'vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            hepatitis_vacination = matches[0].strip()
        return hepatitis_vacination

    def get_medical_problem(self):
        pattern = 'headaches.*?:(.*\D+)'
        matches = re.findall(pattern, self.text)
        if matches:
            med_prob = matches[0].strip()
        return med_prob
if __name__ =='__main__':
    document_text = '''
        17/12/2020
    
    Patient Medical Record
    
    Patient Information Birth Date
    
    Kathy Crawford May 6 1972
    
    (737) 988-0851 Weight’
    
    9264 Ash Dr 95
    
    New York City, 10005 '
    
    United States Height:
    190
    
    In Case of Emergency
    ee J
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History
    nn ee
    Chicken Pox (Varicella): Measies:
    IMMUNE
    
    IMMUNE
    Have you had the Hepatitis B vaccination?
    
    No
    
    List any Medical Problems (asthma, seizures, headaches):
    
    Migraine
        '''

    doc = PatientDetailsParser(document_text).parse()
    print(doc)