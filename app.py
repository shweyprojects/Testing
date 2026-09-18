from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Agentic Deployment Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }

            .container {
                background: white;
                padding: 45px;
                border-radius: 16px;
                box-shadow: 0 8px 30px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 650px;
                width: 90%;
            }

            .icon {
                font-size: 50px;
                margin-bottom: 15px;
            }

            h1 {
                margin-bottom: 10px;
                color: #1f2937;
            }

            p {
                color: #6b7280;
                font-size: 17px;
            }

            .status {
                margin: 25px 0;
                padding: 15px;
                background: #ecfdf5;
                color: #047857;
                border-radius: 10px;
                font-weight: bold;
            }

            .info {
                text-align: left;
                background: #f9fafb;
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
            }

            .info div {
                padding: 8px 0;
            }

            .label {
                font-weight: bold;
                color: #374151;
            }

            .footer {
                margin-top: 25px;
                font-size: 13px;
                color: #9ca3af;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <div class="icon">🚀</div>

            <h1>Agentic Deployment Demo</h1>

            <p>
                A Python Flask application deployed automatically
                using the Agentic AI Deployment Hub.
            </p>

            <div class="status">
                ✓ Application is running successfully
            </div>

            <div class="info">
                <div>
                    <span class="label">Application:</span>
                    Demo Flask Application
                </div>

                <div>
                    <span class="label">Framework:</span>
                    Flask
                </div>

                <div>
                    <span class="label">Deployment:</span>
                    Docker + Cloud
                </div>

                <div>
                    <span class="label">Status:</span>
                    Healthy
                </div>
            </div>

            <div class="footer">
                Deployed by Agentic AI Deployment Hub
            </div>

        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
