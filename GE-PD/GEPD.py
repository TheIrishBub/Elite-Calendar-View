from flask import Blueprint, render_template, request
from . import db, time_calc
from datetime import date, datetime, time


bp = Blueprint("GEPD", __name__)

@bp.route('/', methods=('GET', 'POST'))
def ge_calendar():
    dateOne = date.today()
    with db.get_db() as con:
        with con.cursor() as cur:
            # This should display my times as of the current day.
            cur.execute("""
               SELECT stage_time FROM (
               	SELECT DISTINCT ON (stage, difficulty) id, date_achieved, stage, difficulty, stage_time
               	FROM ge_pr_history
               	ORDER BY stage, difficulty, stage_time, date_achieved ASC
               ) AS ge_prs
               """)
            time_test = cur.fetchall()
            times = time_test[0]
            for n in range(1,60):
                times += time_test[n]
    if request.method == 'POST':
        dateOne = request.form['date']
        # If the date from the form is empty, set dateOne to today's date
        if request.form['date'] == '':
            dateOne = date.today()
        print(dateOne)

        with db.get_db() as con:
            with con.cursor() as cur:
                cur.execute("""
                   SELECT stage_time FROM (
                   	SELECT DISTINCT ON (stage, difficulty) id, date_achieved, stage, difficulty, stage_time
                   	FROM ge_pr_history WHERE date_achieved <= %s
                   	ORDER BY stage, difficulty, stage_time, date_achieved ASC
                   ) AS ge_prs
                   """, (dateOne,))
                time_test = cur.fetchall()
                times = time_test[0]
                for n in range(1,60):
                    times += time_test[n]

    # I think I should make the following a separate module/function

    calc = time_calc.ge_time_calculation(times)
    print(calc)
    # Maybe I could do calc=calc ?
    return render_template('geTimes.html', times=times, calc=calc, dateOne=dateOne)
