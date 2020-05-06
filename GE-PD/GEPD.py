from flask import Blueprint, render_template, request
from . import db
from datetime import datetime, time


bp = Blueprint("GEPD", __name__)

@bp.route('/', methods=('GET', 'POST'))
def calendar():
    if request.method == 'POST':
        dateOne = request.form['date']
        print(dateOne)

        with db.get_db() as con:
            with con.cursor() as cur:
                # I am attempting to cut out several hundred lines of code by
                # running the following query:
                cur.execute("""
                   SELECT stage_time FROM (
                   	SELECT DISTINCT ON (stage, difficulty) id, date_achieved, stage, difficulty, stage_time
                   	FROM ge_pr_history WHERE date_achieved <= %s
                   	ORDER BY stage, difficulty, stage_time, date_achieved ASC
                   ) AS ge_prs
                   """, (dateOne,))
                time_test = cur.fetchall()
                print(time_test[0])
                times = time_test[0]
                for n in range(1,60):
                    times += time_test[n]
                print(times)

                # I think I should make the following a separate module/function

                agentSeconds = 0
                agentMinutes = 0
                agentHours = 0
                sagentSeconds = 0
                sagentMinutes = 0
                sagentHours = 0
                dagentSeconds = 0
                dagentMinutes = 0
                dagentHours = 0
                totalSeconds = 0
                totalMinutes = 0
                totalHours = 0

                for n in range(0,20):
                    # if times[n] is None:
                    #     times[n].hour = 0
                    #     times[n].minute = 20
                    #     times[n].second = 0
                    # if times[n].minute >= 20:
                    #     times[n].minute = 20
                    #     times[n].second = 0
                    agentSeconds += times[3*n+1].second
                    if agentSeconds >= 60:
                        agentSeconds -= 60
                        agentMinutes += 1
                    agentMinutes += times[3*n+1].minute
                    if agentMinutes >= 60:
                        agentMinutes -= 60
                        agentHours += 1
                    agentHours += times[3*n+1].hour
                for n in range(0,20):
                    sagentSeconds += times[3*n+2].second
                    if sagentSeconds >= 60:
                        sagentSeconds -= 60
                        sagentMinutes += 1
                    sagentMinutes += times[3*n+2].minute
                    if sagentMinutes >= 60:
                        sagentMinutes -= 60
                        sagentHours += 1
                    sagentHours += times[3*n+2].hour
                for n in range(0,20):
                    dagentSeconds += times[3*n].second
                    if dagentSeconds >= 60:
                        dagentSeconds -= 60
                        dagentMinutes += 1
                    dagentMinutes += times[3*n].minute
                    if dagentMinutes >= 60:
                        dagentMinutes -= 60
                        dagentHours += 1
                    dagentHours += times[3*n].hour

                totalSeconds += (agentSeconds + sagentSeconds + dagentSeconds)
                if totalSeconds >= 120:
                    totalSeconds -= 120
                    totalMinutes += 2
                if totalSeconds >= 60:
                    totalSeconds -= 60
                    totalMinutes += 1
                totalMinutes += (agentMinutes + sagentMinutes + dagentMinutes)
                if totalMinutes >= 120:
                    totalMinutes -= 120
                    totalHours += 2
                if totalMinutes >= 60:
                    totalMinutes -= 60
                    totalHours += 1
                totalHours += (agentHours + sagentHours + dagentHours)
                print(totalHours)
                print(totalMinutes)
                print(totalSeconds)


                return render_template('ge_times.html', times=times,
                        agentSeconds=agentSeconds, agentMinutes=agentMinutes, agentHours=agentHours,
                        sagentSeconds=sagentSeconds, sagentMinutes=sagentMinutes, sagentHours=sagentHours,
                        dagentSeconds=dagentSeconds, dagentMinutes=dagentMinutes, dagentHours=dagentHours,
                        totalSeconds=totalSeconds, totalMinutes=totalMinutes, totalHours=totalHours,
                        dateOne=dateOne)
    # Write something here that displays my best times on the current day.
    # I think that with this, I can get rid of the render_template blank times
    # below, and render index instead
    return render_template('blank_times.html')
