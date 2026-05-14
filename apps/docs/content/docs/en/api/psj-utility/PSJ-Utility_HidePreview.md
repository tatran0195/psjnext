---
title: "JPT.HidePreview()"
description: "Hide preview render on the main screen"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Hide preview render on the main screen. Preview is still existing, but it will be hidden.

## Syntax

```psj
JPT.HidePreview(...)
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {12}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube _2", iPartColor=13259210)
JPT.ViewFitToModel()

#Preview:
color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
parts = JPT.GetAllParts()
JPT.PreviewScaling(parts,[2,1.1,1.1],[0,0,0],color,0.2)

#Hide Preview:
JPT.HidePreview()
```
