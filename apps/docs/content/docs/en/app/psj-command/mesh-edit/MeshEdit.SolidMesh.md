---
title: "MeshEdit.SolidMesh()"
description: "Command for converting surface mesh of specified parts to solid mesh."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MeshEdit > SolidMesh"
macro_link: "[ElementConv_Solid](../../macro/mesh-edit/ElementConv_Solid)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Element Conversion","Command for converting surface mesh of specified parts to solid mesh."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Command for converting surface mesh of specified parts to solid mesh.

## Syntax

```psj
MeshEdit.SolidMesh(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The target parts.

### `iType` @type(Integer) @default(1)

- The solid element conversion type.
  - 0: To Linear (Tet4/Penta5/Hex8/Pyramid5)
  - 1: To Quadratic (Tet10/Penta15/Hex20/Pyramid13)
  - 2: Hexa to Penta5
  - 3: Hexa/Penta to Tet4

## Return Code

Returns a string "1" if successful, or "0" if failed.

## Sample Code

```psj
# Prepare model and view
HexModeling.BallHexa(crPart=None, dRadius=0.005, dMeshSize=0.001, strPartName="HexBall_1")
JPT.ViewFitToModel()
JPT.Exec('ViewShowMesh(1)')

# Convert to Tet4
MeshEdit.SolidMesh(crlParts=[Part(1)], iType=3)
```
