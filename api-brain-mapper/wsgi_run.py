from gevent import monkey
monkey.patch_all() # we need to patch very early

from psycogreen.gevent import patch_psycopg # Patch DB client
patch_psycopg()

from src.app import create_app
app = create_app() # re-export
