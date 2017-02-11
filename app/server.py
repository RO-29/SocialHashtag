import json
import requests
import os
import sys
from flask import Flask,jsonify
from flask import request, session, g, redirect, url_for, abort, flash, _app_ctx_stack
import stream
import datetime
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__,static_url_path='/static')

CORS(app)


@app.route('/')
def welcome():
  return jsonify({"message":"It Works!", "status":"HTTP_200_OK"})


def getRequstParams(request):
  start_date      = request.args.get("start_date",datetime.datetime.now().strftime("%Y-%m-%d"))
  end_date        = request.args.get("end_date",(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
  insta           = request.args.get("insta",1)
  tweet           = request.args.get("tweets",1)
  mode            = {"auto":1, "manual":0}.get(request.args.get("mode","auto").lower(),1)
  location        = request.args.get("location","") 
  old_post        = int(request.args.get("old",1))
  results_number  = int(request.args.get("results_number",0))
  return start_date, end_date, insta, tweet, mode,location,old_post,results_number

sinceidTwitter = 0
sinceidInsta   = 0

@app.route('/get/posts')
def index():
  search_term = str(request.args.get("hashtag",""))
  search_term = search_term.split("#")[1] if len(search_term.split("#")) >=2  else search_term
  if not search_term:
    return jsonify({"message":"Invalid/Missing mandatory hashtag value", "status":"HTTP_400_BAD_REQUEST"})
  start_date, end_date, insta, tweet, mode,location,old_post,results_number = getRequstParams(request)
  response = {"data":[]}
  
  global sinceidTwitter, sinceidInsta
  response_twitter = []
  response_insta = []
  if tweet:
    response_twitter,sinceidTwitter = stream.StreamSocial()._getSearchResults(search_term,start_date, end_date, mode, location,"tweets", sinceidTwitter,old_post,results_number)
  if insta:
    response_insta , sinceidInsta = stream.StreamSocial()._getSearchResults(search_term,start_date, end_date, mode, location,"insta", sinceidInsta,old_post,results_number)
  response["data"]+=response_twitter + response_insta
  return jsonify(response)

if __name__=="__main__":
   app.run(host="0.0.0.0",port=int(8080),debug=True)


