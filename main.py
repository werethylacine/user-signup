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
import webapp2
import re


def valid_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

def valid_password(password):
    USER_RE = re.compile(r"^.{3,20}$")
    return USER_RE.match(password)

def valid_email(email):
    USER_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    return USER_RE.match(email)

def buildpage(text_area_content):
    title = "<div id='title'><h1>Signup</h1></div>"
    username_chunk = '''<div id="username">
            <label>
                Username
                <input type="text" name="username">
                </label>
        </div>
    '''

    password_chunk = '''<div id="pw1">
            <label>
                Password
                 <input type="password" name="pw1">
             </label>
         </div>
     '''
    verify_password_chunk = '''<div id="pw2">
            <label>
                Verify Password
                <input type="password" name="pw2">
            </label>
        </div>
    '''
    email_chunk = '''<div id="email">
            <label>
                Email (optional)
                <input type="email" name="email">
            </label>
        </div>
    '''
    submit = "<input type='submit' />"
    return title + '<form method="post">' + username_chunk + password_chunk + verify_password_chunk + email_chunk + submit + '</form>'

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = buildpage("")
        self.response.write(content)

    def post(self):
        username = self.request.get("username")
        pw1 = self.request.get("pw1")
        pw2 = self.request.get("pw2")
        email = self.request.get("email")

        ok_username = valid_username(username)
        pw_match = pw1 == pw2
        ok_password = valid_password(pw1)
        ok_email = valid_email(email)

        if ok_username and pw_match and ok_password and ok_email:
            self.response.write("%s, got your info! PW: %s, Email: %s" %(username, pw1, email))
        else:
            self.response.write("something's not okay!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
