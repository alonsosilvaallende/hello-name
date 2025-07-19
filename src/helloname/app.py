from textual.app import App, ComposeResult
from textual.widgets import Label, Input
from textual import on

class HelloNameApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Write your name")
        yield Label()

    @on(Input.Changed)
    def add_name(self, event: Input.Changed) -> None:
        self.query_one(Label).update(f"Hello, {event.value}!")

def main():
    app = HelloNameApp()
    app.run()

if __name__ == "__main__":
    main()
