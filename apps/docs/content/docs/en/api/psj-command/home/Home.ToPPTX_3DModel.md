---
title: "Home.ToPPTX _3DModel()"
description: "Save the model in the current document as a 3D object (.glb file) and embed it into a .pptx file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > ToImage > 3D Model(*.glb)"
---

## Description

Save the model in the current document as a 3D object (.glb file) and embed it into a .pptx file.

## Syntax

```psj
Home.ToPPTX(...)
```

## Inputs

This function does not require any input value.

## Return Code

A _Boolean_ specifying the status of the process:

- _True_: The model is saved as a 3d model file in pptx.
- _False_: The model is saved as a 3d model file in pptx.

## Sample Code

```psj {5}
Geometry.Part.Cube()
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Home.ToPPTX _3DModel()
```
