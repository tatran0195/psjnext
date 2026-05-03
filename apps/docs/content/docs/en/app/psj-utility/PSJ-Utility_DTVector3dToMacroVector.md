---
title: "JPT.DTVector3dToMacroVector()"
description: "Convert DTVector3d object to DTVector3d (Macro string type)"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Convert _[TVector3d](../data-type/psj-utility/pre-utility/built-in-types/TVector3d)_ object to DTVector3d (Macro string type).

## Syntax

```psj
JPT.DTVector3dToMacroVector(DTVector3d)
```

## Inputs

### `DTVector3d` @type(TVector3d) @required

- Object to be converted.

## Return Code

A _String_ containing all the converted items.

## Sample Code

```psj {13}
# Prepare model
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube_2")
Geometry.Part.Cube(strName="Cube_3")
JPT.ViewFitToModel()

# Get all the existing Nodes and convert one of them to DTVector3D (Macro string type)
## Get all Nodes from model
listNodes = JPT.GetAllNodes() # List of DNode objects
## Get position (DTVector3D) of 1 node in list
posNode1 = listNodes[0].pos # DTVector3D object
# Return DTVector3D object to a string object, for example, return value = [0,0.00777778,0.00444444]
JPT.Debugger(JPT.DTVector3dToMacroVector(posNode1))
```
