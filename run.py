#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    primfeed view_feed
    primfeed post <title> <body>
    primfeed comment <postId> <title> <body>
    primfeed (-i | --interactive)
    primfeed (-h | --help | --version)
Options:
    view_feed Returns a list of all posts
    post  adds a new post
    <title>  represents the title of the new resource
    <body>  represents the body of the new resource
    comment  adds a new comment to a post, see postid
    <postId>  specifies the post id
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

"""

import sys
import cmd
from docopt import docopt, DocoptExit
from App.view_posts import view_posts
from App.add_post import add_post
from App.comment_post import comment_post


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to Phoenix news Feed!' \
        + ' (type help for a list of commands.)'
    prompt = 'primfeed '

    @docopt_cmd
    def do_view_feed(self, arg):
        """Usage: view_feed"""

        view_posts()

    @docopt_cmd
    def do_post(self, arg):
        """Usage: post <title> <body>"""

        add_post(title=arg['title'], body=arg['body'])

    @docopt_cmd
    def do_commit(self, arg):
        """Usage: comment <postId> <title> <body>"""

        comment_post(post_id=(arg['postId']), title=arg['title'], body=arg['body'] )

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
