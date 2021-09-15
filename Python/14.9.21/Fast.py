# from fastapi import FastAPI
# from enum import Enum
# app = FastAPI()
# class AvailableGirls(str, Enum):
#     tamil = "tamil"
#     golti = "golti"
#     banglore ="banglore"
# girls_name = { 'tamil' : [ "Muthupriya","Narmatha" ],
#                'golti' : [ "Geetha","Gayathri"],
#                'banglore' : [ "Manisha"]
# }
# valid_girls = girls_name.keys()
# @app.get("/get_names/{girls}")
# async def get_names(girls: AvailableGirls):
#     return girls_name.get(girls)