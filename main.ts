input.onButtonPressed(Button.A, function () {
    sprite.change(LedSpriteProperty.Y, -2)
    sprite2.change(LedSpriteProperty.Y, -2)
    basic.pause(2 * temps)
    sprite.change(LedSpriteProperty.Y, 2)
    sprite2.change(LedSpriteProperty.Y, 2)
})
let temps = 0
let sprite2: game.LedSprite = null
let sprite: game.LedSprite = null
sprite = game.createSprite(3, 4)
sprite2 = game.createSprite(3, 3)
let obstacle = game.createSprite(0, 4)
temps = 500
let niv = 1
basic.forever(function () {
    basic.showString("" + (niv))
    for (let index = 0; index < 6; index++) {
        for (let index = 0; index <= 4; index++) {
            obstacle.set(LedSpriteProperty.X, index)
            basic.pause(temps)
        }
    }
    temps = temps * 0.9
    niv = 1
})
basic.forever(function () {
    if (sprite.isTouching(obstacle)) {
        game.gameOver()
    }
})
