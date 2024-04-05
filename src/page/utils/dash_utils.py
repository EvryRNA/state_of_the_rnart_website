from dash import html
import dash_mantine_components as dmc

from src.enums.colors import CYAN


def get_button(text: str, href: str, button_color: str, text_color: str = "white"):
    button = html.Button(
        html.A(
            text,
            href=href,
            style={
                "color": text_color,
                "text-decoration": "none",
            },
            target="_blank",
        ),
        style={
            "color": "inherit",
            "text-decoration": "none",
            "background-color": button_color,
            "border": "black",
            "border-radius": "5px",
            "padding": "10px",
            "margin": "0 auto",
            "display": "block",
            "fontSize": "20px",
        },
    )
    return button


def get_card(img_path: str, title: str, nb_rna: str, text: str, link: str, color: str):
    return dmc.Card(
        children=[
            dmc.CardSection(
                html.Div(
                    dmc.Image(
                        src=img_path, style={"width": "100px", "height": "100px"}
                    ),
                    style={"display": "flex", "justify-content": "center"},
                ),
            ),
            dmc.Group(
                [
                    dmc.Text(
                        title,
                        weight=500,
                        style={"fontSize": 35},
                    ),
                    dmc.Badge(
                        nb_rna,
                        color="blue",
                        variant="light",
                        style={"fontSize": 15},
                    ),
                ],
                position="apart",
                mt="md",
                mb="xs",
            ),
            dmc.Text(
                text,
                size="sm",
                color="black",
                style={
                    "width": "70%",
                    "margin": "0 auto",
                    "textAlign": "center",
                    "fontSize": "25px",
                },
            ),
            html.Hr(style={"height": "10px"}),
            dmc.Anchor(
                dmc.Button(
                    "More information",
                    fullWidth=False,
                    size="lg",
                    radius="md",
                    style={"backgroundColor": color},
                ),
                href=link,
            ),
        ],
        withBorder=True,
        shadow="lg",
        radius="md",
        style={"backgroundColor": CYAN},
    )
