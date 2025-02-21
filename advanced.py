from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('profile')

@app.route('/profile')
def profile():
    name = "Nguyen Hoang Hiep"  
    address = "5-7 Vyazemsky, Saint Petersburg"
    gmail = "hoanghieppt2k@gmail.com" 
    phone = "+7(931)358-23-89"
    return render_template('advanced.html', name=name, address=address, gmail=gmail, phone=phone)
if __name__ == '__main__':
    app.run(debug=True, port=5000)