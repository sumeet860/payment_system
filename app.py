from flask import Flask, request, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, validators, DecimalField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Length, Optional

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


class ProcessPayment(FlaskForm):
    """ 
    Class for payment
    """
    cardnumber = StringField('CreditCardNumber', validators=[
                             DataRequired(), Length(16)])
    name = StringField('CardHolder', validators=[DataRequired()])
    expiry = DateTimeField('ExpirationDate', validators=[Optional()])
    code = StringField('SecurityCode', validators=[
                       DataRequired(), Length(3)])
    amt = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Make Payment')


@app.route('/', methods=['GET', 'POST'])
def payment():
    form = ProcessPayment()
    if form.validate_on_submit():
        cardnumber = form.cardnumber.data
        name = form.name.data
        expiry = form.expiry.data
        code = form.code.data
        amt = form.amt.data
        # if amt <= 20:
        #     print("CheapPaymentGateway")
        # elif amt in range(21, 501):
        #     print("ExpensivePaymentGateway")
        # else:
        #     print("PremiumPaymentGateway")
        return redirect(url_for('success'))
    return render_template('payment.html', title='Payment', form=form)


@app.route('/success')
def success():
    return render_template('success.html')
