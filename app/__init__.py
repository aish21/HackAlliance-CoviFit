from flask import Flask, render_template, Response, request

app = Flask(__name__)

from app import views