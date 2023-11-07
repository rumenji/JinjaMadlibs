from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = '12fdgfg'

# debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)
    

@app.route('/story')
def story_route():
    madlib = story.generate(request.args)
    return render_template('story.html', madlib=madlib)
    