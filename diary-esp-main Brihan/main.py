# Importar
from flask import Flask, render_template,request, redirect
# Importando la biblioteca de bases de datos
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Conectando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creación de una base de datos
db = SQLAlchemy(app )

#Asignación #1. Crear una tabla de base de datos

class Card(db.Model):
    # Creación de los campos
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Título de la entrada
    title = db.Column(db.String(100), nullable=False)
    # Título secundario de la entrada
    subtitle = db.Column(db.String(100), nullable=False)
    # Título secundario de la entrada
    text = db.Column(db.String(100), nullable=False)

    # Salida del objeto y su id
    def __repr__(self):
        return f'<Card {self.id}>'

# Ejecutar la página con contenido
@app.route('/')
def index():
    # Visualización de los objetos de la DB
    # Asignación #2. Mostrar los objetos de la DB en index.html

    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html', cards=cards)
            
# Ejecutar la página con la tarjeta

@app.route('/card/<int:id>')
def card(id):
    # Asignación #2. Mostrar la tarjeta correcta por su id
    card = Card.query.get(id)

    return render_template('card.html', card=card)


# Ejecutar la página y crear la tarjeta
@app.route('/create')
def create():
    return render_template('create_card.html')

# El formulario de la tarjeta
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['titleBox']
        subtitle =  request.form['subtitleBox']
        text =  request.form['textArea']

        # Asignación #2.Crear una forma de almacenar datos en la BD
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()


        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
