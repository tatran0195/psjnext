---
title: "Meshing.LocalRemesh.Solid()"
description: "Mesh the selected solid elements locally without affecting the other positions"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > LocalRemesh > Solid"
---

## Description

Mesh the selected solid elements locally without affecting the other positions.

## Syntax

```psj
Meshing.LocalRemesh.Solid(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts list to perform remesh.

### `dlCenter` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The center of the sphere. This sphere is the region to remesh.

### `dRadius` @type(Double) @default(5.0)

- The radius of the remesh sphere in millimeter.

### `dGradFactor` @type(Double) @default(1.0)

- The grading factor of the result mesh.

### `dStretchLimit` @type(Double) @default(0.1)

- The stretch limit of the elements in the result mesh.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {20,21,22,23,24}
cube = Geometry.Part.Cube(iPartColor=12603072)
MeshEdit.MoveNode.CADFollows(crlNodes=[Node(453)], 
                             dMovedPosX=5.527019999999999, 
                             dMovedPosY=5.43058, 
                             dMovedPosZ=10.0)

Meshing.SolidMeshing(crlParts=[cube], 
                     bTet10=True, 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1, 
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=4, 
                     bSurfaceNodes=False, 
                     bEdgeNodes=False, 
                     bPreservation=False, 
                     iPartColor=65280)

remesh_status = Meshing.LocalRemesh.Solid(crlParts=[cube], 
                                          dlCenter=[0.005555555555555556, 
                                                    0.005555555555555556, 
                                                    0.01], 
                                          dRadius=2.0)

JPT.Debugger(remesh_status)
```
