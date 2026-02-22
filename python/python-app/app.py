from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                font-family: 'Arial', sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                text-align: center;
                background: white;
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                max-width: 500px;
            }
            h1 {
                color: #667eea;
                font-size: 48px;
                margin: 0 0 20px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            }
            p {
                color: #764ba2;
                font-size: 24px;
                margin: 10px 0;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello Rajesh</h1>
            <p>Welcome to Python Lab</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)