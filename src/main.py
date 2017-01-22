##need to run the server flask while the main.py file is configured as the FLASK_APP
##go to cmd as admin, and set nex environment variable setx FLASK_APP main.py
##go to cmd redirect to flask located at C:\Python27\Scripts
##and run flask:
# C:\Python27\Scripts>flask run
#  * Serving Flask app "src.main"
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#
##the server is running...
## you can go to http://127.0.0.1:5000/ and see it happens
##NOTE: must be a simple way to run it from intellij terminal, maybe there is plugin(?)



from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/",methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return 'you are using GET'
    else:
        return 'you are using POST'

if __name__ == "main":
    app.run()
