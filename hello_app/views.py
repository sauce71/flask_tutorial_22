from datetime import datetime, date
from flask import Flask, render_template, redirect, request, url_for
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route("/form", methods=['GET'])
def form():

    #TODO: Legg inn en standardverdi for Bruker Id
    #TODO: Legg inn at dato er ferdig utfylt med dagens dato
    #TODO: Sett Vestre Valøs som standard verdi 
    #TODO: Sett Skifjell som standardverdi

    # Setter opp default verdie
    destination = 1
    visit_date = date.today()
    start_place = 2

    #return render_template("form.html", destination=destination)
    # Bruker **locals() fro å slippe å skrive alle variablene som parameter
    return render_template("form.html", **locals())


@app.route("/form/post", methods=['POST'])
def form_post():
    user_id = request.form['user_id']
    visit_date = request.form['visit_date']
    destination = request.form['destination']
    start_place = request.form['start_place']
    
    print(user_id)
    print(visit_date)

    #TODO: Lagre data i en kommaseparert fil
    #TODO: lagre også datetime.now() i filen (Tidspunktet du registrer data)

    return redirect(url_for('form'))