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

#uses Udacity-provided regex to check for valid username
def valid_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

#uses Udacity-provided regex to check for valid password
def valid_password(password):
    USER_RE = re.compile(r"^.{3,20}$")
    return USER_RE.match(password)

#uses Google-provided and David-M-checked regex to check for valid email (if provided)
def valid_email(email):
    USER_RE = re.compile(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")  # this WORKS!!!
    return_value = not email or USER_RE.match(email)
    return return_value

#general string for the page, including bootstrap links
style_links = '''
    <head>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    </head>
    '''

main_styles = '''
    <style>
        .text-danger {
            margin-left: 10px;
            color: #C44326;
            transition: color .5s ease-in-out;
        }
        .text-danger:hover {
            color: #FF5733;
        }

        span {
            font-weight: 500;
        }
        h1, span {
            color: #FFE8A3;
            margin: 0px 20px 0px 0px;
        }
        body {
            background-image: url("images/dark_wall.png")
        }
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
        textarea:focus, input:focus {
            outline: none;
        }
        .input_field {
            width: 175px;
            height: 35px;
            border: 3px solid transparent;
            background: #AED6D1;
            overflow: hidden;
            transition:
              all        1.2s,
              border     0.5s 1.2s,
              box-shadow 0.3s 1.5s;
            white-space: nowrap;
            text-indent: 5px;
            font-weight: 400;
        }
        .input_field:hover {
            background: #55706D;
            color: #FFE8A3;
            border: 3px solid #8DCCC4;
            box-shadow: 3px 3px 2px rgba(black, 0.15);
        }
        .btn {
              border: 6px solid transparent;
              background: #AED6D1;
              color: #55706D;
              border-radius: 40px;
              padding: 5px 10px;
              overflow: hidden;
              width: 100px;
              transition:
                all        1.2s,
                border     0.5s 1.2s,
                box-shadow 0.3s 1.5s;
              white-space: nowrap;
              text-indent: 5px;
              font-weight: bold;
              }
        .btn:hover {
            text-indent: 0;
            background: #55706D;
            color: #FFE8A3;
            width: 120px;
            border: 6px solid #8DCCC4;
            box-shadow: 3px 3px 2px rgba(black, 0.15);
            }

    </style>
    '''

welcome_styles = '''
    <style>
        div {
            text-align: center;
            margin-right: auto;
            margin-left: auto;
            margin-top: 100px;
            background-color: transparent;
            box-shadow: 1px 1px 20px #000;
            width: 300px;
            height: 300px;
            border-radius: 300px;
            /* orbit2 credit to http://www.useragentman.com/blog/2013/03/03/animating-circular-paths-using-css3-transitions/ */
            -webkit-animation: orbit2 2s linear infinite; /* Chrome, Safari 5 */
            -moz-animation: orbit2 2s linear infinite; /* Firefox 5-15 */
            -o-animation: orbit2 2s linear infinite; /* Opera 12+ */
            animation: orbit2 2s linear infinite; /* Chrome, Firefox 16+, IE 10+, Safari 5 */
            -webkit-animation-delay: .3s; /* Safari 4.0 - 8.0 */
            animation-delay: .3s;
        }

        #spinner {
            width: 350px;
            height: 350px;
            margin-top: -325px;

            -webkit-animation: orbit2 2s linear infinite; /* Chrome, Safari 5 */
            -moz-animation: orbit2 2s linear infinite; /* Firefox 5-15 */
            -o-animation: orbit2 2s linear infinite; /* Opera 12+ */
            animation: orbit2 2s linear infinite; /* Chrome, Firefox 16+,
                                                     IE 10+, Safari 5 */
        }

        @-webkit-keyframes orbit2 {
        	from { 	-webkit-transform: rotate(0deg) translateX(25px) rotate(0deg); }
        	to   {  -webkit-transform: rotate(360deg) translateX(25px) rotate(-360deg); }
        }

        @-moz-keyframes orbit2 {
        	from { 	-moz-transform: rotate(0deg) translateX(25px) rotate(0deg); }
        	to   {  -moz-transform: rotate(360deg) translateX(25px) rotate(-360deg); }
        }

        @-o-keyframes orbit2 {
        	from { 	-o-transform: rotate(0deg) translateX(25px) rotate(0deg); }
        	to   {  -o-transform: rotate(360deg) translateX(25px) rotate(-360deg); }
        }

        @keyframes orbit2 {
        	from { 	transform: rotate(0deg) translateX(25px) rotate(0deg); }
        	to   {  transform: rotate(360deg) translateX(25px) rotate(-360deg); }
        }
        /*end spinner code*/

        p {
            padding-top: 135px;
            text-weight: 500;
        }

        /*gradient changing bg credit to https://codepen.io/tachy0n/pen/YWRaAO*/
        html, body {
        	width: 100%;
        	height: 100%;
        	padding: 0;
        	margin: 0;
        }
        body {
        	/* W3C */
        	background: linear-gradient(top, #FFE8A3 0%,#8DCCC4 50%, #55706D 100%);

        	/* Firefox */
        	background: -moz-linear-gradient(top, #FFE8A3 0%, #8DCCC4 50%, #55706D 100%);

        	/* Chrome,Safari4+ */
        	background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#FFE8A3), color-stop(50%,#8DCCC4), color-stop(100%,#55706D));

        	/* Chrome10+,Safari5.1+ */
        	background: -webkit-linear-gradient(top, #FFE8A3 0%,#8DCCC4 50%,#55706D 100%);

        	background-size: 500%;
        	-moz-background-size: 500%;
        	-webkit-background-size: 500%;

        	/* W3C */
        	animation-name: fun-time-awesome;
        	animation-duration: 15s;
        	animation-timing-function: linear;
        	animation-iteration-count: infinite;
        	animation-direction: alternate;
        	animation-play-state: running;

        	/* Firefox: */
        	-moz-animation-name: fun-time-awesome;
        	-moz-animation-duration: 15s;
        	-moz-animation-timing-function: linear;
        	-moz-animation-iteration-count: infinite;
        	-moz-animation-direction: alternate;
        	-moz-animation-play-state: running;

        	/* Chrome, Safari */
        	-webkit-animation-name: fun-time-awesome;
        	-webkit-animation-duration: 15s;
        	-webkit-animation-timing-function: linear;
        	-webkit-animation-iteration-count: infinite;
        	-webkit-animation-direction: alternate;
        	-webkit-animation-play-state: running;
        }

        /* W3C */
        @keyframes fun-time-awesome {
        	0% {background-position: left top;}
        	100% {background-position: left bottom;}
        }

        /* Firefox */
        @-moz-keyframes fun-time-awesome {
        	0% {background-position: left top;}
        	100% {background-position: left bottom;}
        }

        /* Chrome, Safari */
        @-webkit-keyframes fun-time-awesome {
        	0% {background-position: left top;}
        	100% {background-position: left bottom;}
        }
        /*end gradient code */

    </style>
'''

buildpage = '''
    <body><div id="title"><h1>Signup</h1></div>

    <form method="post">

    <div id="username">
            <label>
                <span>Username</span>
                <input class="input_field" type="text" name="username" value="%(username)s">
            </label>
            <span class="text-danger">%(username_error)s</span>
    </div>

    <div id="pw1">
            <label>
                <span>Password</span>
                 <input class="input_field" type="password" name="pw1">
             </label>
             <span class="text-danger">%(pw_error)s</span>
    </div>

    <div id="pw2">
            <label>
                <span>Verify Password</span>
                <input class="input_field" type="password" name="pw2">
            </label>
            <span class="text-danger">%(pw_match_error)s</span>
        </div>

    <div id="email">
            <label>
                <span>Email (optional)</span>
                <input class="input_field" type="email" name="email">
            </label>
            <span class="text-danger">%(email_error)s</span>
        </div>

    <div><input class="btn" type='submit' /></div></form></body>
    '''


class MainHandler(webapp2.RequestHandler):
    #writes input form, with different types of error to sub in to the buildpage string (see above)
    def write_form(self, (username, username_error, pw_error, pw_match_error, email_error)=('', '','','','')):
        self.response.out.write(style_links + main_styles + buildpage % {"username" : username, "username_error" : username_error, "pw_match_error" : pw_match_error, "pw_error" : pw_error, "email_error" : email_error})

    def get(self):
        self.write_form()

    def post(self):
        #pulls in inputs
        username = self.request.get("username")
        pw1 = self.request.get("pw1")
        pw2 = self.request.get("pw2")
        email = self.request.get("email")

        #validates inputs and checks passwords match
        ok_username = valid_username(username)
        pw_match = pw1 == pw2
        ok_password = valid_password(pw1)
        ok_email = valid_email(email)

        #if everything is okay we can welcome the new user...
        if ok_username and pw_match and ok_password and ok_email:
            self.redirect("/welcome?username=" + username)
        #but if not we need to get ALL THE ERRORS and send them back to try
        #signing up again
        else:
            error_list = [username]

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

#welcomes a successful new user, with double-checking they have a valid username;
#sends them back to try logging in again if not valid
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        if valid_username(username):
            self.response.write(style_links + welcome_styles + "<div><p>Welcome, %s!</p></div><div id='spinner'></div>" %username)
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
