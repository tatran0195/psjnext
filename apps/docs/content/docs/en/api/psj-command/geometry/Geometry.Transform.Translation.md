---
title: "Geometry.Transform.Translation()"
description: "Move the parts along a given vector. The direction and magnitude of the vector are arbitrary or along the specific axis in the Cartesian coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Transform > Translation"
macro _link: "[TranslateBody](../../macro/geometry/TranslateBody)"
---

## Description

Move the parts along a given vector. The direction and magnitude of the vector are arbitrary or along the specific axis in the Cartesian coordinate system.

## Syntax

```psj
Geometry.Transform.Translation(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts to be moved.

<!-- @since:5.0.1 @type:List[Position] @optional @default:[] -->
### `dlTranslationVector`

- The translation vector in _crLocalCoordinate_ coordinate system defining the direction and magnitude of the particular translation.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCoordinate`

- The local coordinate system using for the definition of the _dlTranslationVector_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCreateNewPart`

- Whether to keep the original parts and create new parts in the moved positions or not.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyLBC`

- Whether to copy boundary conditions from the existing part to the created parts or not.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyProperty`

- Whether to copy properties from the existing part to the created parts or not.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyReference`

- Whether to copy references from the existing part to the created parts or not.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCopyCount`

- The number of copies (Creating parts).

## Return Code

A _List of Cursor_ specifying the new parts if success, or _empty_ if fail.

## Sample Code

```psj {2,3}
Geometry.Part.Cube(iPartColor=8124407)
translated _part = Geometry.Transform.Translation(crlParts=[Part(1)],
                                                 dlTranslationVector=[[-0.00666, 0.00222, 0]])
JPT.Debugger(translated _part)
```
