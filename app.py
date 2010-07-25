#-*- coding: utf-8 -*-

# Initial setup by Antonio Ognio <antonio@ognio.com>

import os
import sys
import cgi

# General AppEngine imports
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp.util import login_required
# WTForms imports (Form handling)
from wtforms import Form, fields, widgets, validators

# Jinja2 imports and settings (Template handling)

import codecs
from jinja2 import Environment, FileSystemLoader

template_dirs = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

environment = Environment(loader=FileSystemLoader(template_dirs))

# Request Handlers

class BaseRequestHandler(webapp.RequestHandler):

    def render_template(self, template_path, context = {}):
        template = environment.get_template(template_path)
        # Fixes a bug in Python that renders the unicode identifier (0xEF 0xBB 0xBF) as a character.
        # If untreated, it can prevent the page from validating or rendering properly. 
        bom = unicode( codecs.BOM_UTF8, "utf8" )
        rendered_content = template.render(**context).replace(bom, '')
        self.response.out.write(rendered_content)

# Lista de Url Handlers

class main(BaseRequestHandler):
    def get(self):
        self.render_template('main')
	
class codigo(BaseRequestHandler):
    def get(self):
        self.render_template('codigo')

class comunidad(BaseRequestHandler):
    def get(self):
        self.render_template('comunidad')
	
class contacto(BaseRequestHandler):
    def get(self):
        self.render_template('contacto')
	
class docs(BaseRequestHandler):
    def get(self):
        self.render_template('docs')

class faqs(BaseRequestHandler):
    def get(self):
        self.render_template('faqs')

class irc(BaseRequestHandler):
    def get(self):
        self.render_template('irc')

# URL mapping

application = webapp.WSGIApplication(
    [('/', main),('/codigo',codigo),('/comunidad',comunidad),('/contacto',contacto),('/docs',docs),('/faqs',faqs),('/irc',irc)],
    debug=True)

# Run application

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
