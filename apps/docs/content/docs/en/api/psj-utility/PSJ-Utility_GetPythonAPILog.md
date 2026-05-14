---
title: "JPT.GetPythonAPILog()"
description: "Get the text existing on the Python API window"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the text existing on the Python API window.

## Syntax

```psj
JPT.GetPythonAPILog()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _String_ containing all the text existing on the Python API window.

## Sample Code

```psj {11}
# Prepare model to write all text on Python API log
Geometry.Part.Cube(strName="Cube _5", iPartColor=7463537)
Geometry.Part.Cube(strName="Cube _6", iPartColor=7434735)
Geometry.Part.Cube(strName="Cube _7", iPartColor=14903267)
Geometry.Part.Cube(strName="Cube _8", iPartColor=15658599)
Geometry.Part.Cube(strName="Cube _9", iPartColor=7961077)
Geometry.Part.Cube(strName="Cube _10", iPartColor=7829501)
JPT.ViewFitToModel()

# Get the printed text in Python API window
log = JPT.GetPythonAPILog()
JPT.Debugger(log)
```
