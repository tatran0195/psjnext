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

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of bore cylinder.
- The default value is "BORE\_1".

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify the target parts to perform FFT analysis.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crl2DElems

- Specify the selected 2D elements.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dAngle

- Specify the angle to extract the target cylinder surface.
- The default value is 20.0.

<!-- @since:5.1.0 @optional -->
### crTopNode

- Specify the node to determine the top end of the bore cylinder surface.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crBottomNode

- Specify the node to determine the bottom end of the bore cylinder surface. To define the bore height also.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### dlCenterPoint

- Specify the center coordinate of the bore coordinate system.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.1.0 @optional -->
### dBoreRadius

- Specify the radius of the bore cylinder.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dBoreHeight

- Specify the height of the bore cylinder.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iAxisDirection

- Specify the bore cylinder axial direction in global coordinate system X, Y, Z or arbitrary direction (user defined).
- The default value is 3.

<!-- @since:5.1.0 @optional -->
### dlAxisDefined

- Specify the defined bore cylinder axial direction.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.1.0 @optional -->
### iDepthDirection

- Specify the depth direction.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iNumOfLayerPoint

- Specify the number of calculation points in one layer.
- The default value is 36.

<!-- @since:5.1.0 @optional -->
### dlLayers

- Specify the number of layers and depth value at each layer.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iCalculationMethod

- Specify the calculation method.
  - 0: Best Fit Circle
  - 1: Best Fit Cylinder
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dlAxisX

- Specify X axial direction of the the bore cylinder.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing FFT condition
  - If this parameter is used, the specified FFT condition will be modified.
  - If it is left None, a new FFT condition will be created.
- The default value is _None_.

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
