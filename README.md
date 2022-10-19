# Medical Information Extraction 

The problem revolves around the extraction of important data from pdf documents which can be used for analysis.

Note: Important folders in this directory includes src, resources, and test. src contains the codes for this program and it has readme to understand its' files

## Problem Statement

A company that deals with processing of patients’ health information gets these documents in pdf form from respective branches of the hospital. These agency needs to be able to extract information from these documents so that financial claims and analytics can be done on the extracted data. The extraction is done manually which result in the following issues:
1)	Several staff member is needed
2)	The process is slow and not easily scalable
3)	It involves several financial expenses

## Proposed Solution

The proposed solution involves the development of a program that is capable of extracting important text information from pdf files of patients in an hospital. A built FastAPI was included which will allow third party software to consume the extracted field or exported via JSON format and imported into excel for analysis

## Key Steps

•	Three different patients’ documents type would be passed into the program for information extraction. The information extracted for each of the documents vary depending on the document type

•	The pdf file is converted to an image document using pdf2image python module. The image was made clearer using OpenCV module.

•	Using pytesseract which is an Optical character recognition (OCR) module, the text from the respective pdf file was extracted 

•	Consequently, the respective needed data was extracted using regular expression (regex)

•	This data can be retrieved via an incorporated FastAPI into the in-house software that will consume the data. It can also be accessed using “postman” API testing software and then exported as a JSON file. These files can be imported in excel and used for analysis.






Sample of patient’s “invoice” document extraction
 
![image](https://user-images.githubusercontent.com/71553115/194100600-e136a4f2-192f-4727-91bd-4cb46f985264.png)












Sample of “Prescription” pdf document for a patient
 
![image](https://user-images.githubusercontent.com/71553115/194100731-d1c17df9-5ae0-4ca7-862b-e43e8acd9cef.png)




## Conclusion

This extraction can be used for multiple pdf document of specific type and either consumed once at a time by the in-house software or exported into excel file for further data analysis.

Ola Akinbola: Data Scientist | Data Analyst

(Open to Opportunities)

