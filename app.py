"""Movie Quotes - A simple Flask app that displays random movie quotes."""

import random
from flask import Flask, render_template

app = Flask(__name__)

QUOTES = [
    {"quote": "Life is like a box of chocolates.", "movie": "Forrest Gump", "year": 1994},
    {"quote": "To infinity and beyond\!", "movie": "Toy Story", "year": 1995},
    {"quote": "After all, tomorrow is another day.", "movie": "Gone with the Wind", "year": 1939},
    {"quote": "Just keep swimming.", "movie": "Finding Nemo", "year": 2003},
    {"quote": "Why so serious?", "movie": "The Dark Knight", "year": 2008},
    {"quote": "I'll be back.", "movie": "The Terminator", "year": 1984},
    {"quote": "May the Force be with you.", "movie": "Star Wars", "year": 1977},
    {"quote": "Here's looking at you, kid.", "movie": "Casablanca", "year": 1942},
    {"quote": "Roads? Where we're going we don't need roads.", "movie": "Back to the Future", "year": 1985},
    {"quote": "Carpe diem. Seize the day.", "movie": "Dead Poets Society", "year": 1989},
    {"quote": "Adventure is out there\!", "movie": "Up", "year": 2009},
    {"quote": "With great power comes great responsibility.", "movie": "Spider-Man", "year": 2002},
    {"quote": "It's not who I am underneath, but what I do that defines me.", "movie": "Batman Begins", "year": 2005},
]


@app.route("/")
def index():
    """Display a random movie quote."""
    quote = random.choice(QUOTES)
    return render_template("index.html", quote=quote)


@app.route("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
