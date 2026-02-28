from flask import Flask, request, jsonify, render_template
import sys
from io import StringIO
import re
import os

# Your existing Interpreter class remains the same
class Interpreter:
    # ... (keep all your existing interpreter code)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        interp = Interpreter()
        interp.run(code)
        output = redirected_output.getvalue()
    except Exception as e:
        output = str(e)
    finally:
        sys.stdout = old_stdout
    return jsonify({'output': output})

if __name__ != '__main__':
    # When running on Gunicorn, don't use the built-in server
    pass

if __name__ == '__main__':
    # For local development only
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
