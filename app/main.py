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

@app.route("/api/234")
def test():
    req = request.get_json()
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "commerceCard": {
                        "description": "민간분양 우선공급 유형",
                        "thumbnails": [
                            {
                                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg",
                                "link": {
                                    "web": "https://store.kakaofriends.com/kr/products/1542"
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "순위요건",
                                "action": "webLink",
                                "webLinkUrl": "https://store.kakaofriends.com/kr/products/1542"
                            },
                        ]
                    }
                }
            ]
        }
    }
    return response