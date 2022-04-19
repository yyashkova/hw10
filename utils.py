import json

def get_candidates(path):
    with open('candidates.json', 'r') as candidates:
        return json.load(candidates)


def format_candidate(candidates_list):
    result = '<pre>'
    for candidate in candidates_list:
        result += (
        f'Имя кандидата - {candidate["name"]}\n'
        f'Позиция кандидата - {candidate["position"]}\n'
        f'Навыки - {candidate["skills"]}\n \n'
        )
        result += '<pre>'

    return result


def get_id_candidate(candidates_list, candidate_id):
    candidate_id = int(candidate_id)

    for c in candidates_list:
        if c['id'] == candidate_id:

            return c


def get_candidate_by_skill(candidates_list, candidate_skill):
    result = []

    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')

        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result




