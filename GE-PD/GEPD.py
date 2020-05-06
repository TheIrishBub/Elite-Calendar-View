from flask import Blueprint, render_template, request
from . import db, time_calc
from datetime import date, datetime, time


bp = Blueprint("GEPD", __name__)

@bp.route('/', methods=('GET', 'POST'))
def calendar():
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
    return render_template('geTimes.html', times=times,
            agentSeconds=calc[2], agentMinutes=calc[1], agentHours=calc[0],
            sAgentSeconds=calc[5], sAgentMinutes=calc[4], sAgentHours=calc[3],
            dAgentSeconds=calc[8], dAgentMinutes=calc[7], dAgentHours=calc[6],
            totalSeconds=calc[11], totalMinutes=calc[10], totalHours=calc[9],
            dateOne=dateOne)
