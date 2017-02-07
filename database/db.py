from flask import Flask, g
import sqlite3

# Database files
DATABASE =    './database/concordia.sqlite'
INIT_SCHEMA = 'schema.sql'

# ----------------------------------- #
# ------------- Queries ------------- #

'''
'   Make database query.
'''
def query(query, args=(), one=False):
    cur = get().execute(query, args) # Execute query
    rv = cur.fetchall() # Get results
    cur.close()
    return (rv[0] if rv else None) if one else rv
    
'''
'   Make database insert.
'''
def insert(insert, args=(), one=False):
    query(insert, args) # Insert values
    get().commit() # Commit

# ------------------------------------ #
# ------------ Connection ------------ #

app = Flask(__name__)

'''
'   Get database connection.
'''
def get():
    db = getattr(g, '_database', None)
    if db is None:
        # Connect to database
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = dict_row_factory
        
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
        
# ----------------------------------- #
# ------------- Helpers ------------- #

def dict_row_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
