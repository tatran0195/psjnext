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

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the parts to be moved.

<!-- @since:5.0.1 @optional -->
### dlTranslationVector

- Specify the translation vector in _crLocalCoordinate_ coordinate system defining the direction and magnitude of the particular translation.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crLocalCoordinate

- Specify the local coordinate system using for the definition of the _dlTranslationVector_.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### bCreateNewPart

- Specify whether to keep the original parts and create new parts in the moved positions or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyLBC

- Specify whether to copy boundary conditions from the existing part to the created parts or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyProperty

- Specify whether to copy properties from the existing part to the created parts or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyReference

- Specify whether to copy references from the existing part to the created parts or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iCopyCount

- Specify the number of copies (Creating parts).
- The default value is 1.

## Return Code

A _List of Cursor_ specifying the new parts if success, or _empty_ if fail.

## Sample Code

```psj {2,3}
Geometry.Part.Cube(iPartColor=8124407)
translated _part = Geometry.Transform.Translation(crlParts=[Part(1)],
                                                 dlTranslationVector=[[-0.00666, 0.00222, 0]])
JPT.Debugger(translated _part)
```
