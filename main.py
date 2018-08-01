#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, os, jinja2

from google.appengine.api import users #Google login
from google.appengine.ext import ndb #Cloud storage

#Say where you are keeping your HTML templates for Jinja2
template_directory = os.path.join(os.path.dirname(__file__), 'templates')
#Create a Jinja environment object by passing it the template location
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('mainpage.html')
        self.response.out.write(template.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('aboutus.html')
        self.response.out.write(template.render())

class ResourcesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('resources.html')
        self.response.out.write(template.render())

class SituationsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('situations.html')
        self.response.out.write(template.render())

class UKHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('hotlines-uk.html')
        self.response.out.write(template.render())

class USHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('hotlines-us.html')
        self.response.out.write(template.render())

class AdviceHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('advice.html')
        self.response.out.write(template.render())

class AppsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('app-recs.html')
        self.response.out.write(template.render())

class SituationsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('situations.html')
        self.response.out.write(template.render())

class RespectHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('situations-respect.html')
        self.response.out.write(template.render())

# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_environment.get_template('mainpage.html')
#         self.response.out.write(template.render())
#
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_environment.get_template('mainpage.html')
#         self.response.out.write(template.render())
#
# class MainHandler(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_environment.get_template('mainpage.html')
#         self.response.out.write(template.render())

app = webapp2.WSGIApplication([ #dont forget the commas
    ('/', MainHandler),
    ('/aboutus', AboutHandler),
    ('/resources', ResourcesHandler),
    ('/situations', SituationsHandler),
    ('/hotlinesuk', UKHandler),
    ('/hotlinesus', USHandlers),
    ('/advice', AdviceHandler),
    ('/app-recs', AppsHandler)
], debug=True)
