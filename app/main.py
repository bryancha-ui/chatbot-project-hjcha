# -*- coding: utf-8 -*-
from unittest import result
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    return "Verson : 97"

@app.route("/api/hello", methods = ['POST'])
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
    return response


@app.route("/api/qwerasdf", methods = ['POST'])
def qwerasdf():
    req = request.get_json()
    print(req)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "민간분양 일반공급 유형",
                        "thumbnail": {
                            "imageUrl": "https://raw.githubusercontent.com/bryancha-ui/chatbot-project-hjcha/main/app/image/KakaoTalk_regular.png",
                            "width": 1200,
                            "height": 1200
                        },
                        "buttons": [
                            {
                                "action": "block",
                                "label": "순위요건",
                                "blockId": "62f5df6f70055f434dcd05ed"
                            }
                        ]
                    },
                }
            ]
        }
    }
    return response

@app.route("/api/qwerasdfd", methods = ['POST'])
def qwerasdfd():
    req = request.get_json()
    print(req)
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "thumbnail": {
                            "imageUrl": "https://raw.githubusercontent.com/bryancha-ui/chatbot-project-hjcha/main/app/image/KakaoTalk_point.png",
                            "width": 1200,
                            "height": 1200
                        },
                        "buttons": [
                            {
                                "action": "block",
                                "label": "가점제 점수계산표",
                                "blockId": "62fcf4c58a1240569898cd10"
                            }
                        ]
                    },
                }
            ]
        }
    }
    return response

