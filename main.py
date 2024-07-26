
# Import necessary modules
from flask import Flask, render_template, request
import os
from googletrans import Translator

# Create a Flask app
app = Flask(__name__)

# Sample data for Australian flashcards
flashcards = [
    {"australian": "Fair dinkum", "dutch": "Eerlijk waar"},
    {"australian": "Chuck a sickie", "dutch": "Ziekmelden"},
    {"australian": "G'day", "dutch": "Hallo"},
    {"australian": "No worries", "dutch": "Geen probleem"}
]

# Main route for the application
@app.route('/')
def index():
    return render_template('index.html', flashcards=flashcards)

# Translation route
@app.route('/translate', methods=['POST'])
def translate():
    # Get the form data
    text = request.form['text']
    
    # Create a translator object
    translator = Translator()
    
    # Translate the text
    translation = translator.translate(text, dest='nl')
    
    # Render the results page
    return render_template('results.html', translation=translation.text)

# Main driver function
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
