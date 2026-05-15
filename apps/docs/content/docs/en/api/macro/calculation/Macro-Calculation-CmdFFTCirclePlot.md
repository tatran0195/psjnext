---
title: "CmdFFTCirclePlot()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display the deformation plot graph.

## Syntax

```psj
CmdFFTCirclePlot(int iKey, bool bOACircleOutput, str strOACircleLayers, bool bOADefine, str strOADefine, str strModeOutput, str strModesLayers)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- An Integer specifying the ID of the specified FFT condition.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether to use the OA Circle option.

<!-- @since:5.1.0 -->
### 3. str

- A String specifying the number of layers to display the deformation plot graph of the OA results.

<!-- @since:5.1.0 -->
### 4. bool

- A Boolean specifying whether to use the Define OA Circle option.

<!-- @since:5.1.0 -->
### 5. str

- A String specifying the mode to be used for the OA curve.

<!-- @since:5.1.0 -->
### 6. str

- A String specifying the mode in which deformation plots are displayed graphically.

<!-- @since:5.1.0 -->
### 7. str

- A String specifying the layer to be displayed graphically in each mode.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdFFTCirclePlot(1, 1, "2", 1, "2-4", "2", "2")
```
