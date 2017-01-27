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
    return not email or USER_RE.match(email)

buildpage = '''
    <head>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    </head>

    <style>
        div {
            margin: 10px 10px 10px 50px;
        }
        .error {
            margin-left: 10px;
        }
        #title {
            margin: 10px 0px 20px 50px;
        }
        input {
            border-radius: 5px;
        }
    </style>

    <div id="title"><h1>Signup</h1></div>

    <form method="post">

    <div id="username">
            <label>
                Username
                <input type="text" name="username">
            </label>
            <span class="text-danger">%(username_error)s</span>
    </div>

    <div id="pw1">
            <label>
                Password
                 <input type="password" name="pw1">
             </label>
             <span class="text-danger">%(pw_error)s</span>
    </div>

    <div id="pw2">
            <label>
                Verify Password
                <input type="password" name="pw2">
            </label>
            <span class="text-danger">%(pw_match_error)s</span>
        </div>

    <div id="email">
            <label>
                Email (optional)
                <input type="email" name="email">
            </label>
            <span class="text-danger">%(email_error)s</span>
        </div>

    <div><input type='submit' /></div></form>
    '''


class MainHandler(webapp2.RequestHandler):
    def write_form(self, (username_error, pw_error, pw_match_error, email_error)=('','','','')):
        self.response.out.write(buildpage % {"username_error" : username_error, "pw_match_error" : pw_match_error, "pw_error" : pw_error, "email_error" : email_error})

    def get(self):
        self.write_form()

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
            self.redirect("/welcome?username=" + username)
        else:
            error_list = []

            if not ok_username:
                error_list.append("That username is not valid, pal!")
            else:
                error_list.append("")

            if not ok_password:
                error_list.append("Unfortunately that's not an okay password!")
            else:
                error_list.append("")

            if not pw_match:
                error_list.append("Those passwords don't seem to match!")
            else:
                error_list.append("")

            if not ok_email:
                error_list.append("That email ain't valid, kiddo!")
            else:
                error_list.append("")

            self.write_form(tuple(error_list))

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        if valid_username(username):
            self.response.write("Welcome, %s!" %username)
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
