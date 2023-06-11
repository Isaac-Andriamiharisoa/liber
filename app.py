from models import app, Ame
from flask import render_template, request, jsonify, redirect, url_for, session
import os
import bcrypt

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'MofoAkondro69420!!'


@app.route('/', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def post_login():
    if request.method != 'POST':
        return render_template('login.html')
    else:
        nom = request.form.get('nom')
        motdepasse = request.form.get('motdepasse')
        ame = Ame.query.filter_by(nom=nom, motdepasse=motdepasse).first()

        if ame is None:
            return jsonify({
                'message': 'credential mismatch',
                'error_code': 403
            })
        else:
            id = ame.id
            session['user_id'] = id
            return redirect(url_for('get_ame_details', id=id))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('get_login'))


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
    user_id = session.get('user_id')

    if user_id:
        if user_id == data.id:
            return render_template('ame.html', data=data, user_id=user_id)
        else:
            return jsonify({
                'message': 'restricted page',
                'error_code': 403
            })
    else:
        return redirect(url_for('get_login'))


@app.route('/ames/create', methods=['GET'])
def create_ame():
    return render_template('create_ames.html')


@app.route('/ames/create', methods=['POST'])
def creating():

    data = request.form.to_dict()

    if data is None:
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

    ame = Ame(nom=nom, prenom=prenom, motdepasse=motdepasse, bapteme=batemy, communion=communion,
              fanavaozana=fanavaozana, confirmation=confirmation, mariage=mariage, mort=mort)
    ame.insert()
    id = ame.id
    session['user_id'] = id

    return redirect(url_for('get_ame_details', id=id))


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
