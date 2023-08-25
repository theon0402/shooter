# -*- coding: utf-8 -*-
import stage

stage = stage.Stage()

running = True
while running:
    running = stage.run()
    stage.tick()

stage.halt()