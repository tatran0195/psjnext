---
title: "Geometry.MergeEntities.Parts()"
description: "Merge several parts into a single part. The first selected part will be retained, others will be merged into the first part. Load conditions and material properties, etc., which have been set on faces and edges, will be updated to the merged part automatically"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Merge Entities > Parts"
macro _link: "[MergePart](../../macro/geometry/MergePart)"
---

## Description

Merge several parts into a single part. The first selected part will be retained, others will be merged into the first part.
Load conditions and material properties, etc., which have been set on faces and edges, will be updated to the merged part automatically.

## Syntax

```psj
Geometry.MergeEntities.Parts(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the parts to be merged.

<!-- @since:5.0.1 @optional -->
### dMergeTolerance

- Specify the maximum distance between nodes of the given parts that will be merged.
- The default value is 1e-5.

<!-- @since:5.0.1 @optional -->
### bRemoveSharedFace

- Specify whether to remove the shared faces between the given parts after merging.
- The default value is _True_.

## Return Code

A _Cursor_ specifying the merged part.

## Sample Code

```psj {4,5}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0],
                   strName="Cube _2")
merged _part = Geometry.MergeEntities.Parts(crlParts=[Part(1, 2)],
                                           dMergeTolerance=1e-05)
JPT.Debugger(merged _part)
```
