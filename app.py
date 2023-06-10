from models import app, Ame
from flask import render_template, request, jsonify
import os

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


@app.route('/ames')
def get_ames():
    ames = Ame.query.all()
    data = []
    for ame in ames:
        data.append({
            'nom': ame.nom,
            'prenom': ame.prenom
        })
    return render_template('ames.html', ames=data)


@app.route('/ames/<id>')
def get_ame_details(id):
    data = Ame.query.get(id)
    return jsonify({
        'nom': data.nom,
        'prenom': data.prenom,
        'bapteme': data.bapteme
    })


@app.route('/ames/create', methods=['GET'])
def get_page():
    return render_template('create_ames.html')


@app.route('/ames/create', methods=['POST'])
def create():

    data = request.form.to_dict()

    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    nom = data.get('nom')
    prenom = data.get('prenom')
    motdepasse = data.get('motdepasse')
    batemy = bool(data.get('batemy'))
    communion = bool(data.get('komonio'))
    fanavaozana = bool(data.get('fankaherezana'))
    confirmation = bool(data.get('confirmation'))
    mariage = bool(data.get('mariazy'))
    mort = bool(data.get('maty'))

    if nom is None or prenom is None or motdepasse is None or batemy is None or communion is None or fanavaozana is None or confirmation is None or mariage is None or mort is None:
        return jsonify({
            'error': 'Missing required fields',
            'nom': nom,
            'prenom': prenom,
            'motdepasse': motdepasse,
            'batemy': batemy,
            'communion': communion,
            'fanavaozana': fanavaozana,
            'confirmation': confirmation,
            'mariage': mariage,
            'mort': mort
        }), 400

    ame = Ame(nom=nom, prenom=prenom, bapteme=batemy, communion=communion, fanavaozana=fanavaozana, confirmation=confirmation, mariage=mariage, mort=mort)
    ame.insert()

    return jsonify({
        'success': True,
        'nom': nom,
        'prenom': prenom,
        'motdepasse': motdepasse,
        'batemy': batemy,
        'communion': communion,
        'fanavaozana': fanavaozana,
        'confirmation': confirmation,
        'mariage': mariage,
        'mort': mort
    })


@app.route('/ames/<id>/update', methods=['GET'], endpoint='update')
def get_page(id):
    data = Ame.query.get(id)
    return render_template('update_ames.html', data=data)


@app.route('/ames/<id>/update', methods=['POST'], endpoint='updating')
def update(id):
    ame = Ame.query.filter(Ame.id == id).one_or_none()
    data = request.get_json()
    ame.nom = data['nom']
    ame.prenom = data['prenom']
    ame.bapteme = data['bapteme']
    ame.update()

    return jsonify({
        'success': True,
        'ame_updated': ame.nom
    })


@app.route('/ames/<id>/delete')
def delete(id):
    ame = Ame.query.filter(Ame.id == id).one_or_none()
    ame.delete()
    return jsonify({
        'success': True,
        'ame_deleted': ame.nom
    })


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), debug=True,
            port=int(os.getenv('PORT', 4444)))
