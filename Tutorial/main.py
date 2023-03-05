# ----------------------------------------
# -- Flask => Intro and Your First Page --
# ----------------------------------------
# - Flask Is Micro Framework Built With Python
# --------------------------------------------


from flask import Flask , render_template


skills_app = Flask(__name__)

my_skills = [("Html", 80), ("CSS", 75), ("Python", 95), ("Django", 80)]


@skills_app.route("/")
def homepage():
    return render_template("homepage.html", 
                           title ="home Page",
                           custom_css="home"
                           )


@skills_app.route("/skills")
def skills():
    return render_template("skills.html",
                          title="My Skills",
                          page_head="My Skills",
                          custom_css="skills",
                          description="This Is My Skills Page",
                          skills=my_skills)


@skills_app.route("/add")
def add():
    return render_template('add.html',
                            title ="Add Skills",
                            custom_css="add"
                           )



@skills_app.route("/about")
def about():
    return render_template('about.html',
                           title ="About Us")



if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)



