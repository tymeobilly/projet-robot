bitbot.select_model(BBModel.CLASSIC)
distance = bitbot.sonar(BBPingUnit.CENTIMETERS)

def on_forever():
    if distance <= 15:
        bitbot.stop(BBStopMode.BRAKE)
        bitbot.rotatems(BBRobotDirection.LEFT, 60, 400)
    else:
        bitbot.go(BBDirection.FORWARD, 60)
basic.forever(on_forever)
