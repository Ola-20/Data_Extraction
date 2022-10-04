from pdf2image import convert_from_path
import pytesseract
import util

#These two imported classes were used to extract needed information after tesseract had
#extracted raw text

from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser
from parser_invoice import PatientsInvoiceParser

POPPLER_PATH = r'C:\poppler-22.04.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#To get a clear image we will create a function which use OPenCV adaptive thressholding for our image
# Simple thressholding will not be good enough for us as explained in the file cv_concept

from PIL import Image                #module that will display the picture

#Extract function below (1) gets pdf file convert it to image,
#(2) calls the util.preprocess_image method and processes the image for clarity
#(3)uses pytesseract to extract text and return the document text
def extract(file_path, file_format):
    #extract infomation from pdf file
    pages = convert_from_path(file_path, poppler_path=r'C:\poppler-22.04.0\Library\bin')

    document_text = ''
    for page in pages:
        processed_image = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = document_text + '\n' + '\n' + text
        #mistake at 12:06mins project/module 4:  video 7
        #teacher forgets to put document_text for loop hence only one page returned

    if file_format == 'prescription':
        extracted_info = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_info = PatientDetailsParser(document_text).parse()
    elif file_format == 'patient_invoice':
        extracted_info = PatientsInvoiceParser(document_text).parse()
    else:
        raise Exception(f"You supplied invalid format {file_format}, expected 'prescription' or 'patient_details'")

    return extracted_info




if __name__ == '__main__':
    # data = extract('../resources/patient_details/pd_2.pdf', 'patient_details')
    # print(data)
    data = extract('../resources/invoice/invoices.pdf', 'patient_invoice')
    print(data)