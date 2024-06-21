from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', '127.0.0.1'), port=6379)

@app.route('/')
def hello():
    # Incrementing the hit count in Redis
    redis.incr('hits')
    
    # Fetching the current hit count from Redis
    hits = redis.get('hits').decode('utf-8')
    
    # Getting the hostname of the server
    hostname = socket.gethostname()
    
    # HTML template with CSS for styling
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HitCounter</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                text-align: center;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                font-size: 2.5em;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.2em;
                margin-top: 0;
            }}
            footer {{
                margin-top: 20px;
                font-size: 0.9em;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to HitCounter!</h1>
            <p>This webpage has been viewed {hits} times.</p>
            <footer>Hostname: {hostname}</footer>
        </div>
    </body>
    </html>
    """
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
