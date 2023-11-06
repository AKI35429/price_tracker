from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from pyshorteners import Shortener
from pyshorteners.exceptions import ShorteningErrorException
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html', user=current_user)


@views.route('/home')
def homes():
    return render_template('home.html', user=current_user)



@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST': 
        productname = request.form.get('productname')  # Gets the note from the HTML 
        url = request.form.get('url')  # Gets the note from the HTML 
        req_price = request.form.get('Required_price')  # Gets the note from the HTML 
        if len(productname) < 1:
            flash('Name is too short!', category='error') 
        else:
            
            # Inside your view function
            try:
                s = Shortener()
                short_url = s.tinyurl.short(url)
            except ShorteningErrorException as e:
                flash('Error while shortening the URL. Please check the URL or try again later.', category='error')
            else:
                new_note = Note(product_name=productname, large_url=url, short_url= short_url, req_price=req_price, user_id=current_user.id)  # providing the schema for the note 
                db.session.add(new_note)  # adding the note to the database 
                db.session.commit()
                flash('Tracking for product Started!', category='success')

    return render_template('dashboard.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note(): 
    note = json.loads(request.data)  # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/contact')
def contact():
    return render_template('contact.html',user=current_user)


@views.route('/settings')
def settings():
    return render_template('settings.html',user=current_user)