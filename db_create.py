from app import db
from app.models import Image


# create the database and the database table
db.create_all()

# insert image data
recipe1 = Image('imagem.jpg','imagem de anuncio de biscoito')
db.session.add(recipe1)

# commit the changes
db.session.commit()
