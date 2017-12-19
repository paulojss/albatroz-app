from app import db
from app.models import Recipe


# create the database and the database table
db.create_all()

# insert recipe data
recipe1 = Recipe('anuncio.jpg')
db.session.add(recipe1)


# commit the changes
db.session.commit()
