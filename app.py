from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>서버가 html도 보내주나???</h1>"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>첫번째 줄!!!</h1>
    <h2>두번째 줄!!</h2>
    """

@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", people=name)
    
@app.route("/cube/<int:num>")
def cube(num):
    triple = num*num*num
    return render_template("cube.html",triple=triple,num=num)
    
@app.route('/lunch')
def lunch():
    # 요부분에 점심메뉴를 추천해주는 코드를 작성!
    menu_list = ["삼겹살","피자","치킨"]
    pick = random.choice(menu_list)
    return render_template("lunch.html",pick=pick)

@app.route('/lotto')    
def lotto():
    numbers = range(1,46)
    pick = random.sample(numbers,6)
    sort_pick = sorted(pick)
    return render_template("lotto.html",sort_pick=sort_pick)

@app.route('/google')
def goolge():
    return render_template("google.html")