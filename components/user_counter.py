from fasthtml.common import *

def user_counter():
    """
    Component: User Counter
    Displays the count of users, auto-updates via HTMX
    """
    return Div(
        id="counter",
        hx_get="/api/users/count",
        hx_trigger="load, every 1s"
    )