---
title: "Calculation.AcousticAnalysis.PanelContribution()"
description: "Create a plot line for each panel property based on Actran's element contribution results"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > AcousticAnalysis > PanelContribution"
macro _link: "[PostToolAcousticPanelContribution](../../macro/calculation/PostToolAcousticPanelContribution)"
---

## Description

Create a plot line for each panel property based on Actran's element contribution results.

## Syntax

```psj
Calculation.AcousticAnalysis.PanelContribution(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### ilLoadCases

- Specify the selected loadcases for the element contribution plot line.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crlProperties

- Specify the property panels for the element contribution plot line.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iAreaUnit

- Specify the area unit.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bSum

- Specify whether to sum the element contributions.
- The default value is _True_.

## Return Code

A _List of Cursor_ specifying the created panel contribution.

## Sample Code

```psj {8-12}
# Please set path to your sample Nastran Vibro-Acoustic file.
filePath="C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath=filePath, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# AcousticAnalysis.PanelContribution
Calculation.AcousticAnalysis.PanelContribution(ilLoadCases=[201], 
                                                crlProperties=[Property2DShell(50000), 
                                                Property3DSolid(20000, 40000)], 
                                                iAreaUnit=0)
Calculation.AcousticAnalysis.PanelContributionCreateGraph(crlLoadCases=[PostActranLoadCase(1, 2, 3, 4)])
```
