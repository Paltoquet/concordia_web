from flask import Flask, g
import sqlite3

# Database files
DATABASE =    './database/concordia.sqlite'
INIT_SCHEMA = 'schema.sql'

'''
'   Make database query.
'''
def query(query, args=(), one=False):
    cur = get().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# --------------------------------------- #

app = Flask(__name__)

'''
'   Get database connection.
'''
def get():
    db = getattr(g, '_database', None)
    if db is None:
        # Connect to database
        db = g._database = sqlite3.connect(DATABASE)
        
        # Initialize database
        with app.open_resource(INIT_SCHEMA, mode='r') as script:
            db.cursor().executescript(script.read())
        db.commit()
    return db

'''
'   Close database connection.
'''
def close():
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
