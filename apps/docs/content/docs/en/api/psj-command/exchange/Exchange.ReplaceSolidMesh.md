---
title: "Exchange.ReplaceSolidMesh()"
description: "Replace an adjacent solid part."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Exchange > ReplaceSolidMesh"
macro _link: ""
---

## Description

Replace an adjacent solid part.

## Syntax

```psj
Exchange.ReplaceSolidMesh(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlSourceFace`

- The source face (base model side).

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargetFace`

- The target face (echange part side).

<!-- @since:5.1.0 @type:Double @required -->
### `dTolerance`

- The tolerance between source face and target face.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {19-22}
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0],
    ilAxialNodes=[4, 4, 4],
    strName="Cube _3",
    iPartColor=12867524)

Meshing.SolidMeshing(crlParts=[Part(1,2)],
    bTet10=True,
    dGradingFactor=1.05,
    dStretchLimit=0.1,
    iSpeedVsQual=1,
    iRegion=1,
    bSafeMode=False,
    iParallel=16,
    bInternalMeshOnly=False,
    iPartColor=65280)

ret=Exchange.ReplaceSolidMesh(
    crlSourceFace=[Face(24)],
    crlTargetFace=[Face(49)],
    dTolerance=0.0005)
print(ret)
```
