from flask import Flask, render_template
import chess.js

app = Flask(__name__)
chess_engine = chess.js.Chess()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
