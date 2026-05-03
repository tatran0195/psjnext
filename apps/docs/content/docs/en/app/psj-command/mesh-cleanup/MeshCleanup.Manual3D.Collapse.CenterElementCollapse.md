---
title: "MeshCleanup.Manual3D.Collapse.CenterElementCollapse()"
description: "Collapse the selected element towards the center of its element and connect the surrounding elements"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MeshCleanup > Manual3D > Collapse > CenterElementCollapse"
macro_link: ""
---

## Description

Collapse the selected element towards the center of its element and connect the surrounding elements.

## Syntax

```psj
MeshCleanup.Manual3D.Collapse.CenterElementCollapse(...)
```

## Inputs

### `crlElems` @type(List\[Cursor]) @required

- The solid element.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {11}
Geometry.Part.Cube(iPartColor=6409934)
Meshing.SolidMeshing(crlParts=[Part(1)], 
                    dGradingFactor=1.05, 
                    dStretchLimit=0.1, 
                    iSpeedVsQual=1, 
                    iRegion=1, 
                    bSafeMode=False, 
                    iParallel=16, 
                    bInternalMeshOnly=False, 
                    iPartColor=65280)
MeshCleanup.Manual3D.Collapse.CenterCollapse(crlElems=[Elem(8756)])
```
