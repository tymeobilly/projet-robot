bitbot.select_model(BBModel.Classic)
let distance = bitbot.sonar(BBPingUnit.Centimeters)
basic.forever(function on_forever() {
    if (distance <= 15) {
        bitbot.stop(BBStopMode.Brake)
        bitbot.rotatems(BBRobotDirection.Left, 60, 400)
    } else {
        bitbot.go(BBDirection.Forward, 60)
    }
    
})
