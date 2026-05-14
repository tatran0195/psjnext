---
title: "JPT.GetOutputLog()"
description: "Get the text existing on the Output window"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get the text existing on the Output window.

## Syntax

```psj
JPT.GetOutputLog()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _String_ containing all the text existing on the Output window.

## Sample Code

```psj {11}
# Prepare model to write all text on Output log
Geometry.Part.Cube(strName="Cube _5", iPartColor=7463537)
Geometry.Part.Cube(strName="Cube _6", iPartColor=7434735)
Geometry.Part.Cube(strName="Cube _7", iPartColor=14903267)
Geometry.Part.Cube(strName="Cube _8", iPartColor=15658599)
Geometry.Part.Cube(strName="Cube _9", iPartColor=7961077)
Geometry.Part.Cube(strName="Cube _10", iPartColor=7829501)
JPT.ViewFitToModel()

# Get the printed text in Output window
log = JPT.GetOutputLog()
JPT.Debugger(log)
```
