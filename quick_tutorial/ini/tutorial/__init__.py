from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
  return Response('<body><h1>Hello World</h1></body>')


def main(global_config, **settings):
  config = Configurator()
  config.add_route('home', '/')
  config.add_view(hello_world, route_name='home')
  return config.make_wsgi_app()