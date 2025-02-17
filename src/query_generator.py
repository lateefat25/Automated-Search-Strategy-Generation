def generate_boolean_query(job_title, skills, location):
    skills_query = " OR ".join([f'"{skill}"' for skill in skills])
    return f'("{job_title}") AND ({skills_query}) AND ("{location}")'
