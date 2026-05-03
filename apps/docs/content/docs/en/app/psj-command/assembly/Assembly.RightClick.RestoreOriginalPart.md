---
title: "Assembly.RightClick.RestoreOriginalPart()"
description: "Replace the current part by using its reference. In case the number of reference = 0, it will keep the current part without changing anything"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assembly > Right Click > Restore Original Part"
---

## Description

Replace the current part by using its reference. In case the number of reference = 0, it will keep the current part without changing anything.

## Syntax

```psj
Assembly.RightClick.RestoreOriginalPart(...)
```

## Inputs

### `crlBodies` @type(List\[Cursor]) @required

- The list of parts which will be restored.

### `bKeepShareFace` @type(Boolean) @default(False)

- Whether or not keep share face after restore.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {15}
Geometry.Part.Cube()
Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                         surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634, 
                                                  iPerformanceMode=1, 
                                                  dAutoMergeTinyFacesAngle=0.5235987756, 
                                                  bGeomApprox=True, 
                                                  iNextEntityOffsetId=0))
Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                       surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634, 
                                                iPerformanceMode=1, 
                                                dAutoMergeTinyFacesAngle=0.5235987756, 
                                                bGeomApprox=True, 
                                                iNextEntityOffsetId=0))

restore_status = Assembly.RightClick.RestoreOriginalPart(crlBodies=[Part(1)])

JPT.Debugger(restore_status)
```
