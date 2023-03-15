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
        return "No response"

    # Get the conversation_id from the POST request
    conversation_id = request.form.get('conversation_id')

    # Get the if_continue_prev_conv from the POST request
    if_continue_prev_conv = request.form.get('if_continue')

    logger.debug(request.form)

    # Process the prompt here...
    res, conversation_id = cptserver.ask(prompt=prompt,
                                         conversation_id=conversation_id,
                                         if_continue_prev_conv=True,
                                         if_human_mode=True)

    # Return a response
    return res['choices'][0]['message']['content']
@app.route('/clear', methods=['GET'])
def clear():
    # Check if the requester's IP address is allowed
    if request.remote_addr not in ALLOWED_IPS:
        logger.warning(request.remote_addr)
        abort(403)

    cptserver.clear_prev()
    return 'Cleared'

@app.route('/', methods=['GET'])
def home():
    # Check if the requester's IP address is allowed
    if request.remote_addr not in ALLOWED_IPS:
        logger.warning(request.remote_addr)
        abort(403)

    return 'HELLO'

@app.route('/diyAsk', methods=['POST'])
def diy_ask():
    if request.remote_addr not in ALLOWED_IPS:
        logger.warning(request.remote_addr)
        abort(403)
    messages = request.json.get("messages")
    res = cptserver.diy_ask(messages=messages)
    return res['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
