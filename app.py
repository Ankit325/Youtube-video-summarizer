from flask import render_template, Flask,request,jsonify
import youtube as yt
import summarize as sm

app=Flask(__name__,template_folder='templates',static_folder='assets')
app.secret_key = "B99"


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/hire-me', methods=["GET","POST"])
def hire_me():
    summary=""
    if(request.method=="POST"):
        link= request.form.get("link")
        #print(link)
        subtitle=yt.get_subtitles(link)
        #print(subtitle)
        summary=sm.summary(subtitle)
        #print(summary)   
        return render_template("hire-me.html" ,summary=summary)
    return render_template("hire-me.html" ,summary=summary)


@app.route("/project-page")
def project_page():
    return render_template("project-page.html")

@app.route("/about-team")
def about_team():
    return render_template("projects-grid-cards.html")

@app.route("/about-project")
def about_project():
    return render_template("projects-no-images.html")








if __name__ == '__main__':
    app.run(debug=True, port=80)
    