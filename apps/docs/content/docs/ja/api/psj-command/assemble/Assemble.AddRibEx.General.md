---
title: "Assemble.AddRibEx.General()"
description: "Add rib part on a part."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Assemble > AddRibEx > General"
macro _link: "AddRibGeneralEx"
---

## Description

Add rib part on a part.

## Syntax

```psj
Assemble.AddRibEx.General(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### dlPositions

- Specify position of first end of the rib to create.

<!-- @since:5.1.0 @required -->
### crlFaces

- Specify position of second end of the rib to create.

<!-- @since:5.1.0 @optional -->
### dThickness

- Specify the width of the rib.
- The default value is 0.0005.

<!-- @since:5.1.0 @optional -->
### #dHeight

- Specify the height of the rib from the attachment surface.
- The default value is 0.001.

<!-- @since:5.1.0 @optional -->
### #crCoordinate

- Specify the coordinate system to reference when attaching the rib.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bDirectByCoord

- Specify whether or not align the rib direction with the coordinate plane defined by the specified coordinate axes.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iPlane

- Specify the coordinate plane:
  - 0: Aligns the rib with the XY plane direction.
  - 1: Aligns the rib with the YZ plane direction.
  - 2: Aligns the rib with the ZX plane direction.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dOffsetX

- Specify offset value the rib creation position in X direction.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dOffsetY

- Specify offset value the rib creation position in Y direction.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dOffsetZ

- Specify offset value the rib creation position in Z direction.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bTriangle

- Specify whether creates the rib as a triangular rib with a higher starting point.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bPlaneTop

- Specify whether or not makes the rib top flat even when the attachment surface is curved.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bCreateNewPart

- Specify whether or not create a rib part as a new part.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bMerge

- Specify whether or not merge rib part to the part of target face belongs to.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bPreview

- Specify whether or not display preview.
- The default value is _True_.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {2-8}
Geometry.Part.Cube()
Assemble.AddRibEx.General(
    dlPositions=[
        [0.007777777777777778, 0.003333333333333333, 0.01], 
        [0.002222222222222222, 0.007777777777777778, 0.01]], 
    crlFaces=[Face(26)], 
    dThickness=0.001, 
    dHeight=0.001)
```
