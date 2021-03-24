from app import app
#Importing routes   
from app.routes import *
#Importing models
from app.models import endereco
from app.models import usuario


if __name__ == "__main__":
    app.run(port=8080, debug=True)    