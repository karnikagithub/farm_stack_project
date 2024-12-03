from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from indents.core import indent_router
from masters.core import masters_router

## APP Object
app = FastAPI(
    title="FastAPI & React Project, Inventory Management",
    description="Inventory Management ERP",
    summary="Summary can be about application",
    version="0.0.1",
    contact={
        "name":"ERP suite",
        "url":"url",
        "email":"email",
    },
    license_info={
        "name":"Unicorn 1.0",
        "identifier":"ERP inventory",
    },

)


## meaning backend will listen & respond to these url
origins = ["https://localhost:3000"]



## adding middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


## create a basic route
@app.get("/")
def read_root():
    return {'ping':'pong'}


app.include_router(indent_router, prefix="/indents", tags=["Manage Indents"])
app.include_router(masters_router, prefix="/masters", tags=["Manage Masters"])