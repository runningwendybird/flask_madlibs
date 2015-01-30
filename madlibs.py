from random import choice, sample
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route('/game')
def show_game_form():
    playing = request.args.get("play")
    if playing == "no":
        return  render_template("goodbye.html")
    else: #if playing is 'yes'
        return render_template("game.html")

@app.route("/madlib", methods=['POST', 'GET'])
def show_madlib():

    name = request.values.get("person_name")
    color = request.values.get("color")
    noun = request.values.get("noun")
    adj = request.values.get("adj")
    startdate = request.values.get("start_date")
    coolPic = request.values.get("image")
    cheese = request.values.get("cheese")
    rabbit = request.values.get("rabbit")
    chopsticks = request.values.get("chopsticks")

    html_list = ["madlib.html", "madlib2.html"]
    loadpage = choice(html_list)

    check_dict = {"a block cheese": cheese, "your lucky rabbit foot": rabbit, "a pair of chopsticks": chopsticks}
    list_to_print = []

    for key in check_dict.keys():
        if check_dict[key] == 'on':
            list_to_print.append(key)

    print loadpage
    
    return render_template(loadpage, name=name, color=color, noun=noun, adj=adj, startdate=startdate, coolPic=coolPic, list_to_print=list_to_print)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
