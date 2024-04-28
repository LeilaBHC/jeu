def on_button_pressed_a():
    sprite.change(LedSpriteProperty.Y, -2)
    sprite2.change(LedSpriteProperty.Y, -2)
    basic.pause(2 * temps)
    sprite.change(LedSpriteProperty.Y, 2)
    sprite2.change(LedSpriteProperty.Y, 2)
input.on_button_pressed(Button.A, on_button_pressed_a)

temps = 0
sprite2: game.LedSprite = None
sprite: game.LedSprite = None
sprite = game.create_sprite(3, 4)
sprite2 = game.create_sprite(3, 3)
obstacle = game.create_sprite(0, 4)
temps = 500
niv = 1

def on_forever():
    global temps, niv
    basic.show_string("" + str((niv)))
    for index in range(6):
        for index2 in range(5):
            obstacle.set(LedSpriteProperty.X, index2)
            basic.pause(temps)
    temps = temps * 0.9
    niv = 1
basic.forever(on_forever)

def on_forever2():
    if sprite.is_touching(obstacle):
        game.game_over()
basic.forever(on_forever2)
