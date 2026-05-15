---
title: "PostFFTConditionOut()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Perform a FFT analysis.

## Syntax

```psj
PostFFTConditionOut(str strName, cursor[] crlTargets, cursor[] crl2DElems, double dAngle, 
    cursor crTopNode, cursor crBotNode, double[] dlCenterPoint, double dBoreRadius, 
    double dBoreHeight, int iAxisDirection, double[] dlAxisDefined, int iDepthDirection, 
    int iNumOfLayerPoint, double[] dlLayers, int iCalculationMethod, double[] dlAxisX, 
    cursor crEdit)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. str

- A String specifying the name of bore cylinder.

<!-- @since:5.1.0 -->
### 2. cursor\[]

- A List of Cursor specifying the target parts to perform FFT analysis.

<!-- @since:5.1.0 -->
### 3. cursor\[]

- A List of Cursor specifying the selected 2D elements.

<!-- @since:5.1.0 -->
### 4. double

- A Double specifying the angle to extract the target cylinder surface.

<!-- @since:5.1.0 -->
### 5. cursor

- A Cursor specifying the node to determine the top end of the bore cylinder surface.

<!-- @since:5.1.0 -->
### 6. cursor

- A Cursor specifying the node to determine the bottom end of the bore cylinder surface. To define the bore height also.

<!-- @since:5.1.0 -->
### 7. double\[]

- A List of Double specifying the center coordinate of the bore coordinate system.

<!-- @since:5.1.0 -->
### 8. double

- A Double specifying the radius of the bore cylinder.

<!-- @since:5.1.0 -->
### 9. double

- A Double specifying the height of the bore cylinder.

<!-- @since:5.1.0 -->
### 10. int

- An Integer specifying the bore cylinder axial direction in global coordinate system X, Y, Z or arbitrary direction.

<!-- @since:5.1.0 -->
### 11. double\[]

- A Double List specifying the defined bore cylinder axial direction.

<!-- @since:5.1.0 -->
### 12. int

- An Integer specifying the depth direction.

<!-- @since:5.1.0 -->
### 13. int

- An Integer specifying the number of calculation points in one layer.

<!-- @since:5.1.0 -->
### 14. double\[]

- A List of Double specifying the number of layers and depth value at each layer.

<!-- @since:5.1.0 -->
### 15. int

- An Integer specifying the calculation method.

<!-- @since:5.1.0 -->
### 16. double\[]

- A List of Double specifying X axial direction of the the bore cylinder.

<!-- @since:5.1.0 -->
### 17. cursor

- A Cursor specifying an existing FFT condition

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
PostFFTConditionOut("BORE _1", [0:0], [0:0], 20.0, 0:0, 0:0, [0.0, 0.0, 0.0], 0.0, 0.0, 3, [0.0, 0.0, 0.0], 
    0, 36, [], 0, [0.0, 0.0, 0.0], 0:0)
```
