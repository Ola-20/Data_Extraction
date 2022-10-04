from backends.src.parser_patient_details import PatientDetailsParser
import pytest

@pytest.fixture()
def doc_1_kathy():
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
    return PatientDetailsParser(document_text)

@pytest.fixture()
def doc_2_jerry():
    document_text = '''
    Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

- eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

    '''
    return PatientDetailsParser(document_text)




def test_get_patient_name(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_patient_name() == 'Kathy Crawford'
    assert doc_2_jerry.get_patient_name() == 'Jerry Lucas'

def test_get_patient_phone(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_patient_phone() == '(737) 988-0851'
    assert doc_2_jerry.get_patient_phone() == '(279) 920-8204'

def test_get_hepatitis_vacination_status(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_hepatitis_vacination_status() == 'No'
    assert doc_2_jerry.get_hepatitis_vacination_status() == "Yes"

def test_get_medical_problem(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_medical_problem() == 'Migraine'
    assert doc_2_jerry.get_medical_problem() == "N/A"