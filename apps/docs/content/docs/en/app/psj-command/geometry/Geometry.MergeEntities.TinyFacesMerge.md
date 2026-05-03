---
title: "Geometry.MergeEntities.TinyFacesMerge()"
description: "Merge tiny faces either by extending the user selection or using only the selected faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Merge Entities > Tiny Faces Merge"
macro_link: "[GeometryMergeEntitiesTinyFacesMerge_K](../../macro/geometry/GeometryMergeEntitiesTinyFacesMerge_K)"
---
<!-- REVIEW FLAGS — requires human review
   [param_removed_unexpectedly] Param 'bConnectFace' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Merge tiny faces either by extending the user selection or using only the selected faces.

## Syntax

```psj
Geometry.MergeEntities.TinyFacesMerge(...)
```

## Inputs

### `strMethod` @type(String) @default(AUTO)

- The method use to merge. Possible values ar&#x65;_&#x41;UTO_,_SELECT_,_MERGE_,_RESTORE_.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The parts or faces to be merged.

### `dMinFaceWidth` @type(Double) @default(0.0)

- The minimum face width in meter. This argument is used whe&#x6E;_&#x73;trMetho&#x64;_&#x68;as the valu&#x65;_&#x41;UT&#x4F;_&#x6F;&#x72;_&#x53;ELECT_.

### `dMaxFaceWidth` @type(Double) @default(0.001)

- The maximum face width in meter. This argument is used whe&#x6E;_&#x73;trMetho&#x64;_&#x68;as the valu&#x65;_&#x41;UT&#x4F;_&#x6F;&#x72;_&#x53;ELECT_.

### `dFaceAngle` @type(Double) @default(30)

- The angle between faces in degree. This argument is used whe&#x6E;_&#x73;trMetho&#x64;_&#x68;as the valu&#x65;_&#x41;UT&#x4F;_&#x6F;&#x72;_&#x4D;ERGE_.

### `bReferLocalSetting` @type(Boolean) @default(False)

- Whether to refer to the local setting or not.

### `bCreateRefPart` @type(Boolean) @default(False) @since(5.1.0)

- Whether or not create a reference part.

### `crlRefPart` @type(List\[Cursor]) @default(\[]) @since(5.1.0)

- The reference parts.

### `crlRefEdge` @type(List\[Cursor]) @default(\[]) @since(5.1.0)

- The reference edge.

### `bConnectFace` @type(Boolean) @default(False) @deprecated @until(5.1.0)

- Whether to connect faces after the merge operation is executed.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- _True_: The function is executed successfully.
- _False_: The function cannot be executed.

## Sample Code

```psj {15,16}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2",
                   iPartColor=6409934)
Geometry.Edge.Angle([CursorPair(Node(945), Node(953))])
Geometry.Edge.Angle([CursorPair(Node(464), Node(472))])
Geometry.Edge.Angle([CursorPair(Node(79), Node(432))])
Geometry.Edge.Angle([CursorPair(Node(96), Node(487))])
Geometry.Edge.Angle([CursorPair(Node(470), Node(479))])
Geometry.Edge.Angle([CursorPair(Node(471), Node(479))])
Geometry.Edge.Angle([CursorPair(Node(946), Node(954))])
Geometry.Edge.Angle([CursorPair(Node(953), Node(954))])
Geometry.Edge.Angle([CursorPair(Node(961), Node(962))])
Geometry.Edge.Angle([CursorPair(Node(953), Node(962))])
merged_entities = Geometry.MergeEntities.TinyFacesMerge(crlTargets=[Part(1, 2)],
                                                        bCreateRefPart=True)
JPT.Debugger(merged_entities)
```
