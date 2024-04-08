from src.enums.links import TIMELINE_TEXT
from src.page.abstract_page import AbstractPage
import dash_mantine_components as dmc
from dash import html


class Models(AbstractPage):
    def get_page(self):
        return html.Div(
            children=[
                html.H2(
                    "Models",
                    style={
                        "text-align": "center",
                        "color": "black",
                        "font-size": "45px",
                    },
                ),
                self.get_timeline(),
            ],
            style={
                "width": "100%",
                "height": "100%",
                "padding": "0px",
                "margin": "0 auto",
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center",
            },
        )

    def get_time_item(
        self,
        title: str,
        text: str,
        year: str,
        input: str,
        method: str,
        paper: str,
        code: str,
        web_server: str,
    ):
        return dmc.TimelineItem(
            title=title,
            children=[
                dmc.Text(year, style={"font-size": "25px"}),
                dmc.Text(text, color="dimmed", style={"font-size": "20px"}),
                self._get_text("Input", input),
                self._get_text("Method", method),
                dmc.Text(
                    children=[
                        dmc.Anchor(
                            "Original paper", href=paper, style={"font-size": "22px"}
                        ),
                        dmc.Anchor(
                            "Code", href=code, size="m", style={"font-size": "22px"}
                        ),
                        dmc.Anchor(
                            "Web server",
                            href=web_server,
                            size="m",
                            style={"font-size": "22px"},
                        ),
                    ],
                    style={"display": "flex", "justify-content": "space-between"},
                ),
                html.Hr(style={"height": "10px"}),
            ],
            style={
                "margin": "0 auto",
                "width": "30%",
                "font-size": "30px",
            },
        )

    def _get_text(self, title: str, text: str):
        return dmc.Text(
            [
                dmc.Text(f"{title}:", style={"font-size": "25px", "display": "inline"}),
                dmc.Text(
                    f" {text}",
                    color="dimmed",
                    style={"font-size": "22px", "display": "inline"},
                ),
            ]
        )

    def get_timeline(self):
        output = dmc.Timeline(
            active=len(TIMELINE_TEXT),
            bulletSize=30,
            lineWidth=10,
            children=[
                self.get_time_item(**info) for info in list(TIMELINE_TEXT.values())
            ],
        )
        return output
