from flask import Blueprint, render_template, request
from . import db, time_calc
from datetime import date, datetime, time


bp = Blueprint("GEPD", __name__)

@bp.route('/', methods=('GET', 'POST'))
def home_page():
    return render_template('index.html')

@bp.route('/geTimes/', methods=('GET', 'POST'))
def ge_calendar():
    dateOne = date.today()
    with db.get_db() as con:
        with con.cursor() as cur:
            # This should display my times as of the current day.
            cur.execute("""
               	SELECT DISTINCT ON (stage, difficulty) id, date_achieved, stage, difficulty, stage_time
               	FROM ge_pr_history
               	ORDER BY stage, difficulty, stage_time, date_achieved ASC
               """)
            time_test = cur.fetchall()
            times = []
            time_id = []
            for n in range(0,60):
                times.append(time_test[n]['stage_time'])
                time_id.append(time_test[n]['id'])
    if request.method == 'POST':
        dateOne = request.form['date']
        # If the date from the form is empty, set dateOne to today's date
        if request.form['date'] == '':
            dateOne = date.today()
        with db.get_db() as con:
            with con.cursor() as cur:
                cur.execute("""
                   	SELECT DISTINCT ON (stage, difficulty) id, date_achieved, stage, difficulty, stage_time
                   	FROM ge_pr_history WHERE date_achieved <= %s
                   	ORDER BY stage, difficulty, stage_time, date_achieved ASC
                   """, (dateOne,))
                time_test = cur.fetchall()
                times = []
                time_id = []
                for n in range(0,60):
                    times.append(time_test[n]['stage_time'])
                    time_id.append(time_test[n]['id'])

    calc = time_calc.ge_time_calculation(times)
    return render_template('geTimes.html', times=times, calc=calc, dateOne=dateOne, time_id=time_id)

@bp.route('/pdTimes/', methods=('GET', 'POST'))
def pd_calendar():
    dateOne = date.today()
    with db.get_db() as con:
        with con.cursor() as cur:
            # This should display my times as of the current day.
            cur.execute("""
               	SELECT DISTINCT ON (stage, difficulty) id, date_achieved, stage, difficulty, stage_time
               	FROM pd_pr_history
               	ORDER BY stage, difficulty, stage_time, date_achieved ASC
               """)
            time_test = cur.fetchall()
            times = []
            time_id = []
            for n in range(0,63):
                times.append(time_test[n]['stage_time'])
                time_id.append(time_test[n]['id'])
    if request.method == 'POST':
        dateOne = request.form['date']
        # If the date from the form is empty, set dateOne to today's date
        if request.form['date'] == '':
            dateOne = date.today()

        with db.get_db() as con:
            with con.cursor() as cur:
                cur.execute("""
                   	SELECT DISTINCT ON (stage, difficulty) id, date_achieved, stage, difficulty, stage_time
                   	FROM pd_pr_history WHERE date_achieved <= %s
                   	ORDER BY stage, difficulty, stage_time, date_achieved ASC
                   """, (dateOne,))
                time_test = cur.fetchall()
                times = []
                time_id = []
                for n in range(0,63):
                    times.append(time_test[n]['stage_time'])
                    time_id.append(time_test[n]['id'])

    calc = time_calc.pd_time_calculation(times)
    return render_template('pdTimes.html', times=times, time_id=time_id, calc=calc, dateOne=dateOne)

@bp.route('/geTimes/<int:id>/')
def ge_time(id):
    with db.get_db() as con:
        with con.cursor() as cur:
            # The following I can use for displaying a single time on its own page
            #
            cur.execute("""
              	SELECT DISTINCT ON (stage, difficulty) *
              	FROM ge_pr_history WHERE id=%s
              	ORDER BY stage, difficulty, stage_time, date_achieved ASC
               """, (id,))
            info_test = cur.fetchall()
            # I want to display a history of that stage/difficulty
            cur.execute("""
                SELECT stage, difficulty
                FROM ge_pr_history
                WHERE id=%s
                """, (id,))
            stage_info = cur.fetchall()
            cur.execute("""
                SELECT *
                FROM ge_pr_history
                WHERE stage=%s AND difficulty=%s
                ORDER BY id DESC
                """, (stage_info[0]['stage'], stage_info[0]['difficulty']))
            stage_history = cur.fetchall()
            game = 'GE'
    return render_template('time.html', info_test=info_test, stage_history=stage_history, game=game)

@bp.route('/pdTimes/<int:id>/')
def pd_time(id):
    with db.get_db() as con:
        with con.cursor() as cur:
            # The following I can use for displaying a single time on its own page
            #
            cur.execute("""
              	SELECT DISTINCT ON (stage, difficulty) *
              	FROM pd_pr_history WHERE id=%s
              	ORDER BY stage, difficulty, stage_time, date_achieved ASC
               """, (id,))
            info_test = cur.fetchall()
            # I want to display a history of that stage/difficulty
            cur.execute("""
                SELECT stage, difficulty
                FROM pd_pr_history
                WHERE id=%s
                """, (id,))
            stage_info = cur.fetchall()
            cur.execute("""
                SELECT *
                FROM pd_pr_history
                WHERE stage=%s AND difficulty=%s
                ORDER BY id DESC
                """, (stage_info[0]['stage'], stage_info[0]['difficulty']))
            stage_history = cur.fetchall()
            game = 'PD'
    return render_template('time.html', info_test=info_test, stage_history=stage_history, game=game)
