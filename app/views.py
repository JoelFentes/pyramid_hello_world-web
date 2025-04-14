from pyramid.view import view_config

@view_config(route_name='home', renderer='home.jinja2')
def home_view(request):
    nomes = ["Ana", "Emanuele", "Joel", "Class", "Prof. Domingos"]
    cores_body = ["#ff66cc", "#16213e", "#0f3460", "#533483", "red"] 
    return {'nomes': nomes, 'cores_body': cores_body}

