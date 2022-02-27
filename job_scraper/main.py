from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from web_scraper import scrape_listing
import urllib.request
from lxml import etree
import lxml.html
import requests


# class Job(BaseModel):
#     title: str
#     company: str
#     location: str
#     listing_url: str
#     job_desc: str


app = FastAPI()


@app.get("/")  # path operation decorator
# function right below is in charge of handling requests that go to the path / using a get operation
async def root():
    return {"message": "Welcome to our web scraper!"}


# @app.post("/info/{website}/{url_id}")
# async def create_job(website: str, url_id: int, job: Job):
#     return "hello"


@app.get("/info/{website}/{url_id}")
def get_info(website: str, url_id: int):
    if url_id == 1:
        url = 'https://www.fastjobs.sg/singapore-job-ad/1403500/finance-officer/certis-human-resource-services/'
    else:
        url = 'https://www.fastjobs.sg/singapore-job-ad/1394252/accounts-associate-fresh-grads-are/gain-city/?offset=4&source=web-jobfeed'

    return scrape_listing(website, url)
