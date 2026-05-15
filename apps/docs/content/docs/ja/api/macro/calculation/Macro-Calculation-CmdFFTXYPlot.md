---
title: "CmdFFTXYPlot()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Display the circularity XY plot graph and export it to a specified file.

## Syntax

```psj
CmdFFTXYPlot(int iKey, bool bDefineOA, str strOADefined, str strModesDefined, bool b3DPlot, str strSavePath, bool bSaveFFTInfo, bool bExportTop, bool bExportAllPlotToFile, bool b2DPlot):
```

## Inputs

<!-- @since:5.1.0 -->
### 1. int

- An Integer specifying the ID of the specified FFT condition.

<!-- @since:5.1.0 -->
### 2. bool

- A Boolean specifying whether to display the OA result.

<!-- @since:5.1.0 -->
### 3. str

- A String specifying the mode to display the graph of OA result.

<!-- @since:5.1.0 -->
### 4. str

- A String specifying the mode to display the circularity XY plot graph.

<!-- @since:5.1.0 -->
### 5. bool

- A Boolean specifying whether to display the circularity plot graph in 3D space.

<!-- @since:5.1.0 -->
### 6. str

- A string specifying the save path.

<!-- @since:5.1.0 -->
### 7. bool

- A Boolean specifying whether to save the FFT analysis result to file.

<!-- @since:5.1.0 -->
### 8. bool

- A Boolean specifying whether to shift the values of all layers when outputting amplitude data (except for the 0th order mode).

<!-- @since:5.1.0 -->
### 9. bool

- A Boolean specifying whether to save all resulting roundness XY plots and deformation plots to a CSV file.

<!-- @since:5.1.0 -->
### 10. bool

- A Boolean specifying whether to display the circularity plot graph in 3D space.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CmdFFTXYPlot(1, 1, "2-4", "2, 3, 4", 1,  "path/to/the/file", 1, 1, 1, 1)
```
