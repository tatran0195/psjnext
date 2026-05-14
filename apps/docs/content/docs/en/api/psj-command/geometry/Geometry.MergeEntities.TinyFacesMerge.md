---
title: "Geometry.MergeEntities.TinyFacesMerge()"
description: "Merge tiny faces either by extending the user selection or using only the selected faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Merge Entities > Tiny Faces Merge"
macro _link: "[GeometryMergeEntitiesTinyFacesMerge _K](../../macro/geometry/GeometryMergeEntitiesTinyFacesMerge _K)"
---

## Description

Merge tiny faces either by extending the user selection or using only the selected faces.

## Syntax

```psj
Geometry.MergeEntities.TinyFacesMerge(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:AUTO -->
### `strMethod`

- The method use to merge. Possible values are _AUTO_, _SELECT_, _MERGE_, _RESTORE_.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The parts or faces to be merged.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMinFaceWidth`

- The minimum face width in meter. This argument is used when _strMethod_ has the value _AUTO_ or _SELECT_.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dMaxFaceWidth`

- The maximum face width in meter. This argument is used when _strMethod_ has the value _AUTO_ or _SELECT_.

<!-- @since:5.0.1 @type:Double @optional @default:30 -->
### `dFaceAngle`

- The angle between faces in degree. This argument is used when _strMethod_ has the value _AUTO_ or _MERGE_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bReferLocalSetting`

- Whether to refer to the local setting or not.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCreateRefPart`

- Whether or not create a reference part.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlRefPart`

- The reference parts.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlRefEdge`

- The reference edge.

<!-- @since:5.0.1 @type:Boolean @removed:5.1.0 @optional @deprecated @default:False -->
### `bConnectFace`

- Whether to connect faces after the merge operation is executed.

## Return Code

A _Boolean_ specifying whether the function is executed successfully or not:

- _True_: The function is executed successfully.
- _False_: The function cannot be executed.

## Sample Code

```psj {15,16}
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube _2",
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
merged _entities = Geometry.MergeEntities.TinyFacesMerge(crlTargets=[Part(1, 2)],
                                                        bCreateRefPart=True)
JPT.Debugger(merged _entities)
```
