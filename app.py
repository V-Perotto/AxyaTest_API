from models.table import create_table
from models.db import mysql
from config import create_app

if __name__ == '__main__':
    app = create_app(host, port, user, pwd, db)
    mysql.init_app(app)
    create_table()
    app.run(debug=True)