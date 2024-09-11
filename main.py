from flask import Flask, render_template_string
import random

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Случайный код</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .container {
            text-align: center;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 2.5rem;
            color: #333;
        }
        p {
            font-size: 1.5rem;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ваш случайный код</h1>
        <p>{{ code }}</p>
    </div>
</body>
</html>
'''

@app.route('/')
def generate_code():
    code = random.randint(1000, 9999)
    return render_template_string(html_template, code=code)

if __name__ == '__main__':
    app.run(debug=True)
