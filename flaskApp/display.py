import functools
import json

from fetch import BWFRankings
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('display', __name__, url_prefix='/display')


@bp.route('/display', methods=('GET', 'POST'))
def query():
    if request.method == 'POST':
        discipline = request.form.get('discipline')

        if discipline is None:
            discipline = 'MS'

        players = BWFRankings.main(BWFRankings.ladders[discipline])

        return render_template('display/display.html', players=players, discipline=json.dumps(discipline))

    if request.method == 'GET':
        discipline = 'MS'  # Default is MS
        return render_template('display/display.html', discipline=json.dumps(discipline))
