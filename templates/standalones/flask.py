# IMPORTS
from flask import Flask, render_template, send_file, url_for

# APP INIT
app = Flask(__name__)

# DB INIT


# SETTINGS


# FUNCTIONS


# PAGES INIT
@app.route("/")
def homePage():
    pass

# APP BOOT
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5500)
