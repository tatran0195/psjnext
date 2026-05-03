---
title: "Geometry.MergeEntities.Parts()"
description: "Merge several parts into a single part. The first selected part will be retained, others will be merged into the first part. Load conditions and material properties, etc., which have been set on faces and edges, will be updated to the merged part automatically"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Merge Entities > Parts"
macro_link: "[MergePart](../../macro/geometry/MergePart)"
---

## Description

Merge several parts into a single part. The first selected part will be retained, others will be merged into the first part.
Load conditions and material properties, etc., which have been set on faces and edges, will be updated to the merged part automatically.

## Syntax

```psj
Geometry.MergeEntities.Parts(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to be merged.

### `dMergeTolerance` @type(Double) @default(1e-5)

- The maximum distance between nodes of the given parts that will be merged.

### `bRemoveSharedFace` @type(Boolean) @default(True)

- Whether to remove the shared faces between the given parts after merging.

## Return Code

A _Cursor_ specifying the merged part.

## Sample Code

```psj {4,5}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0],
                   strName="Cube_2")
merged_part = Geometry.MergeEntities.Parts(crlParts=[Part(1, 2)],
                                           dMergeTolerance=1e-05)
JPT.Debugger(merged_part)
```
