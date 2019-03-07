
from flask import request, Flask, render_template
import re
app = Flask(__name__)

@app.route('/mailparser', methods=['POST','GET'])
def mailparser():
    if request.method == 'POST':
        texto_con_emails = request.form['texto_con_emails']
        emails = re.findall(r"(\w+@\w+\.\w+\.*\w*)",texto_con_emails)
        return render_template('mailparser.html', emails=emails)
    else:
        return render_template('mailparser.html')
