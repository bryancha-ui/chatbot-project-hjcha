# -*- coding: utf-8 -*-
from unittest import result
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2
import database

app = Flask(__name__)

@app.route("/")
def hello():
    database.db_create()
    return "Verson : 97"

@app.route("/api/hello")
def test():
    req = request.get_json()
    response = {
        "version" : "2.0",
        "template": {
            "outputs" : [
                {
                    'simpleText':{
                        "text": "안녕하세요"
                    }
                }
            ]
        }
    }


@app.route("/api/qwerasdf")
def qwerasdf():
    req = request.get_json()
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "민간분양 일반공급 유형",
                        "buttons": [
                            {
                                "action": "block",
                                "label": "순위요건",
                                "blockId": "62f5df6f70055f434dcd05ed"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return response
