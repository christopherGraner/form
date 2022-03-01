from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    deadlift = request.args['deadlift']
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if deadlift >= '315':
        reply1 = "Zyzz would be proud"
    else:
        reply1 = "Lol beta weight"
    n = int(request.args['deadlift']) #values in request.args are strings by default
    reply2 = "I like cardio"
    return render_template('response.html', response1 = reply1, response2 = reply2)

if __name__=="__main__":
    app.run(debug=False)
