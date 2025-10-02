from fasthtml.common import *
from pages.entry_form import entry_form_page
from pages.user_list import user_list_page

# Initialize FastHTML app
app, rt = fast_app()

# In-memory storage for users
users = []

# ============================================
# PAGE ROUTES
# ============================================

@rt('/')
def get():
    """
    Serves the entry form page (Page 1)
    """
    return entry_form_page()

@rt('/users')
def get():
    """
    Serves the user list page (Page 2)
    """
    return user_list_page()

# ============================================
# API ROUTES
# ============================================

@rt('/api/users')
def post(first_name: str, last_name: str):
    """
    POST endpoint to add a new user
    Accepts first name and last name, adds to in-memory list
    Returns success message
    """
    user = {
        "first_name": first_name,
        "last_name": last_name
    }
    users.append(user)
    
    return P("User added")

@rt('/api/users/count')
def get():
    """
    GET endpoint to retrieve the count of users
    Returns the total number of users
    """
    return P(f"Total entries: {len(users)}")

@rt('/api/users')
def get():
    """
    GET endpoint to retrieve all users
    Returns table of all users
    """
    if not users:
        return P("No users found")
    
    return Table(
        Thead(
            Tr(
                Th("First Name"),
                Th("Last Name")
            )
        ),
        Tbody(
            *[Tr(Td(u["first_name"]), Td(u["last_name"])) for u in users]
        )
    )

serve()