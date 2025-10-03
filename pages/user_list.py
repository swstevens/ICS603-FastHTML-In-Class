from fasthtml.common import *
from components.user_table import user_table

def user_list_page(users):
    """
    Page 2: User List
    Composed of user_table component
    """
    return Title("User List"), Main(
        H1("All Users"),
        
        user_table(users),  # Pass the users list
        
        A("Back", href="/")
    )