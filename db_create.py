from app import db
from app.models import Image, User


# drop all of the existing database tables
db.drop_all()

# create the database and the database table
db.create_all()

# insert image data
recipe1 = Image('imagem-test','0938PPJ.jpeg','imagem de anuncio de biscoito','nnnn/nnn/nnn/nn')
db.session.add(recipe1)

# insert user
#user1 = User('Paulo', 'Soares', 'Paulo@gmail.com', '123456789')
#db.session.add(user1)
# commit the changes
db.session.commit()
