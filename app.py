from flask import Flask, render_template, redirect, url_for, session, request, send_file
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.secret_key = 'SDEtw$etdsg54TY5gdrfyh%$yrthfdy$%^#$%23'  # Replace with a strong secret key.

USERS = {'user': 'ASR2354$%^$RGFDEgdg'}

@app.route('/')
def home():
    if 'user' in session:
        return render_template('home.html', username=session['user'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            session['user'] = username
            return redirect(url_for('home'))
        return render_template('login.html', error="Invalid credentials!")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in USERS:
            USERS[username] = password
            return redirect(url_for('login'))
        return render_template('register.html', error="User already exists!")
    return render_template('register.html')

@app.route('/diary', methods=['GET', 'POST'])
def diary():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        diary_entry = request.form['diary_entry']
        pdf_buffer = BytesIO()
        content = []
        styles = getSampleStyleSheet()
        content.append(Paragraph(f"Diary Entry by {session['user']}:", styles['Heading2']))
        content.append(Paragraph(diary_entry, styles['Normal']))

        doc = SimpleDocTemplate(pdf_buffer)
        doc.build(content)
        pdf_buffer.seek(0)

        return send_file(pdf_buffer, as_attachment=True, download_name="diary_entry.pdf", mimetype='application/pdf')

    return render_template('diary.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
