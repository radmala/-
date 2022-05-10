from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_1 = StringField('ID астронавта', validators=[DataRequired()])
    password_1 = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_2 = StringField('ID капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template('base.html', title=title)


@app.route("/training/<prof>")
def training(prof):
    return render_template('training.html', prof=prof)


@app.route("/list_prof/<list_type>")
def list_prof(list_type):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_prof.html', professions=professions, list_type=list_type)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route("/answer")
@app.route("/auto_answer")
def auto_answer():
    params = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template('auto_answer.html', **params)


@app.route("/distribution")
def distribution():
    astronauts = ['Рэдли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Шон Бин']
    return render_template('distribution.html', astronauts=astronauts)


@app.route("/table/<sex>/<int:age>")
def table(sex, age):
    return render_template('table.html', sex=sex, age=age)


images = ['mars1.jpg', 'mars2.jpg', 'mars3.jpg']


@app.route("/galery", methods=['POST', 'GET'])
def galery():
    if request.method == 'GET':
        return render_template('galery.html', images=images)
    elif request.method == 'POST':
        f = request.files['file']
        image = open(f'static/img/{f.filename}', 'wb')
        image.write(f.read())
        image.close()
        images.append(f.filename)
        return render_template('galery.html', images=images)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
