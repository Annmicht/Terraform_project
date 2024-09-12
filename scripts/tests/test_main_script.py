#!/usr/bin python3
"""
This is the main file for the py_cloud project. It can be used at any situation
"""
import os
from collections import ChainMap

import boto3
import pandas as pd
import requests
import toml
from dotenv import load_dotenv


def read_api(url):
    """
    Reads the API and returns the response
    """
    print("Reading the API...")
    response = requests.get(url)
    return response


def output_jobs(response, output_file_path=""):
    response = response.json()
    # the company name
    print("Building the dataframe...")
    company_list = [
        response["results"][i]["company"]["name"]
        for i in range(len(response["results"]))
    ]
    company_name = {"company": company_list}

    # the locations
    location_list = [
        response["results"][i]["locations"][0]["name"]
        for i in range(len(response["results"]))
    ]
    location_name = {"locations": location_list}
        # the job name
    job_list = [response["results"][i]["name"] for i in range(len(response["results"]))]
    job_name = {"job": job_list}


    # the job type
    job_type_list = [
        response["results"][i]["type"] for i in range(len(response["results"]))
    ]
    job_type = {"job_type": job_type_list}

    # the publication date
    publication_date_list = [
        response["results"][i]["publication_date"]
        for i in range(len(response["results"]))
    ]
    publication_date = {"publication_date": publication_date_list}
