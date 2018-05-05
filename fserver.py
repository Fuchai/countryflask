from flask import Flask, render_template, send_from_directory
from flask.ext.wtf import Form
from wtforms import SelectField, DecimalField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import query

app = Flask(__name__)
Bootstrap(app)
app.debug=True
app.secret_key = 'jasonhu'

form=None
class countryForm(Form):
    continents = SelectField('Hit Search to populate this field',
                   choices=[])
    submit =SubmitField("Search")

@app.route('/', methods=['GET', 'POST'])
def index():
    form=countryForm()
    form.continents.choices=getcontinents()
    if form.validate_on_submit():
        countrytable=()
        return render_template('countrytable.html', countrytable=countrytable,form=form)
    return render_template('index.html', form=form)

@app.route('/continents_name',methods=['GET', 'POST'])
def getcontinents():
    continent_list=query.get_continents()
    return continent_list

if __name__ == '__main__':
    app.run()
