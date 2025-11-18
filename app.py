from flask import Flask, request, jsonify, render_template
from nlp_parser import parse_message
from workflow import handle_intent

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def message():
    data = request.json
    text = data.get('text', '')
    user_id = data.get('user_id', 1)

    parsed = parse_message(text)
    result = handle_intent(user_id, parsed)

    return jsonify(result)

if _name_ == '_main_':
    app.run(debug=True)
