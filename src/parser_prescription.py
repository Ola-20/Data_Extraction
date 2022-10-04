import re
from backends_test.src.parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patients_name' : self.get_field('patients_name'),
            'patients_address' : self.get_field('patients_address'),
            'medicines' : self.get_field('medicines'),
            'directions' : self.get_field('directions'),
            'refill' : self.get_field('refill')
        }
    def get_field(self, field_name):

        pattern_dict = {
            'patients_name':{'pattern':'Name:(.*)Date', 'flags':0},
            'patients_address': {'pattern': 'Address:(.*)', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill:', 'flags': re.DOTALL},
            'refill': {'pattern': 'Refill:(.*)times', 'flags': 0}

        }
        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()
        # if field_name == 'patients_name':
        #     pattern = 'Name:(.*)Date'
        # elif field_name == 'patients_address':
        #     pattern = 'Address:(.*)'
        # elif field_name == 'medicines':
        #     pattern = 'Address[^\n]*(.*)Directions'
        #     falgs = re.DOTALL
        # elif field_name == 'directions':
        #     pattern = 'Directions:(.*)Refill:'
        #     falgs = re.DOTALL
        # elif field_name == 'refill':
        #     pattern = 'Refill:(.*)times'

        # matches = re.findall(pattern, self.text, flags)
        # if len(matches) > 0:
        #     return matches[0].strip()

if __name__ == '__main__':
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''





    pp = PrescriptionParser(document_text)
    print(pp.parse())
