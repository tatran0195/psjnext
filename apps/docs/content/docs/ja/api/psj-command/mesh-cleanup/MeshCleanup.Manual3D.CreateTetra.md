---
title: "MeshCleanup.Manual3D.CreateTetra()"
description: "create element Tet"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshCleanup > Manual3D > CreateTetra"
---

## Description

Create element Tet

## Syntax

```psj
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNodes=[], crlElems=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iParentEntityId

- Specify the parent entity ID.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify the node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlElems

- Specify the element.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNodes=[], crlElems=[])
```
