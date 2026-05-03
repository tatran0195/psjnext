---
title: "Exchange.ReplaceSolidMesh()"
description: "Replace an adjacent solid part."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Exchange > ReplaceSolidMesh"
macro_link: ""
---

## Description

Replace an adjacent solid part.

## Syntax

```psj
Exchange.ReplaceSolidMesh(...)
```

## Inputs

### `crlSourceFace` @type(List\[Cursor]) @required

- Source face (base model side).

### `crlTargetFace` @type(List\[Cursor]) @required

- Target face (echange part side).

### `dTolerance` @type(Double) @required

- Tolerance between source face and target face.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {19-22}
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0],
    ilAxialNodes=[4, 4, 4],
    strName="Cube_3",
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
