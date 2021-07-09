from flask import Flask
from flask import request
from flask import jsonify
import outlook

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Woaaaadrld!"

@app.route('/getOTPHotmail')
def my_route():
    mail = request.args.get('mail',type=str)
    passMail = request.args.get('passMail',type=str)
    print(mail)
    print(passMail)
    
    otpCode = outlook.apiOTPLZD(mail, passMail)
    if (len(otpCode) == 6):
        print(otpCode)
        return jsonify(status=True,otp = otpCode)
    

if __name__ == '__main__':
    app.run()
    