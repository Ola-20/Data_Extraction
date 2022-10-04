import re
pattern_dict = {
            'patients_name':{'pattern':'Name:(.*)Date', 'flags':0},
            'patients_address': {'pattern': 'Address:(.*)', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill:', 'flags': re.DOTALL},
            'refill': {'pattern': 'Address: (.*)', 'flags': 0}

        }
part = pattern_dict.get('patients_address')['pattern']
print(part)