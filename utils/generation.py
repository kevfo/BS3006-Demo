from flask import render_template

def construct_route(page):
    '''
    Construct a route for a function - for use in initial pages.
    '''
    def route_handler():
        return render_template(page)
    return route_handler