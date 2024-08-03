## You can make a DB migration like this:

Move to API folder and activate virtual environment:

`source venv/bin/activate`

Execute the migration:

`flask db migrate -m "Initial migration."`

> Note: The migration script needs to be reviewed and edited, as Alembic is not always able to detect every change you make to your models. In particular, Alembic is currently unable to detect table name changes, column name changes, or anonymously named constraints. A detailed summary of limitations can be found in the Alembic autogenerate documentation.

Then you can apply the changes described by the migration script to your database:

`flask db upgrade`

Each time the database models change, repeat the migrate and upgrade commands.

> Once finalized, the migration also needs to be added to version control. (Migrations are stored in /migrations/versions/ folder)