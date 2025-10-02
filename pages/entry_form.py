from fasthtml.common import *
from components.user_form import user_form
from components.user_counter import user_counter

def entry_form_page():
    """
    Page 1: Entry Form
    Composed of user_form and user_counter components
    """
    return Title("User Entry Form"), Main(
        H1("User Entry Form"),
        
        user_form(),
        
        Hr(),
        
        Div(id="message"),
        user_counter(),

        
        A("View All Entries", href="/users")
    )