from flask import Flask, render_template, request
import random

import requests
from flask import Flask
#http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+3x-7%3D11&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json

class ApiData:
    def __init__(self, equation):
        self.eq = equation

        self.apiData = requests.get(f"http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+{self.formatEq()}&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json").json()

    def setEquation(self,equation):
        self.eq = equation
        self.apiData = requests.get(f"http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+{self.formatEq()}&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json").json()

    def formatEq(self):
        return self.eq.replace('=', '%3D').replace("+","%2D")

    def getAnswer(self):
        return self.apiData['queryresult']['pods'][0]['subpods'][0]['plaintext']

    def getSolAnswer(self):
        self.pop = self.apiData['queryresult']['pods'][0]['subpods'][0]['plaintext'].replace("x","")
        self.pop = self.apiData['queryresult']['pods'][0]['subpods'][0]['plaintext'].replace(" ","")
        return self.pop

    def getSolution(self):
        return str(self.apiData['queryresult'][ 'pods'][0]['subpods'][1]['plaintext']).replace("\n","  <br>  ")

listQ = ["10x+5=55", "3x+2=8","2x+5=11","20x+20=80","6x=12+3x","15=7x+1", '210=5x+10', '1=x-10', '5x+10=110']
app = Flask(__name__)
ques = listQ[random.randrange(5)]
ApData = ApiData(ques)
@app.route('/')  
def index():
    ques = listQ[random.randrange(5)]
    ApData.setEquation(ques)
    return render_template("practice.html",value = ApData.eq) 

@app.route("/checkAnswer")
def get_response():
    #if request.method == "POST":
    answer1 = request.form.get("answer")
    print("GETTTTT")
    #answer1 = request.args.get('answer')
    cAnswer = ApData.getSolAnswer()
    if (answer1 == cAnswer):
        return render_template("checkAnswer.html",value = (" Correct!" + str(cAnswer) + "is correct "))
    else:
        finalStr = "Incorrect." + "<br> The correct answer was " + str(cAnswer) + "<br>"
        try:
            finalStr += "<br> The work is shown below: \n "+"<br>"+ str(ApData.getSolution())
            return(render_template("checkAnswer.html", value = finalStr))
        except:
            return(render_template("checkAnswer.html", value = finalStr))

       # return render_template("checkAnswer.html",value = "Incorrect" + "\n The correct answer was " + str(cAnswer) + "\nThe work is shown below: \n "+ str(ApData.getSolution()))

if __name__ == "__main__":
    app.run()
"""
@app.route('/')  
def index():
    return render_template("index.html") 

@app.route("/practice")
def practice():
    ques = listQ[random.randrange(5)]
    return render_template("practice.html", value = ApData.eq)

@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/study")
def study():
    return render_template("study.html")
"""

#def getWebResponse():
 #   #userText = request.args.get("msg")








# eq = "3x+5%3D11"
# webInfo = requests.get("http://api.wolframalpha.com/v2/query?appid=YGV9XJ-RH825P558W&input=solve+3x-7%3D11&podstate=Result__Step-by-step+solution&format=plaintext&includepodid=Result&output=json")
# #print(webInfo.status_code) 200 if works 410 if not
# dictInfo = webInfo.json()

# print('\n'+dictInfo['queryresult']['pods'][0]['subpods'][0]['plaintext'])
# print('\n'+dictInfo['queryresult'][ 'pods'][0]['subpods'][1]['plaintext'])


# def getAnswer(problem, apiData):
#    return apiData['queryresult']['pods'][0]['subpods'][0]['plaintext']

# def getSolution(problem, apiData):
#     return apiData['queryresult'][ 'pods'][0]['subpods'][1]['plaintext']

