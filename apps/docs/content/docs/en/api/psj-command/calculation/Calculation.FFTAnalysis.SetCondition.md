---
title: "Calculation.FFTAnalysis.SetCondition()"
description: "Perform a FFT analysis"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FFTAnalysis > SetCondition"
macro _link: "[PostFFTConditionOut](../../macro/calculation/PostFFTConditionOut)"
---

## Description

Perform a FFT analysis.

## Syntax

```psj
Calculation.FFTAnalysis.SetCondition(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"BORE _1" -->
### `strName`

- The name of bore cylinder.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target parts to perform FFT analysis.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crl2DElems`

- The selected 2D elements.

<!-- @since:5.1.0 @type:Double @optional @default:20.0 -->
### `dAngle`

- The angle to extract the target cylinder surface.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTopNode`

- The node to determine the top end of the bore cylinder surface.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crBottomNode`

- The node to determine the bottom end of the bore cylinder surface. To define the bore height also.

<!-- @since:5.1.0 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlCenterPoint`

- The center coordinate of the bore coordinate system.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dBoreRadius`

- The radius of the bore cylinder.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dBoreHeight`

- The height of the bore cylinder.

<!-- @since:5.1.0 @type:Integer @optional @default:3 -->
### `iAxisDirection`

- The bore cylinder axial direction in global coordinate system X, Y, Z or arbitrary direction (user defined).

<!-- @since:5.1.0 @type:Double List @optional @default:[0.0,0.0,0.0] -->
### `dlAxisDefined`

- The defined bore cylinder axial direction.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iDepthDirection`

- The depth direction.

<!-- @since:5.1.0 @type:Integer @optional @default:36 -->
### `iNumOfLayerPoint`

- The number of calculation points in one layer.

<!-- @since:5.1.0 @type:List[Double] @optional @default:[] -->
### `dlLayers`

- The number of layers and depth value at each layer.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iCalculationMethod`

- The calculation method.
  - 0: Best Fit Circle
  - 1: Best Fit Cylinder

<!-- @since:5.1.0 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlAxisX`

- The X axial direction of the the bore cylinder.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing FFT condition
  - If this parameter is used, the specified FFT condition will be modified.
  - If it is left None, a new FFT condition will be created.

## Return Code

A _Cursor_ specifying the created FFT condition.

## Sample Code

```psj {8-13}
# Please set path to your sample file.
filePath="C:/Temp/Sample..."

# Prepare result model
Home.ImportResults.ADVC(filePath, iImportType=1, dFaceAngle=60, dEdgeAngle=60)

# Set FFT condition
FFTCondition = Calculation.FFTAnalysis.SetCondition(crlTargets=[Elem(...)], crl2DElems=[Elem(...)], 
                                    crTopNode=RONode(7584), crBottomNode=RONode(9717), 
                                    dlCenterPoint=[207.65, -190.85, 191.06], dBoreRadius=49.8668, 
                                    dBoreHeight=170.105, dlAxisDefined=[0.0, 0.71, -0.71], 
                                    iDepthDirection=-1, iNumOfLayerPoint=20, 
                                    dlLayers=[0.0, 56.7015, 113.403, 170.105], dlAxisX=[0.14, 0.7, 0.7])
JPT.Debugger(FFTCondition)
```
