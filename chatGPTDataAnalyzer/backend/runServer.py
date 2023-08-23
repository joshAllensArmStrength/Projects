import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from csvAnalyzer import csvAnalyzer

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
CORS(app)

@app.route('/')
def index():
    return render_template('front-end.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'csvFile' not in request.files:
        return jsonify(error='No file uploaded'), 400

    file = request.files['csvFile']
    filename = file.filename
    file.save(os.path.join('uploads', filename))

    # Now with csv file received, create csvAnalyzer class to parse csv file and send to gpt
    csv_analyzer_instance = csvAnalyzer(os.path.join('uploads', filename))
    print("Reaching out to Chat Gpt...")
    analysis_result = csv_analyzer_instance.get_gpt_response()
    print(analysis_result)

    # Return the analysis result as a response to the front end
    return jsonify(result=analysis_result), 200

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.mkdir('uploads')

    # Specify the host and port for the Flask server
    host = '127.0.0.1'  # localhost
    port = 8000

    app.run(host=host, port=port, debug=True)