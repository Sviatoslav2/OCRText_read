import traceback
from typing import List
from fastapi import FastAPI, File, UploadFile
from paddle_script import extract_paddle_result

app = FastAPI()

@app.post("/processimage/")
async def create_upload_file(file: UploadFile):
    print("Trying to process file: {}".format(file.filename))
    try:
        contents = await file.read()
        with open(f"tmp.{file.filename.split('.')[1]}", "wb") as f:
            f.write(contents)
        return {"results": extract_paddle_result(f"tmp.{file.filename.split('.')[1]}")}
    except Exception as e:
        return {
            "error": "Unhandled Internal Server Error. Please send request data to atarasov@binariks.com",
            "details": {"exceptionType": str(type(e)), "args": str(e)},
            "traceback": traceback.format_exc()
            }


@app.post("/files/")     
async def create_upload_files(files: List[UploadFile]):
    res = []
    for file in files:
        print("Trying to process file: {}".format(file.filename))
        try:
            contents = await file.read()
            with open(f"tmp.{file.filename.split('.')[1]}", "wb") as f:
                f.write(contents)
            res.append({"filename":file.filename, "results": extract_paddle_result(f"tmp.{file.filename.split('.')[1]}")})
        except Exception as e:
            res.append({"filename":file.filename,
                        "error": "Unhandled Internal Server Error. Please send request data to atarasov@binariks.com",
                        "details": {"exceptionType": str(type(e)), "args": str(e)},
                        "traceback": traceback.format_exc()
                        })
    return res            