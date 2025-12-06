"""
Tests for your Drafter website.
"""

from drafter import *
from bakery import assert_equal

# do_not_start_server(): Prevent the server from starting during tests
get_main_server().configuration.skip = True

from main import *

## You can add your tests below this line

assert_equal(
 question_one(State(password='P@55w0rd', attempts=1, was_solved=False)),
 Page(state=State(password='P@55w0rd', attempts=1, was_solved=False),
     content=['Question #1',
              'What is the name of your hometown?',
              TextBox(name='first_user_input', kind='text', default_value=''),
              Button(text='Continue', url='/question_one_check', arguments=Argument(name='text', value='P@55w0rd')),
              Button(text='Close', url='/new_desktop')]))

assert_equal(
 new_webmail(State(password='P@55w0rd', attempts=1, was_solved=False)),
 Page(state=State(password='P@55w0rd', attempts=1, was_solved=False),
     content=['You have one unread message.',
              Button(text='Password Reset - November 15, 2002', url='/password_reset'),
              Button(text='View Read Messages', url='/new_read_messages'),
              Button(text='Close', url='/new_desktop')]))

assert_equal(
 new_desktop(State(password='P@55w0rd', attempts=1, was_solved=False)),
 Page(state=State(password='P@55w0rd', attempts=1, was_solved=False),
     content=['Welcome to your desktop!',
              'Owner Name: Nathan Dale',
              "Today's Date: November 15, 2002",
              Button(text='HACK INC', url='/'),
              Button(text='WebMail', url='/new_webmail'),
              Button(text='Trash', url='/new_trash')]))

assert_equal(
 forgot_my_password(State(password='P@55w0rd', attempts=1, was_solved=False)),
 Page(state=State(password='P@55w0rd', attempts=1, was_solved=False),
     content=['We sent an email with a link to update your password.', Button(text='Close', url='/new_desktop')]))

assert_equal(
 question_one_check(State(password='P@55w0rd', attempts=1, was_solved=False), 'Lusaka'),
 Page(state=State(password='P@55w0rd', attempts=1, was_solved=False),
     content=['Question #1',
              'Oops, you got it wrong.',
              'What is the name of your hometown?',
              Button(text='Continue', url='/question_one_check', arguments=Argument(name='text', value='P@55w0rd')),
              Button(text='Close', url='/new_desktop')]))

assert_equal(
 password_check(State(password='P@55w0rd', attempts=0, was_solved=False), 'Fill in here'),
 Page(state=State(password='P@55w0rd', attempts=1, was_solved=False),
     content=['Incorrect!',
              Button(text='Forgot My Password', url='/forgot_my_password'),
              Button(text='Return', url='/')]))

assert_equal(
 password_reset(State(password='P@55w0rd', attempts=1, was_solved=False)),
 Page(state=State(password='P@55w0rd', attempts=1, was_solved=False),
     content=['Hello user_2,',
              'You have requested a change to your password.',
              '\n'
              '        But first, we need to verify that it is you.\n'
              '        You have given us security questions to help verify\n'
              '        your identity. Please answer the questions to change\n'
              '        the password.\n'
              '        ',
              'Please click the link below to get started.',
              Button(text='Begin', url='/question_one')]))

assert_equal(
 index(State(password='P@55w0rd', attempts=0, was_solved=False)),
 Page(state=State(password='P@55w0rd', attempts=0, was_solved=False),
     content=['HACK INC v2.0',
              '\n'
              '        Hello user_2, welcome back to HACK INC.\n'
              '        As you can see, we had to update our security policy\n'
              '        due to recent breaches that have occurred on the site.\n'
              '        Thank you for your understanding."\n'
              '        ',
              Button(text='Learn More', url='/security_update'),
              'Username: user_2',
              'Password:  ',
              TextBox(name='user_login', kind='text', default_value='Fill in here'),
              Button(text='Continue', url='/password_check', arguments=Argument(name='text', value='P@55w0rd')),
              Button(text='Close', url='/desktop')]))
