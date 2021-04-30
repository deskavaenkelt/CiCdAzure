import gspread
from flask import Flask, render_template, jsonify, request, abort

app = Flask(__name__)

gc = gspread.service_account(filename='shared/google-sheet.json')
sh = gc.open('flask-website')

sh_profile = sh.get_worksheet(0)
sh_contacts = sh.get_worksheet(1)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        sh_contacts.append_row([request.form['name'], request.form['email'], request.form['message']])

    profile = {
        'about': sh_profile.acell('B2').value,
        'interests': sh_profile.acell('B3').value,
        'experience': sh_profile.acell('B4').value,
        'education': sh_profile.acell('B5').value
    }

    # profile2 = jsonify(sh_profile.get_all_records())

    return render_template('index.html', profile=profile)


# An example GET Route to get all reviews
@app.route('/all', methods=["GET"])
def all_reviews():
    return jsonify(sh_profile.get_all_records())


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
