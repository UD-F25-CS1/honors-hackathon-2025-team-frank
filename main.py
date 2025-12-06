from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

from meta import *

set_website_title("Your Drafter Website")
set_site_information(
    author="frankhye@udel.edu",
    description="""Welcome to the HACK INC login page. The
    goal is pretty simple. Log in to your account by typing in
    the password. """,
    sources=["None"],
    planning=["None"],
    links=["None"]
)
hide_debug_information()
set_website_framed(False)
set_website_style("XP")

@dataclass
class State:
    password: str
    attempts: int
    was_solved: bool
    
@route
def index(state: State) -> Page:
    return Page(state,
        [
        "HACK INC v2.0",
        """
        Hello user_2, welcome back to HACK INC.
        As you can see, we had to update our security policy
        due to recent breaches that have occurred on the site.
        Thank you for your understanding."
        """,
        Button(text="Learn More", url="/security_update"),
        "Username: user_2",
        "Password:  ",
        TextBox("user_login", "Fill in here"),
        Button("Continue", password_check, arguments=Argument("text", state.password)),
        Button(text="Close", url="/desktop")
        ])

@route
def desktop(state: State) -> Page:
    return Page(state,
        [
        "Welcome to your desktop!",
        "Owner Name: Nathan Dale",
        "Today's Date: November 15, 2002",
        Button("HACK INC", url="/index"),
        Button("WebMail", url="/webmail"),
        Button("Trash", url="/trash"),
        ]
    )

@route
def trash(state: State) -> Page:
    return Page(state,
        [
        "You have one file in the trash.",
        Button("DO_NOT_CLICK", url="/secret_message"),
        "Will delete in 30 days.",
        Button("Exit", url="/desktop")
        ]
    )

@route
def secret_message(state: State) -> Page:
    return Page(state,
        [
        "Forwarded Message",
        "From: user_9",
        "Subject: h3lp",
        "To: user_1",
        """
         I shall never sleep calmly again when I think of the horrors that lurk ceaselessly behind life in time and in space,
         and of those unhallowed blasphemies from elder stars which dream beneath the sea, known and favoured by a nightmare
         cult ready and eager to loose them upon the world whenever another earthquake shall heave their monstrous stone city
         again to the sun and air.
        """,
        "Who am I?",
        Button("Exit", url="/trash")
        ]
    )

@route
def webmail(state: State) -> Page:
    return Page(state,
        [
        "You have no unread messages.",
        Button("View Read Messages", url="/read_messages"),
        Button(text="Close", url="/desktop"),
        ]
    )

@route
def read_messages(state: State) -> Page:
    return Page(state,
        [
        Button("What up! - November 10, 2002", url="/what_up"),
        "",
        Button("Important Message - November 5, 2002", url="/important_message"),
        "",
        Button("Need Help With...That Assignment - November 4, 2002", url="/need_help"),
        "",
        Button("Hey son. - October 31, 2002", url="/hey_son"),
        "",
        Button("Close", url="/webmail")
        ]
    )

@route
def what_up(state: State) -> Page:
    return Page(state,
        [
        "Hey bud,",
        """
        So I just heard you’re going to be in town in a couple of weeks—seriously? That’s awesome. It feels like forever since we’ve actually seen each other in person.
        If you’ve got time while you’re here, do you want to hang out? No pressure or anything, but it’d be great to catch up. Maybe grab coffee, wander around the old spots, relive our glory days of getting into trouble for absolutely nothing… you know, the classics.
        """,
        "Just let me know what your schedule looks like. It’d be really nice to see you again.",
        "- Amelia",
        Button("Close", url="/read_messages")
        ]
    )

@route
def important_message(state: State) -> Page:
    return Page(state,
        [
        "Dear user_2,",
        """
        I’ve been informed by user_3 that you are willing to participate in the special assignment we discussed last quarter. I appreciate your discretion—this project requires a level of confidentiality and precision that not everyone in the department can provide.
        You will be receiving restricted-access files shortly. Review them carefully and provide user_3 with any support they request. The timeline is aggressive, and I expect progress without delays.
        Remember: this initiative does not appear on any public roadmap. Do not share or reference it outside the approved chain.
        """,
        "Thank you for your cooperation.",
        "Sincerely",
        "Management",
        Button("Close", url="/read_messages")
        ]
    )

@route
def need_help(state: State) -> Page:
    return Page(state,
        [
        "Hey,",
        """
        So, uh—about that “special” project the boss dumped on me yesterday. I’m trying to get it up and running, but some of the code he handed over doesn’t make sense. Parts of it don’t even look like anything we officially work on.
        Can you take a look when you get a minute? Don’t mention this to anyone else. The boss was very clear that this stays between us—“off the books,” his words, not mine.
        I’ll send you the files once you say you’re in. And seriously, keep this quiet. I don’t want to get dragged into something I don’t understand alone. I'm sorry to ask this of you,
        especially since you're going to be on leave to visit your parents. But please, I need help.
        """,
        "Sincerely",
        "Sam",
        Button("Close", url="/read_messages")
        ]
    )

@route
def hey_son(state: State) -> Page:
    return Page(state,
        [
        "Hi sweetheart,",
        """
       I hope this message actually reaches you. It feels like ages since we last heard your voice. Your father and I know your new job at HACK INC keeps you busy, but we miss you more than you probably realize. The house has been so quiet lately, and we keep catching ourselves waiting for the phone to ring.
       I’m proud of you—both of us are—but I worry. You’ve always thrown yourself into your work, but this time it seems like the job has swallowed your whole schedule. I just want to make sure you’re taking care of yourself, eating real meals, getting some sleep…I remember how I had to nag about it when you
       were just a boy.
       Thanksgiving is coming up, and your father asked me again this morning if you might be able to come home to Oakland this year. We’d love nothing more than to have you at the table with us. Even if it’s just for a day or two, it would mean the world.
       Please write back when you can. Just a few lines to let us know you’re okay.
        """,
        "We love you. Always",
        "Mom",
        Button("Close", url="/read_messages")
        ]
    )

@route
def security_update(state: State) -> Page:
    return Page(state,
        [
        "Security Update",
        """
        Recently, on November 12, 2002, our website experienced an unauthorized intrusion that temporarily compromised portions of our service. It’s believed that this malicious third-party had got into the website after stealing the laptop of one of our developers. Thankfully, our team has acted quickly to contain the incident, investigate the breach, and restore normal operation.
        We want to assure all users that no payment information was accessed. However, some account details may have been viewed by the attacker. Out of caution, we are requiring password resets for all users and have implemented several new security measures, including multi-factor authentication, upgraded encryption standards, and continuous monitoring.
        We know this incident may have caused concern, and we appreciate your patience. Protecting your data is our highest priority, and we’re committed to preventing anything like this from happening again.
        """,
        "If you notice any suspicious activity, please contact our support team immediately.",
        "Thank you for your trust.",
        Button("Return", url="/index")
        ]
    )

@route
def password_check(state: State, user_login: str) -> Page:
    if user_login == state.password:
        state.attempts += 1
        state.was_solved = not state.was_solved
        return victory(state)
    else:
        state.attempts += 1
        return incorrect(state)

@route
def victory(state: State) -> Page:
    return Page(
        state,
        content=[
            "Congratulations, you logged in!",
            "Thank you for playing!",
            "Attempts:", str(state.attempts),
            Button(text="Logout", url="/index")
        ]
    )

@route
def incorrect(state: State) -> Page:
    return Page(
        state,
        content=[
            "Incorrect!",
            Button(text="Forgot My Password", url="/forgot_my_password"),
            Button(text="Return", url="/index")
        ],
    )

@route
def forgot_my_password(state: State) -> Page:
    return Page(
        state,
        content=[
            "We sent an email with a link to update your password.",
            Button(text="Close", url="/new_desktop"),
            ]
        )

@route
def new_desktop(state: State) -> Page:
    return Page(state,
        [
        "Welcome to your desktop!",
        "Owner Name: Nathan Dale",
        "Today's Date: November 15, 2002",
        Button("HACK INC", url="/index"),
        Button("WebMail", url="/new_webmail"),
        Button("Trash", url="/new_trash"),
        ]
    )

@route
def new_trash(state: State) -> Page:
    return Page(state,
        [
        "You have one file in the trash.",
        Button("DO_NOT_CLICK", url="/new_secret_message"),
        "Will delete in 30 days.",
        Button("Exit", url="/new_desktop")
        ]
    )

@route
def new_secret_message(state: State) -> Page:
    return Page(state,
        [
        "Forwarded Message",
        "From: user_9",
        "Subject: h3lp",
        "To: user_1",
        """
         I shall never sleep calmly again when I think of the horrors that lurk ceaselessly behind life in time and in space,
         and of those unhallowed blasphemies from elder stars which dream beneath the sea, known and favoured by a nightmare
         cult ready and eager to loose them upon the world whenever another earthquake shall heave their monstrous stone city
         again to the sun and air.
        """,
        "Who am I?",
        Button("Exit", url="/new_trash")
        ]
    )

@route
def password_reset(state: State) -> Page:
    return Page(state,
        [
        "Hello user_2,",
        "You have requested a change to your password.",
        """
        But first, we need to verify that it is you.
        You have given us security questions to help verify
        your identity. Please answer the questions to change
        the password.
        """,
        "Please click the link below to get started.",
        Button("Begin", url="/question_one")
        ]
    )

@route
def new_webmail(state: State) -> Page:
    return Page(state,
        [
        "You have one unread message.",
        Button("Password Reset - November 15, 2002", url="/password_reset"),
        Button("View Read Messages", url="/new_read_messages"),
        Button(text="Close", url="/new_desktop")
        ]
    )


def town_check(user_input: str) -> Page:
    first_lock = False
    if user_input == "Oakland":
        first_lock = not first_lock
        return first_lock
    else:
        return first_lock
    
@route
def question_one_check(state: State, first_user_input: str) -> Page:
    if town_check(first_user_input):
        return question_two(state)
    else:
        return Page(
        state,
        content=[
           "Question #1",
           "Oops, you got it wrong.",
           "What is the name of your hometown?",
        Button("Continue", question_one_check, arguments=Argument("text", state.password)),
        Button(text="Close", url="/new_desktop")
        ])
    
@route
def question_one(state: State) -> Page:
    return Page(
        state,
        content=[
           "Question #1",
           "What is the name of your hometown?",
           TextBox("first_user_input", ""),
        Button("Continue", question_one_check, arguments=Argument("text", state.password)),
        Button(text="Close", url="/new_desktop")
        ])

def friend_check(user_input: str) -> Page:
    second_lock = False
    if user_input == "Amelia":
        second_lock = not second_lock
        return second_lock
    else:
        return second_lock

@route
def question_two_check(state: State, second_user_input: str) -> Page:
    if friend_check(second_user_input):
        return question_three(state)
    else:
        return Page(
        state,
        content=[
           "Question #2",
           "Oops, you got it wrong.",
           "Who was your childhood crush?",
        Button("Continue", question_two_check, arguments=Argument("text", state.password)),
        Button(text="Close", url="/new_desktop")
        ])

@route
def question_two(state: State) -> Page:
    return Page(
        state,
        content=[
           "Question #2",
           "Who was your childhood crush?",
           TextBox("second_user_input", ""),
        Button("Continue", question_two_check, arguments=Argument("text", state.password)),
        Button(text="Close", url="/new_desktop")
        ])

def final_check(user_input: str) -> Page:
    third_lock = False
    if user_input == "Abdul Alhazred":
        third_lock = not third_lock
        return third_lock
    else:
        return third_lock

@route
def question_three_check(state: State, third_user_input: str) -> Page:
    if final_check(third_user_input):
        return new_password(state)
    else:
        return Page(
        state,
        content=[
           "Question #3",
           "Oops, you got it wrong.",
           "You don't get to try again.",
        Button("...", url="/bad_end")
        ])

@route
def bad_end(state: State):
   return Page(
        state,
        content=[
            "You got the bad ending."
        ]) 


@route
def question_three(state: State) -> Page:
    return Page(
        state,
        content=[
            "Question #3",
            "Who am I?",
            TextBox("third_user_input", ""),
        Button("Continue", question_three_check, arguments=Argument("text", state.password)),
        Button(text="Close", url="/new_desktop")
        ])

@route
def password_change(state: State, password_fill_in: str) -> Page:
    state.password = password_fill_in
    return Page(
        state,
        content=[
        "You changed your password. Go back to the website to login.",
        Button("Return", url="/index")
        ]
    )

@route
def new_password(state: State):
    return Page(
        state,
        content=[
        "Fill in your new password.",
        TextBox("password_fill_in", ""),
        Button("Continue", password_change, arguments=Argument("text", state.password))
        ]
    )

@route
def new_read_messages(state: State) -> Page:
    return Page(state,
        [
        Button("What up! - November 10, 2002", url="/new_what_up"),
        "",
        Button("Important Message - November 5, 2002", url="/new_important_message"),
        "",
        Button("Need Help With...That Assignment - November 4, 2002", url="/new_need_help"),
        "",
        Button("Hey son. - October 31, 2002", url="/new_hey_son"),
        "",
        Button("Close", url="/new_webmail")
        ]
    )

@route
def new_what_up(state: State) -> Page:
    return Page(state,
        [
        "Hey bud,",
        """
        So I just heard you’re going to be in town in a couple of weeks—seriously? That’s awesome. It feels like forever since we’ve actually seen each other in person.
        If you’ve got time while you’re here, do you want to hang out? No pressure or anything, but it’d be great to catch up. Maybe grab coffee, wander around the old spots, relive our glory days of getting into trouble for absolutely nothing… you know, the classics.
        """,
        "Just let me know what your schedule looks like. It’d be really nice to see you again.",
        "- Amelia",
        Button("Close", url="/new_read_messages")
        ]
    )

@route
def new_important_message(state: State) -> Page:
    return Page(state,
        [
        "Dear user_2,",
        """
        I’ve been informed by user_3 that you are willing to participate in the special assignment we discussed last quarter. I appreciate your discretion—this project requires a level of confidentiality and precision that not everyone in the department can provide.
        You will be receiving restricted-access files shortly. Review them carefully and provide user_3 with any support they request. The timeline is aggressive, and I expect progress without delays.
        Remember: this initiative does not appear on any public roadmap. Do not share or reference it outside the approved chain.
        """,
        "Thank you for your cooperation.",
        "Sincerely",
        "Management",
        Button("Close", url="/new_read_messages")
        ]
    )

@route
def new_need_help(state: State) -> Page:
    return Page(state,
        [
        "Hey,",
        """
        So, uh—about that “special” project the boss dumped on me yesterday. I’m trying to get it up and running, but some of the code he handed over doesn’t make sense. Parts of it don’t even look like anything we officially work on.
        Can you take a look when you get a minute? Don’t mention this to anyone else. The boss was very clear that this stays between us—“off the books,” his words, not mine.
        I’ll send you the files once you say you’re in. And seriously, keep this quiet. I don’t want to get dragged into something I don’t understand alone. I'm sorry to ask this of you,
        especially since you're going to be on leave to visit your parents. But please, I need help.
        """,
        "Sincerely",
        "Sam",
        Button("Close", url="/new_read_messages")
        ]
    )

@route
def new_hey_son(state: State) -> Page:
    return Page(state,
        [
        "Hi sweetheart,",
        """
       I hope this message actually reaches you. It feels like ages since we last heard your voice. Your father and I know your new job at HACK INC keeps you busy, but we miss you more than you probably realize. The house has been so quiet lately, and we keep catching ourselves waiting for the phone to ring.
       I’m proud of you—both of us are—but I worry. You’ve always thrown yourself into your work, but this time it seems like the job has swallowed your whole schedule. I just want to make sure you’re taking care of yourself, eating real meals, getting some sleep…I remember how I had to nag about it when you
       were just a boy.
       Thanksgiving is coming up, and your father asked me again this morning if you might be able to come home to Oakland this year. We’d love nothing more than to have you at the table with us. Even if it’s just for a day or two, it would mean the world.
       Please write back when you can. Just a few lines to let us know you’re okay.
        """,
        "We love you. Always",
        "Mom",
        Button("Close", url="/new_read_messages")
        ]
    )

start_server(State("P@55w0rd", 0, False))
