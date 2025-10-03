from fasthtml.common import *

def user_row(user, idx):
    """
    Component: User Row
    Creates a single table row for a user with delete button
    Takes a user dict with first_name and last_name, and the index
    """
    return Tr(
        Td(user["first_name"]),
        Td(user["last_name"]),
        Td(
            Button(
                "Delete",
                hx_delete=f"/api/users/{idx}",
                hx_target="closest tr",
                hx_swap="outerHTML"
            )
        ),
        id=f"user-{idx}"
    )