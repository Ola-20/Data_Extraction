import re
from backends_test.src.parser_generic import MedicalDocParser

class PrescriptionPerser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    # def parse(self):
    #     return {
    #         'patients_name' : self.get_name(),
    #         'patients_address' : self.get_address('patients_address'),
    #         'medicines' : self.get_medicines('medicines'),
    #         'directions' : self.get_directions('directions'),
    #         'refill' : self.get_refill('refill')
    #     }

    # def get_name(self):
    #     pattern = 'Name:(.*)Date'
    #     matches = re.findall(pattern, self.text)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    #
    # def get_address(self):
    #     pattern = 'Address:(.*)'
    #     matches = re.findall(pattern, self.text)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_medicines(self):
    #     pattern = 'Address[^\n]*(.*)Directions'
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches)>0:
    #         return matches[0].strip()
    #
    # def get_direction(self):
    #     pattern = 'Directions:(.*)Refill:'
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches) > 0:
    #         return matches[0].strip()
    #
    # def get_refill(self):
    #     pattern = 'Refill:(.*)times'
    #     matches = re.findall(pattern, self.text)
    #     if len(matches) > 0:
    #         return matches[0].strip()

#'''
#THE ABOVE COMMENTED CODE WILL WORK FINE BUT VIA REFRACTORING, WE REDUCE IT TO THAT BELOW'''
    def parse(self):
        return {
            'patients_name' : self.get_field('patients_name'),
            'patients_address' : self.get_field('patients_address'),
            'medicines' : self.get_field('medicines'),
            'directions' : self.get_field('directions'),
            'refill' : self.get_field('refill')
        }

    def get_field(self, field_name):
        pattern=''
        flags=0

        if field_name == 'patients_name':
            pattern = 'Name:(.*)Date'
        elif field_name == 'patients_address':
            pattern = 'Address:(.*)'
        elif field_name == 'medicines':
            pattern = 'Address[^\n]*(.*)Directions'
            falgs = re.DOTALL
        elif field_name == 'directions':
            pattern = 'Directions:(.*)Refill:'
            falgs = re.DOTALL
        elif field_name == 'refill':
            pattern = 'Refill:(.*)times'
        matches = re.findall(pattern, self.text, flags)
        if len(matches) > 0:
            return matches[0].strip()
#THE ABOVE IF CONDITION CAN EVEN BE CODED BETTER BY USING DICTIONARY, since it is only returning content in "pattern"
        # variable(container). This is exactly what keys do in dictionary
        # HENCE WE REFACTOR THE CODE BELOW:
        # REMOVE THE COMMENT TO RUN IT AFTER COMMENTING OUT THE IF ABOVE



        #  pattern_dict = {
        #     'patients_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
        #     'patients_address': {'pattern': 'Address:(.*)', 'flags': 0},
        #     'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
        #     'directions': {'pattern': 'Directions:(.*)Refill:', 'flags': re.DOTALL},
        #     'refill': {'pattern': 'Address: (.*)', 'flags': 0}
        #
        # }
        #
        # pattern_object = pattern_dict.get(field_name)
        # if pattern_object:
        #     matches = re.findall(pattern_object['pattern'], self.text, pattern_object['flags'])
        # if len(matches) > 0:
        #     return matches[0].strip()




if __name__ == '__main__':
    document_text = '''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC
    
    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks -
    Lialda - take 2 pill everyday for 1 month
    Refill: 3 ti
    '''

docs = PrescriptionPerser(document_text)
print(docs.parse())
