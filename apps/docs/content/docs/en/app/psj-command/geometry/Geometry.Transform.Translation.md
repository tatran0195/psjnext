---
title: "Geometry.Transform.Translation()"
description: "Move the parts along a given vector. The direction and magnitude of the vector are arbitrary or along the specific axis in the Cartesian coordinate system"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Transform > Translation"
macro_link: "[TranslateBody](../../macro/geometry/TranslateBody)"
---

## Description

Move the parts along a given vector. The direction and magnitude of the vector are arbitrary or along the specific axis in the Cartesian coordinate system.

## Syntax

```psj
Geometry.Transform.Translation(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to be moved.

### `dlTranslationVector` @type(List\[Position]) @default(\[])

- The translation vector i&#x6E;_&#x63;rLocalCoordinat&#x65;_&#x63;oordinate system defining the direction and magnitude of the particular translation.

### `crLocalCoordinate` @type(Cursor) @default(None)

- The local coordinate system using for the definition of th&#x65;_&#x64;lTranslationVector_.

### `bCreateNewPart` @type(Boolean) @default(False)

- Whether to keep the original parts and create new parts in the moved positions or not.

### `bCopyLBC` @type(Boolean) @default(False)

- Whether to copy boundary conditions from the existing part to the created parts or not.

### `bCopyProperty` @type(Boolean) @default(False)

- Whether to copy properties from the existing part to the created parts or not.

### `bCopyReference` @type(Boolean) @default(False)

- Whether to copy references from the existing part to the created parts or not.

### `iCopyCount` @type(Integer) @default(1)

- The number of copies (Creating parts).

## Return Code

A _List of Cursor_ specifying the new parts if success, or _empty_ if fail.

## Sample Code

```psj {2,3}
Geometry.Part.Cube(iPartColor=8124407)
translated_part = Geometry.Transform.Translation(crlParts=[Part(1)],
                                                 dlTranslationVector=[[-0.00666, 0.00222, 0]])
JPT.Debugger(translated_part)
```
