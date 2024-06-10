from flask import Flask

app = Flask(__name__)

@app.route('/run_script')
def run_script():
    # Execute your Python script here
    # Example:
    import subprocess
    subprocess.call(['python', 'your_script.py'])
    
    return 'Python script executed successfully.'

if __name__ == '__main__':
    app.run()
