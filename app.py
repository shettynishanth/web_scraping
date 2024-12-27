from flask import Flask, render_template
import threading
from selenium_script import run_selenium_script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    # Create a new thread to run the Selenium script
    threading.Thread(target=run_selenium_script).start()
    return "Script is running..."

if __name__ == '__main__':
    app.run(debug=True)
