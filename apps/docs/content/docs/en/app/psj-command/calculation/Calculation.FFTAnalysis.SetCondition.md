---
title: "Calculation.FFTAnalysis.SetCondition()"
description: "Perform a FFT analysis"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > FFTAnalysis > SetCondition"
macro_link: "[PostFFTConditionOut](../../macro/calculation/PostFFTConditionOut)"
---

## Description

Perform a FFT analysis.

## Syntax

```psj
Calculation.FFTAnalysis.SetCondition(...)
```

## Inputs

### `strName` @type(String) @default("BORE\_1")

- The name of bore cylinder.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target parts to perform FFT analysis.

### `crl2DElems` @type(List\[Cursor]) @default(\[])

- The selected 2D elements.

### `dAngle` @type(Double) @default(20.0)

- The angle to extract the target cylinder surface.

### `crTopNode` @type(Cursor) @default(None)

- The node to determine the top end of the bore cylinder surface.

### `crBottomNode` @type(Cursor) @default(None)

- The node to determine the bottom end of the bore cylinder surface. To define the bore height also.

### `dlCenterPoint` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The center coordinate of the bore coordinate system.

### `dBoreRadius` @type(Double) @default(0.0)

- The radius of the bore cylinder.

### `dBoreHeight` @type(Double) @default(0.0)

- The height of the bore cylinder.

### `iAxisDirection` @type(Integer) @default(3)

- The bore cylinder axial direction in global coordinate system X, Y, Z or arbitrary direction (user defined).

### `dlAxisDefined` @type(Double List) @default(\[0.0,0.0,0.0])

- The defined bore cylinder axial direction.

### `iDepthDirection` @type(Integer) @default(0)

- The depth direction.

### `iNumOfLayerPoint` @type(Integer) @default(36)

- The number of calculation points in one layer.

### `dlLayers` @type(List\[Double]) @default(\[])

- The number of layers and depth value at each layer.

### `iCalculationMethod` @type(Integer) @default(0)

- The calculation method.
  - 0: Best Fit Circle
  - 1: Best Fit Cylinder

### `dlAxisX` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- X axial direction of the the bore cylinder.

### `crEdit` @type(Cursor) @default(None)

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
