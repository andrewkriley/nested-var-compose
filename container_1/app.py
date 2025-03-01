from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()
    os_variable1 = os.getenv('TZ', 'Default Value 1')
    os_variable2 = os.getenv('LANG', 'Default Value 2')
    os_variable3 = os.getenv('NFSSERVER', 'Default Value 3')
    os_variable4 = os.getenv('GROUP1', 'Default Value 4')

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
        <p><strong>OS Variable 1:</strong> {os_variable1}</p>
        <p><strong>OS Variable 2:</strong> {os_variable2}</p>
        <p><strong>OS Variable 3:</strong> {os_variable3}</p>
        <p><strong>OS Variable 4:</strong> {os_variable4}</p>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)