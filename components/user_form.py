from fasthtml.common import *

def user_form():
    """
    Component: User Form
    Contains first name, last name inputs and submit button
    """
    return Form(
        Div(
            Label("First Name:", _for="first_name"),
            Input(type="text", id="first_name", name="first_name", required=True)
        ),
        Div(
            Label("Last Name:", _for="last_name"),
            Input(type="text", id="last_name", name="last_name", required=True)
        ),
        Button("Submit", type="submit"),
        hx_post="/api/users",
        hx_target="#message",
        hx_swap="innerHTML"
    )