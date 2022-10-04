import re
from backends_test.src.parser_generic import MedicalDocParser

class PatientsInvoiceParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patients_name': self.get_field('patients_name'),
            'purchase_order_no': self.get_field('purchase_order_no'),
            'order_date': self.get_field('order_date'),
            'patients_address': self.get_field('patients_address'),
            'phone_number': self.get_field('phone_number'),
            'order_amount': self.get_field('order_amount')


        }

    # def get_patients_name(self):
    #     pattern = "Name (.*)"
    #     matches = re.findall(pattern, self.text)
    #     if len(matches) > 0:
    #         return matches[0].strip()
    #
    # def get_purchase_order_no(self):
    #     pattern = "Customer's Purchase ([a-zA-Z0-9]*)"
    #     matches = re.findall(pattern, self.text)
    #     if len(matches) > 0:
    #         return matches[0].strip()
    #
    # def get_order_date(self):
    #     pattern = "Date (.*)"
    #     matches = re.findall(pattern, self.text)
    #     if len(matches) > 0:
    #         return matches[0].strip()
    #
    # def get_patients_address(self):
    #     pattern = "Address (.*?)Phone"
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches) > 0:
    #         return matches[0].strip()
    #
    # def get_phone_number(self):
    #     pattern = "Phone: (\+\d*) email"
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches) > 0:
    #         return matches[0].strip()
    #
    # def get_order_amount(self):
    #     pattern = "a Total \|(.*)"
    #     matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(matches) > 0:
    #         return matches[0].strip()

#THE CODE ABOVE CAN BE REFACTORED TO THE ONE BELOW WHICH WILL BE FURTHER REFACTORED

    # def get_field(self, field_name):
    #     pattern = ''
    #     flags = 0
    #     if field_name == 'patients_name':
    #         pattern = "Name (.*)"
    #     elif field_name == 'purchase_order_no':
    #         pattern = "Customer's Purchase ([a-zA-Z0-9]*)"
    #     elif field_name == 'order_date':
    #         pattern = "Date (.*)"
    #     elif field_name == 'patients_address':
    #         pattern = "Address (.*?)Phone"
    #         flags = re.DOTALL
    #     elif field_name == 'phone_number':
    #         pattern = "Phone: (\+\d*) email"
    #         flags = re.DOTALL
    #     elif field_name == 'order_amount':
    #         pattern = "a Total \|(.*)"
    #         flags = re.DOTALL
    #
    #     matches = re.findall(pattern, self.text, flags)
    #     if len(matches) > 0:
    #         return matches[0].strip()

#WE FURTHER REFACTOR THE ABOVE TO GIVE A MORE COMPACT ONE BELOW
    def get_field(self, field_name):

        pattern_dict= {
            'patients_name': {'pattern': 'Name (.*)', 'flag': 0},
            'purchase_order_no': {'pattern': "Customer's Purchase ([a-zA-Z0-9]*)", 'flag': 0},
            'order_date': {'pattern': 'Date (.*)', 'flag': 0},
            'patients_address': {'pattern': "Address (.*?)Phone", 'flag': re.DOTALL},
            'phone_number': {'pattern': 'Phone: (\+\d*) email', 'flag': re.DOTALL},
            'order_amount': {'pattern': 'a Total \|(.*)', 'flag': re.DOTALL}
        }
        pattern_object = pattern_dict.get(field_name)
        matches = re.findall(pattern_object['pattern'], self.text, pattern_object['flag'])
        if len(matches) > 0:
            return matches[0].strip()


if __name__ == '__main__':
    document_text = '''
        Website | Email Address

Phone 000-000-0000

Customer's Purchase 001A

Order No. — Date 12/05/2022

Name Ola Joshua

Address 105 James Ave, K6H1A3

Phone: +12254446543 email: — olaj@gmail.com
DESCRIPTION AMOUNT

Panadol Extra 300CAD

Tax | 40CAD

a Total | 340CAD
        '''

    doc = PatientsInvoiceParser(document_text)
    print(doc.get_field('order_date'))