# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import scoped_session, sessionmaker
# import gevent.local  # For sessions isolated for each coroutine
# import os

# db = SQLAlchemy()

# # In production ensures that every gevent coroutine have its own session
# if(os.getenv('ENV_MODE') == 'production'):
#     db.session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db.engine), scopefunc=gevent.local.local)
# else: # On dev mode a global session is used
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db.engine)
#     db.session = SessionLocal()  # Global session for dev mode

import os
from gevent import getcurrent
from flask_sqlalchemy import SQLAlchemy

# Config db connection without configuring sessions' scope manually
db = SQLAlchemy(
    session_options={
        "autocommit": False,
        "autoflush": False,
        "bind": None,  # It will be assigned when calling init_app()
        "scopefunc": None # Let Flask SQLAlchemy decide the scope, unless u want to fight with gevent and connection pool
    }
)
