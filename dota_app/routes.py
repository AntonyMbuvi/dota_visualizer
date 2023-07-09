from flask import render_template, url_for,flash, redirect, session, request
from dota_app.forms import MyForm, CheckGraphs
from dota_app import app
from dota_app.graphs import my_plots
import os
from dota_app.extra_func import delete_saved_plots

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    
    if request.referrer and 'graphs' in request.referrer:
        delete_saved_plots()
        session.pop('my_images', None)

    if form.validate_on_submit():
        # Process the selected options
        selected_options = form.options.data
        
        # Save flash message to session
        session['flash_message'] = f"Selected options: {', '.join(selected_options)}"
        session['selected_columns'] = selected_options

        delete_saved_plots()
        return redirect(url_for('graphs'))

    flash_message = session.pop('flash_message', None)
    
    return render_template('index.html', form=form, flash_message=flash_message) 



from flask import send_from_directory

@app.route('/graphs', methods=['POST', 'GET'])
def graphs():
    selected_columns = session.get('selected_columns')
    
    if not selected_columns:
        flash('No selected columns. Please go back and select options.')
        return redirect(url_for('index'))

    my_plots(selected_columns)
    
    my_images = session.get('my_images', [])
    
    
    return render_template('graphs.html', images=my_images)
    
    

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)


