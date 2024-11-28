import uvicorn
from fastapi import FastAPI, Request
import runpy
import os


app = FastAPI()


# @app.get('/{code}')
# def getall(code):
#     with open('code1.py', 'w', encoding='utf8') as f:
#         f.write(code)
#     try:
#         runpy.run_module(mod_name="code1")
#     except :
#         return TypeError
#     else:
#         return 200

@app.get('/')
def getall(request: Request):
    req = request.headers.get('code')

    try:
        with open('code1.py', 'w', encoding='utf8') as f:
            f.write(req)
        runpy.run_module(mod_name="code1")
        os.remove('code1.py')
        return 200
    except Exception as a:
        return str(a)
    else:
        return '500'


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=5658)