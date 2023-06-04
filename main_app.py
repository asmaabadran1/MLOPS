from fastapi import FastAPI
from main import multipl_xy
from data_model import sample_data
import logging
import time

log_format = "[%(name)s][%(levelname)-6s] %(message)s"
logging.basicConfig(format=log_format)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) 
app = FastAPI()

 
@app.get("/")
def home():
    return "welcome"


@app.get("/multiply/{x, y}")
def multiply(x : int,y: int):
    return multipl_xy(x, y)

 
@app.post("/printData")
def print_data(request: sample_data):
    return request.age, request.name, request.fav_numbers
    
@app.get("/print_multiply/{c}")
def sum_xy_endpoint(c:str, a: int, b: int):
    logger.info("Recievevd request.")
    start_time = time.time()
    output = c + " " + str(multipl_xy(a, b))
    end_time = time.time()
    total_time = end_time - start_time
    logger.info(f"The processing took {total_time}s")
    logger.debug(f"Debug: Recieved {c=}, {a=}, {b=}")
    return output