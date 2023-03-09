from flask import Flask, request, abort, jsonify
from modules.ChatGPT_modules import CPTServer
from loguru import logger


app = Flask(__name__)
cptserver = CPTServer()

ALLOWED_IPS = ['127.0.0.1', '104.168.202.148']

@app.route('/ask', methods=['POST'])
def ask():
    # Check if the requester's IP address is allowed
    if request.remote_addr not in ALLOWED_IPS:
        logger.warning(request.remote_addr)
        abort(403)

    # Get the prompt from the POST request
    prompt = request.form.get('prompt')
    if not prompt:
        logger.error("mis prompt")
        abort(400, 'Missing prompt in POST request')

    # Get the prompt from the POST request
    conversation_id = request.form.get('conversation_id')

    # Process the prompt here...
    res, conversation_id = cptserver.ask(prompt=prompt,
                                         conversation_id=conversation_id)

    # Return a response
    return res['choices'][0]['message']['content']

@app.route('/', methods=['GET'])
def home():
    # Check if the requester's IP address is allowed
    if request.remote_addr not in ALLOWED_IPS:
        logger.warning(request.remote_addr)
        abort(403)

    return 'HELLO'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
