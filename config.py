#parameters
inputSize = 500.0
classNum = 80
bBoxLossAlpha = 1.0
sMin = 0.2
sMax = 0.95
boxRatios = [1.0, 1.0, 2.0, 3.0, 0.5, 1.0 / 3.0]
conv4_3Ratios = [1.0, 0.5, 2.0]
conv4_3Scale = 0.07
layerBoxesNum = [3, 6, 6, 6, 6, 6]
negPosRatio = 3

GpuMemory = 0.8

outShapes = None
defaults = None

confidence = 0.1
nmsIOU = 0.5
thresholdIOU = 0.5
nmsNum = 300