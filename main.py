from flask import Flask, request, abort
from modules.ChatGPT_modules import CPTServer

app = Flask(__name__)
cptserver = CPTServer()

ALLOWED_IPS = ['127.0.0.1']

@app.route('/ask', methods=['POST'])
def ask():
    # Check if the requester's IP address is allowed
    if request.remote_addr not in ALLOWED_IPS:
        abort(403)

    # Get the prompt from the POST request
    prompt = request.form.get('prompt')
    if not prompt:
        abort(400, 'Missing prompt in POST request')

    # Process the prompt here...
    cptserver.ask(prompt)

    # Return a response
    return 'Prompt received and processed'

if __name__ == '__main__':
    app.run(debug=True)