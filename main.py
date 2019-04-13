import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('create.jinja2')
    
    if request.method == 'POST':
        donor = Donor.select().where(Donor.name == 'Charlie').get()
        print(donor)
        old_donation = Donation.select().where(Donation.donor == donor).get()
        print(old_donation)

        # Donation.update(performed=, performed_by=user)\
        #     .where(Task.id == request.form['task_id'])\
        #     .execute()
        #user = User.select().where(User.name == session['username']).get()

        # Donation.update(performed=datetime.now(), performed_by=user)\
        #     .where(Task.id == request.form['task_id'])\
        #     .execute()
        new_donation = Donation(value=10, donor=donor)
        new_donation.save()
        return redirect(url_for('home'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

