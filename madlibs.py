from random import choice
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

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    playing = request.args.get("play")
    if playing == "no":
        return  render_template("goodbye.html")
    else: #if playing is 'yes'
        return render_template("game.html")

@app.route("/madlib")
def show_madlib():
    name = request.args.get("person_name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adj = request.args.get("adj")
    startdate = request.args.get("start_date")
    coolPic = request.args.get("image")
    cheese = request.args.get("cheese")
    rabbit = request.args.get("rabbit")
    chopsticks = request.args.get("chopsticks")

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
