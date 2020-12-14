from flask import Flask, render_template

#########Migrations#############
app = Flask(__name__)

# ******************************************************
@app.route("/basic_flask")
@app.route("/")
def basic_flask():
    print(f"flask is running")
    return "this is on gnt.tw:5006"