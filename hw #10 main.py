from flask import Flask

from utils import get_candidates, format_candidate, get_id_candidate, get_candidate_by_skill

app = Flask(__name__)

candidates_list = get_candidates('candidates.json')

@app.route('/')
def main():
    return format_candidate(candidates_list)


@app.route('/candidates/<candidate_id>')
def page_candidate(candidate_id):
    candidate = get_id_candidate(candidates_list, candidate_id)

    result = f'<img src="{candidate["picture"]}">\n'

    return result + format_candidate([candidate])

@app.route('/skills/<skill>')
def skills(skill):
    return format_candidate(get_candidate_by_skill(candidates_list, skill))

app.run()

