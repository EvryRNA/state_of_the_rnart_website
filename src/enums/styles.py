from src.enums.colors import HEADER_COLOR, WHITE

NO_PADDING = {
    "padding": "0px",
    "margin": "0px",
    "background-color": WHITE,
}

CONTAINER_STYLE = {
    "display": "flex",
    "justifyContent": "start",
    "width": "100%",
    "height": "100%",
}
HEADER_STYLE = {
    "display": "flex",
    "justifyContent": "space-between",
    "alignItems": "center",
    "border-bottom": "solid black 3px",
    "border": f"1px solid {HEADER_COLOR}",
    "background-color": HEADER_COLOR,
}
FOOTER_STYLE = {
    "display": "inline-block",
    "width": "50%",
    "text-align": "center",
}

ANIMATION_STYLE = {
    "position": "absolute",
    "left": "50%",
    "top": "50%",
    "z-index": 20,
    "width": "600px",
    "height": "500px",
    "margin-left": "-300px",
    "margin-top": "-250px",
    "border-radius": "40%",
}
STYLE_H = {
    "fontSize": "35px",
    "fontWeight": "bold",
    "border-radius": "1px",
    "color": "black",
}
BUTTON_STYLE = {
    "border": "2px solid black",
    "border-radius": "8px",
    "box-sizing": "border-box",
    "cursor": "pointer",
    "display": "inline-block",
    "font-size": "26px",
    "font-weight": "600",
    "line-height": "30px",
    "margin": "0",
    "outline": "none",
    "padding": "13px 23px",
    "position": "relative",
    "text-align": "center",
    "text-decoration": "none",
    "touch-action": "manipulation",
    "transition": "box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s",
    "user-select": "none",
    "-webkit-user-select": "none",
    "width": "auto",
}
STYLE_SCORE = {
    "fontSize": "25px",
    "color": "#0766AD",
    "border-radius": "1px",
}
BUTTON_STYLE = {
    "color": "inherit",
    "text-decoration": "none",
    "border": "2px solid black",
    "border-radius": "5px",
    "padding": "10px",
    "margin": "0 auto",
    "display": "block",
    "fontSize": "20px",
}
