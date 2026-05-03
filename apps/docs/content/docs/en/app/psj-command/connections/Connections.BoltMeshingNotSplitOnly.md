---
title: "Connections.BoltMeshingNotSplitOnly()"
description: "For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions for ADVC."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > BoltMeshingNotSplitOnly"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Unknown Description","For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions for ADVC."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions for ADVC.

## Syntax

```psj
Connections.BoltMeshingNotSplitOnly(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iPartcutparamImethod` @type(Integer) @default(0)

- The part cut parameter method.

### `dPartcutparamDoffset` @type(Double) @default(0.0)

- The part cut parameter offset.

### `iPartcutparamBshareface` @type(Integer) @default(0)

- The part cut parameter share face.

### `iPartcutparamBseparateface` @type(Integer) @default(0)

- The part cut parameter separate face.

### `iPartcutparamBsplitonly` @type(Integer) @default(0)

- The part cut parameter split only.

### `iPartcutparamBmakesectionface` @type(Integer) @default(0)

- The part cut parameter make section face.

### `crPartcutparamCoord` @type(Cursor) @default(None)

- The part cut parameter coordinate.

### `surfaceMesh` @type(SURFACE\_MESH) @default(SURFACE\_MESH)

- The mesh.

### `iLBCPRETENSIONDATAIdir` @type(Integer) @default(0)

- The load boundary condition pretension data direction.

### `dLBCPRETENSIONDATADvalue` @type(Double) @default(0.0)

- The load boundary condition pretension data value.

### `bLBCPRETENSIONDATABfixlength` @type(Boolean) @default(False)

- The load boundary condition pretension data fixed length.

### `crLBCPRETENSIONDATACrtable` @type(Cursor) @default(None)

- The load boundary condition pretension data table.

### `crLBCPRETENSIONDATACrcoord` @type(Cursor) @default(None)

- The load boundary condition pretension data coordinate.

### `iLBCPRETENSIONDATAIlocalunit` @type(Integer) @default(0)

- The load boundary condition pretension data local unit.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `poslCutter` @type(Position List) @default(\[])

- The cutter.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BoltMeshingNotSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), iLBCPRETENSIONDATAIdir=0, dLBCPRETENSIONDATADvalue=0.0, bLBCPRETENSIONDATABfixlength=False, crLBCPRETENSIONDATACrtable=None, crLBCPRETENSIONDATACrcoord=None, iLBCPRETENSIONDATAIlocalunit=0, crlTargets=[], poslCutter=[])
```
