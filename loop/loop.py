from flask import Flask
from flask.templating import render_template
app=Flask(__name__)
@app.route('/')
def index():
    langs=['C','CPP','JAVA','PYTHON','PHP','ORACLE','Flask']
    return render_template('languges.html',langs=langs)

if __name__=='__main__':
    app.run(port=8888)



