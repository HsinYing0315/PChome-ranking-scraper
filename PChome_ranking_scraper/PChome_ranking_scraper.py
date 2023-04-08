"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from .scraper import scraper_products

options = ["3C", "周邊", "NB", "通訊", "數位", "家電", "日用", "母嬰", "食品", "生活", "居家", "休閒", "保健", "美妝", "時尚", "書店"]
class State(pc.State):
    """The app state."""
    
    option = "No Selection"
    result: list = ['Nothing yet']
    
    def submit(self, option):
        self.result = scraper_products(option)

def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Choose a type to see its best sells. ", font_size="2em"),
            pc.select(options, 
                      placeholder="Select a type", 
                      on_change=State.set_option),
            pc.button("Submit", 
                      on_click=State.submit(State.option)),
            pc.vstack(
                pc.text(State.result[0]),
                pc.text(State.result[1]),
                pc.text(State.result[2]),
                pc.text(State.result[3]),
                pc.text(State.result[4]),
                pc.text(State.result[5])
            )
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
