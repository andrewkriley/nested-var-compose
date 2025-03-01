from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()
    globalvar1 = os.getenv('GLOBALVAR1', 'Default Value 1')
    globalvar2 = os.getenv('GLOBALVAR2', 'Default Value 2')
    localvar1 = os.getenv('LOCALVAR1', 'Default Value 3')
    localvar2 = os.getenv('LOCALVAR2', 'Default Value 3')

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hostname and OS Variables</title>
    </head>
    <body>
        <h1>Server Information</h1>
        <p><strong>Hostname:</strong> {hostname}</p>
        <p><strong>OS Variable 1:</strong> {globalvar1}</p>
        <p><strong>OS Variable 2:</strong> {globalvar2}</p>
        <p><strong>OS Variable 3:</strong> {localvar1}</p>
        <p><strong>OS Variable 3:</strong> {localvar2}</p>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


