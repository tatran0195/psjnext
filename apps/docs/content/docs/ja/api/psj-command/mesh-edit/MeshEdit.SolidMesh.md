---
title: "MeshEdit.SolidMesh()"
description: "Command for converting surface mesh of specified parts to solid mesh."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > SolidMesh"
macro _link: "[ElementConv _Solid](../../macro/mesh-edit/ElementConv _Solid)"
---

## Description

Command for converting surface mesh of specified parts to solid mesh.

## Syntax

```psj
MeshEdit.SolidMesh(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the target parts.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iType

- Specify the solid element conversion type.
  - 0: To Linear (Tet4/Penta5/Hex8/Pyramid5)
  - 1: To Quadratic (Tet10/Penta15/Hex20/Pyramid13)
  - 2: Hexa to Penta5
  - 3: Hexa/Penta to Tet4
- The default value is 1.

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
HexModeling.BallHexa(crPart=None, dRadius=0.005, dMeshSize=0.001, strPartName="HexBall _1")
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Convert to Tet4
MeshEdit.SolidMesh(crlParts=[Part(1)], iType=3)
```
