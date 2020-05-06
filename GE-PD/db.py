import os
import psycopg2
import psycopg2.extras

import click
import csv
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    """Get a PostgreSQL database connection object."""

    # This function returns a connection, but you will also need to open a
    # cursor for the given transaction. For SELECT queries, it would look like:
    #
    # cur = get_db().cursor()
    # cur.execute("SELECT ...")
    # result = cur.fetchone()
    # cur.close()

    if "db" not in g:
        # if there is not already a connection, open one using app
        # configuration and save it to global `g` object
        g.db = psycopg2.connect(
            current_app.config['DB_URL'],
            sslmode=current_app.config['DB_SSLMODE'],
            cursor_factory=psycopg2.extras.DictCursor
        )

    return g.db


def close_db(e=None):
    """Close the current PostgreSQL connection"""

    # remove connection object from global `g` object, if it exists
    db = g.pop("db", None)

    if db is not None:
        # close the connection
        db.close()

def init_db():
    """Clear any existing data and create all tables."""

    # get the database connection, save and close when done
    with get_db() as con:
        # begin a transaction
        with con.cursor() as cur:
            # use the file's text to execute the SQL queries within
            # Later: add video_link and comments columns
            cur.execute("""DROP TABLE IF EXISTS ge_pr_history""")
            cur.execute("""CREATE TABLE ge_pr_history(
                id bigint,
                date_achieved date,
                stage text NOT NULL,
                difficulty text NOT NULL,
                stage_time TIME,
                system text
            );""")
            with open('./GE-PD/ge_pr_history.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cur.execute(
                        "INSERT INTO ge_pr_history VALUES (%s, %s, %s, %s, %s, %s)",
                        row
                    )
                con.commit()

@click.command("init-db")
@with_appcontext
def init_db_command():
    """CLI command to clear any existing data and create all tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
