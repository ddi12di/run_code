import uvicorn
from fastapi import FastAPI, Request
import runpy


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

    with open('code1.py', 'w', encoding='utf8') as f:
        f.write(req)
    try:
        runpy.run_module(mod_name="code1")
    except :
        return TypeError
    else:
        return 200


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=5658, reload=True)