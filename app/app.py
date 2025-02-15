from fasthtml.common import *
from monsterui.all import *

# Choose a theme color (blue, green, red, etc)
hdrs = Theme.slate.headers()

# Create your app with the theme
app, rt = fast_app(
    hdrs=hdrs,
    live=True
)

clubs = [
    {"name": "Rebel", "cover": "$20", "img": "https://picsum.photos/400/100?random=1"},
    {"name": "EFS", "cover": "$25", "img": "https://picsum.photos/400/100?random=2"},
    {"name": "Lost & Found", "cover": "$15", "img": "https://picsum.photos/400/100?random=3"},
    {"name": "CODA", "cover": "$20", "img": "https://picsum.photos/400/100?random=4"},
    {"name": "Vertigo", "cover": "$20", "img": "https://picsum.photos/400/100?random=5"},
    {"name": "The Fifth Social Club", "cover": "$25", "img": "https://picsum.photos/400/100?random=6"},
    {"name": "Toybox", "cover": "$15", "img": "https://picsum.photos/400/100?random=7"},
    {"name": "Wildflower", "cover": "$20", "img": "https://picsum.photos/400/100?random=8"},
    {"name": "Cube", "cover": "$15", "img": "https://picsum.photos/400/100?random=9"},
    {"name": "Uniun", "cover": "$20", "img": "https://picsum.photos/400/100?random=10"},
]

def ClubCard(p):
    return Card( 
        Img(src=p["img"], alt=p["name"], style="width:100%"),
        H4(p["name"], cls="mt-2"), 
        P(p["cover"], cls=TextPresets.bold_sm), 
        Button(
            "Click me!", 
            cls=(ButtonT.primary, "mt-2"),  
            hx_get=club_detail.to(club_name=p['name']),
            hx_push_url='true',
            hx_target='body'
            )
        )

@rt
def index():
    return Titled(
        "Night Life Guide App!",
        Grid(*[ClubCard(p) for p in clubs], cols_lg=3)
    )

example_club_description = """\n
This is a sample detailed description of the {club_name} night club.  You can see when clicking on the card
from the gallery you can:

+ Have a detailed description of the club on the page
+ Have an order form to fill out and submit a booking
+ Anything else you want!
"""

@rt
def club_detail(club_name:str):
    return Titled("Club Detail",
        Grid( 
            Div(
                H1(club_name),
                render_md(example_club_description.format(club_name=club_name))
            ),
            Div(
                H3("Order Form"),
                Form( 
                    LabelInput("Name", id='name'), 
                    LabelInput("Email", id='email'),
                    LabelInput("Quantity", id='quantity'),
                    Button("Submit", cls=ButtonT.primary)
                )    
            ),
        cols_lg=2
        )
    ) 

serve()