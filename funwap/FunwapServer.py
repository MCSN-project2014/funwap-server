from flask import Flask
from flask import render_template
from flask import request
import subprocess
from subprocess import TimeoutExpired
import platform

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        dataRow = request.data.decode('utf-8')
        #print (dataRow)

        if dataRow == '' and request.form.get('json') != None:
            dataRow = request.form['json']
        elif dataRow == '':
            return 'data error'

        data = dataRow.split('&')

        if platform.system() == 'Linux':
            comand = ['mono', 'bin/funwaps.exe', data[0], data[1]]
        else:
            comand = ['bin\\funwaps.exe', data[0], data[1]]

        try:
            p = subprocess.Popen(comand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate(timeout=30)
            err = err.decode('utf-8')
            out = out.decode('utf-8')

            if err == '':
                print('result: ' + out)
                return out
            else:
                print('error: ' + err)
                return "server internal error"

        except TimeoutExpired:
            p.kill()
            return 'operation to long'

    return render_template('index.html')
