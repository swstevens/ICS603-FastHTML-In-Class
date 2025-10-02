from fasthtml.common import *

def user_table():
    """
    Component: User Table
    Displays list of all users in a table, loads via HTMX
    """
    return Div(
        id="userTable",
        hx_get="/api/users",
        hx_trigger="load",
        hx_swap="innerHTML"
    )