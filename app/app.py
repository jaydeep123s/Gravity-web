# Gravity-web/app/app.py

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key for session management

# Define a simple route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Define a route for the contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        
        if not name or not message:
            flash('All fields are required!')
            return redirect(url_for('contact'))
        
        # Process the contact form data here (e.g., save to database, send email)
        flash('Your message has been sent successfully!')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Define a 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Define a 500 error page
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
