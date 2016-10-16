from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# For debugging purposes:
app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index_page():
    """Show an index page."""
   
    return render_template("index.html")


@app.route("/application-form")
def app_form():
    """Show an application page"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application_successful():
    """Show page that lets applicant know application has been successfully 
    submitted."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary_requ = request.form.get("salary")
    position = request.form.get("position")
    return render_template("application-response.html",
                            firstname=first_name,
                            lastname=last_name,
                            salaryrequ=salary_requ,
                            position=position)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

