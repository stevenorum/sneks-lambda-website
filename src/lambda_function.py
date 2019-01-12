from sneks.sam.response_core import PathMatcher, ListMatcher, ResponseException
from sneks.sam import ui_stuff

import handlers

STATIC_MATCHERS = [
    PathMatcher(r"^.*/favicon.ico$", ui_stuff.get_static, {"filename":"static/favicons/favicon.ico"}),
    PathMatcher(r"^/?(?P<filename>static/.*)$", ui_stuff.get_static),
]

STANDARD_PREPROCESSORS = [
]

DYNAMIC_MATCHERS = [
    PathMatcher(r"^/?(index.html)?$", handlers.index_handler, preprocessor_functions=STANDARD_PREPROCESSORS),
    PathMatcher(r".*debug.*", ui_stuff.make_debug, preprocessor_functions=STANDARD_PREPROCESSORS),
    PathMatcher(r".*", ui_stuff.make_404),
]

MATCHERS = ListMatcher(STATIC_MATCHERS + DYNAMIC_MATCHERS)

def lambda_handler(event, context):
    try:
        return MATCHERS.handle_event(event)
    except ResponseException as e:
        return e.response
