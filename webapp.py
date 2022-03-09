from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    use = request.args['use']
    brand = request.args['brand']
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    reply1 =""
    if use == "Racing" and brand == "P":
        reply1 = "You should get a Porsche GT3 RS."
    elif use == "Ad" and brand == "P":
        reply1 = "You should get a Posrche Cayanne Turbo S."
    elif use == "FC" and brand == "P":
        reply1 = "You should get a Porsche Macan GTS."
    elif use == "Racing" and brand == "BMW":
        reply1 = "You should get a BMW M4 CS."
    elif use == "FC" and brand == "BMW":
        reply1 = "You should get a BMW 5 series."
    elif use == "Ad" and brand == "BMW":
        reply1 = "You should get an BMW X8."
    elif use == "Racing" and brand == "ford":
        reply1 = "You should get a Ford GT."
    elif use == "Ad" and brand == "ford":
        reply1 = "You should get a Ford Explorer."
    elif use == "FC" and brand == "ford":
        reply1 = "You should get a Ford Fusion."


 #values in request.args are strings by default



    return render_template('response.html', response1 = reply1)

if __name__=="__main__":
    app.run(debug=True)
