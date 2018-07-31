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

        currentUser = users.get_current_user()

        if currentUser:
            nickname = currentUser.nickname()

            url = users.create_login_url("/")
            url_text = "logout"
        else:
            url = users.create_login_url('/')
            url_text = "login"

        template = jinja_environment.get_template('mainpage.html')
        self.response.out.write(template.render(url = url, url_text = url_text))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())

class OutputHandler(webapp2.RequestHandler):
    def post(self): #Use post if you will be receiving information

        #'userInput' is also name in the textarea in about.html
        inputFromAbout = self.request.get('userInput')

        template = jinja_environment.get_template('output.html')
        self.response.out.write(template.render(data=inputFromAbout))

app = webapp2.WSGIApplication([ #dont forget the commas
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/output', OutputHandler)
], debug=True)
