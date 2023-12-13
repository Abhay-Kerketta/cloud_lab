from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    post_data = {
        'title': 'Introduction to Cloud Computing',
        'content': 'Cloud computing is a technology that allows users to access and use computing resources (such as servers, storage, databases, networking, software) over the internet (the cloud) instead of on their own computers or local servers.',
    }
    return render_template('index.html', post=post_data)

if __name__ == '__main__':
    app.run(debug=True)