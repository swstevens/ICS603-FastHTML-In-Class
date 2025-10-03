from fasthtml.common import *
from components.user_row_entry import user_row

def user_table(users):
    """
    Component: User Table
    Displays list of all users in a table
    Takes a list of user dictionaries and renders each using the user_row component
    """
    if not users:
        return Div(
            P("No users found"),
            id="userTable"
        )
    
    return Div(
        Table(
            Thead(
                Tr(
                    Th("First Name"),
                    Th("Last Name"),
                    Th("Action")
                )
            ),
            Tbody(
                *[user_row(u, idx) for idx, u in enumerate(users)]
            )
        ),
        id="userTable"
    )