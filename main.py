from appweb import create_app
from flask import render_template
import os

app = create_app(os.environ.get('FLASK_CONFIG', None))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
