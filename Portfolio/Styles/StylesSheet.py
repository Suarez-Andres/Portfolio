from enum import Enum
import reflex as rx

#Constants
class cons(Enum):
    MAIL="suareza611@hotmail.com"
    LINKEDIN_URL="https://www.linkedin.com/in/andrés-suárez-747922255"
    GITHUB_URL="https://github.com/Suarez-Andres"

#Sizes
class spaces(Enum):
    SMALL="0.5em"
    DEFAULT="1em"
    LARGE="2em"

#Colors
class colors(Enum):
    BACKGROUND = "#0a3143"
    IMPORTANT = "#276e90"
    TITLE = "#efefef"
    PARAGRAPH = "#cecfc9"

#fonts
class fonts(Enum):
    TEXT = "Poppins"
    TITLE = "Poppins"

class f_weight(Enum):
    LIGHT = "300"
    BOLD = "700"

#Remote fonts
FONTS = [
    "https://fonts.googleapis.com/css2?family=Poppins:weight@300;700&display=swap"
]

#default styles
DEF_STYLES = {
    "background_color":colors.BACKGROUND.value,
    rx.Heading: {
        "font_family": fonts.TITLE.value,
        "font_weight": f_weight.BOLD.value,
        "color": colors.TITLE.value,
        "white_space": "normal"
    },
    rx.Text: {
        "font_family": fonts.TEXT.value,
        "font_weight": f_weight.LIGHT.value,
        "font_size": "18px",
        "color": colors.PARAGRAPH.value,
        "white_space": "normal"
    },
    rx.Button: {
        "width":"100%",
        "height":"100%",
        #"display":"block",
        "padding":spaces.SMALL.value,
        "border_radius":spaces.DEFAULT.value,
        "color":colors.BACKGROUND.value,
        "background_color":colors.PARAGRAPH.value,
        "white_space": "normal"
    },
    rx.Link: {
        "text_decoration":"none",
        "white_space": "normal",
        "_hover": {}
    },
    rx.ListItem: {
        "font_family": fonts.TEXT.value,
        "font_weight": f_weight.LIGHT.value,
        "color": colors.PARAGRAPH.value,
        "white_space": "normal"
    },
    rx.Card: {
        "padding": 5,
        "background_color":colors.IMPORTANT.value,
        "white_space": "normal"
    }
}