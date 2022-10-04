from fastapi import FastAPI, Form, UploadFile, File
import uvicorn #server to run fastAPI
from extractor import extract#the function that will carry out extraction
import uuid #used to give unique id to each file path
import os #used to delete file after data extraction

app = FastAPI() #fastAPI instance created

@app.post("/extract_from_doc") #end point, FastAPI instance (app) post the user file here
def extract_from_doc(file_format: str =Form(...) ,
                     file: UploadFile =File(...)):
#in above str is the data type and 'Form' is default
#similarly UploadFile is the data type and File is the default, both cases default is empty

    content = file.file.read()


#Above file provided by user is read in byte and be stored temporarily in content
    #file_path = "../uploads/text.pdf"
#above commented file_path cannot be text.pdf because several users may call the functions at a time
#THEREFORE we create unique file path for each call using uuid
    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf"

    with open(file_path, "wb") as f:
        f.write(content)

    try:
        data= extract(file_path,file_format)
    except Exception as e:
        data = {
            'error': str(e)
        }
    if os.path.exists(file_path): # used to remove file after extraction
        os.remove(file_path)

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)