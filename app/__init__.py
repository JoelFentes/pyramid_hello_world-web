from pyramid.config import Configurator
import os

def main(global_config, **settings):
    config = Configurator(settings=settings)
    # Adicionar suporte ao Jinja2
    config.include('pyramid_jinja2')
    here = os.path.dirname(__file__)
    config.add_jinja2_search_path(os.path.join(here, 'templates'))

    # Registrar arquivos estáticos
    config.add_static_view(name='static', path='app:static')

    # Configurar rotas
    config.add_route('home', '/')
    config.scan('.views')
    return config.make_wsgi_app()

