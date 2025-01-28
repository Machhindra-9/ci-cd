from flask import Flask, render_template_string

app = Flask(__name__)

# HTML templates for each page
templates = {
    "home": "<h1>Home Page</h1><p>Welcome to the Home Page!</p><a href='/about'>Go to About</a>",
    "about": "<h1>About Page</h1><p>This is the About Page.</p><a href='/services'>Go to Services</a>",
    "services": "<h1>Services Page</h1><p>These are our Services.</p><a href='/contact'>Go to Contact</a>",
    "contact": "<h1>Contact Page</h1><p>Contact us here!</p><a href='/faq'>Go to FAQ</a>",
    "faq": "<h1>FAQ Page</h1><p>Frequently Asked Questions.</p><a href='/'>Go to Home</a>",
}

# Routes for each page
@app.route('/')
def home():
    return render_template_string(templates["home"])

@app.route('/about')
def about():
    return render_template_string(templates["about"])

@app.route('/services')
def services():
    return render_template_string(templates["services"])

@app.route('/contact')
def contact():
    return render_template_string(templates["contact"])

@app.route('/faq')
def faq():
    return render_template_string(templates["faq"])

if __name__ == '__main__':
    app.run(debug=True)
