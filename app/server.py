import json
import requests
import os
import sys
from flask import Flask,jsonify
from flask import request, session, g, redirect, url_for, abort, flash, _app_ctx_stack