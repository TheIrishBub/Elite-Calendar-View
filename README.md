# Elite-Calendar-View
This allows someone to view what my PRs are on any given day for the N64 games GoldenEye 007 and Perfect Dark, modeled after my times page on https://rankings.the-elite.net/~TheIrishBub.

This came about from an idea I had where I was curious to see what my PRs (personal records) were on any given day. As far as I'm aware, the rankings page linked above does not have this feature, so I decided to make one myself!

As of now, this project is Mac-only. As I progress, I do plan to work on a version for Windows users, as well.

## Installation instructions (you must have python 3 installed):
Clone this repo, and then run the following commands in the terminal:
```sh
$ cd Elite-Calendar-View
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=GE-PD
$ export FLASK_ENV=development
$ flask init-db
$ flask run
```
After that, just open a new tab (if you wish) and go to http://127.0.0.1:5000/ to see my page.
