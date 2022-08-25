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
                            "imageUrl": "https://github.com/bryancha-ui/chatbot-project-hjcha/blob/main/app/image/KakaoTalk_%EC%9D%BC%EB%B0%98%EB%B6%84%EC%96%91%20%EB%AF%BC%EA%B0%84.png"
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
                            "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
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

