"""
εεε
"""

from flask import Flask
from flask import render_template
from random import randint

# Get words
words = []
f = open("words.txt", "r")
for i in f:
    words.append(i.strip().split("εεε"))
f.close()

# Create app
app = Flask("main")

# Return index.html by default. Will add a home page
@app.route("/")
def main():
    term = words[randint(0,len(words)-1)]
    return render_template(
        "index.html",
        word=term[0],
        translation=term[1]
        )

app.run(debug=True)