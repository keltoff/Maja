import ezpygame_fixed as ez
from menu import Menu
from battle import Battle


app = ez.Application(
    title='Maja',
    resolution=(1280, 720),
    update_rate=60,
)
main_menu = Battle()
app.run(main_menu)