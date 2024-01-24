from pizazz.pizazz import HC595
import time

towerA = HC595(mode="BCM", data=16, clock=21, latch=20, ics=2)
layers = HC595(mode="BCM", data=13, clock=6, latch=5, ics=2)

cube = [[[1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0], 
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0]],
        [[1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0]],
        [[1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0], 
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0], 
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0]],
        [[1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0], 
         [1, 1, 1, 1, 0, 0, 0, 0], 
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0], 
         [1, 1, 1, 1, 0, 0, 0, 0]],
        [[1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0]],
        [[1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0], 
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0]],
        [[1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0], 
         [1, 1, 1, 1, 1, 1, 1, 0]],
        [[1, 1, 1, 1, 1, 1, 1, 1], 
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1], 
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1]],
        [[1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1], 
         [1, 1, 1, 1, 1, 1, 1, 1], 
         [1, 1, 1, 1, 1, 1, 1, 1], 
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1]],
        [[1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0], 
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 0]],
        [[1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0], 
         [1, 1, 1, 1, 1, 1, 0, 0], 
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0]],
        [[1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 0, 0, 0]],
        [[1, 1, 1, 1, 0, 0, 0, 0], 
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0], 
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0]],
        [[1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0], 
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0]], 
        [[1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0]],
        [[1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0], 
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0]]]


layerPatterns = [[[0, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 0, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 0, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 0, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 0, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 0, 1],[1, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 1],[1, 0, 1, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 1, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 0, 1, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 0, 1, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 0, 1, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 0, 1]],
                 [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 0]],
                 ]

while True:              
	for i in range (16):
		for x in range (0,8,2):
			towerA.set_pattern(cube[i][x:x+2])
			print(cube[i][x:x+2])
		layers.set_pattern(layerPatterns[i])
		print(layerPatterns[i])
		
		#towerA.set_pattern(row)
		#print(row)
		#time.sleep(0.0)
