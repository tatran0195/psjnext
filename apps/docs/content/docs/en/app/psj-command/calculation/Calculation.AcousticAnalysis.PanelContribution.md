---
title: "Calculation.AcousticAnalysis.PanelContribution()"
description: "Create a plot line for each panel property based on Actran's element contribution results"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > AcousticAnalysis > PanelContribution"
macro_link: "[PostToolAcousticPanelContribution](../../macro/calculation/PostToolAcousticPanelContribution)"
---

## Description

Create a plot line for each panel property based on Actran's element contribution results.

## Syntax

```psj
Calculation.AcousticAnalysis.PanelContribution(...)
```

## Inputs

### `ilLoadCases` @type(List\[Integer]) @default(\[])

- The selected loadcases for the element contribution plot line.

### `crlProperties` @type(List\[Cursor]) @default(\[])

- The property panels for the element contribution plot line.

### `iAreaUnit` @type(Integer) @default(0)

- The area unit.

### `bSum` @type(Boolean) @default(True)

- Whether to sum the element contributions.

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
