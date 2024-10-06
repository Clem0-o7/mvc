from flask import Flask, render_template, request, redirect, url_for
from mvc.models import get_all_traffic_lights, get_traffic_light, add_traffic_light, update_traffic_light, delete_traffic_light

app = Flask(__name__)

@app.route('/')
def index():
    traffic_lights = get_all_traffic_lights()
    return render_template('index.html', traffic_lights=traffic_lights)

@app.route('/add', methods=['GET', 'POST'])
def add_light():
    if request.method == 'POST':
        location = request.form['location']
        status = request.form['status']
        add_traffic_light(location, status)
        return redirect(url_for('index'))
    return render_template('add_light.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_light(id):
    light = get_traffic_light(id)
    if request.method == 'POST':
        location = request.form['location']
        status = request.form['status']
        update_traffic_light(id, location, status)
        return redirect(url_for('index'))
    return render_template('edit_light.html', light=light)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_light(id):
    delete_traffic_light(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
