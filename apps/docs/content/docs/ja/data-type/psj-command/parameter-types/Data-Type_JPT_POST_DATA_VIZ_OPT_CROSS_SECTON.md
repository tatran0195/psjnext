---
title: POST_DATA_VIZ_OPT_CROSS_SECTION
id: POST_DATA_VIZ_OPT_CROSS_SECTION
---

## Description

A data type used to set the settings for the cross-section display.

## Attributes

### `bCapping`

- A _Boolean_ specifying whether to show/hide the cross-section face.
- The default value is _True_.

### `bCuttingEdge`

- A _Boolean_ specifying whether to show/hide the profile lines of the cross-section.
- The default value is _False_.

### `bSectionElem`

- A _Boolean_ specifying whether to show/hide the solid elements on the cross-section.
- The default value is _False_.

### `bMeshLine`

- A _Boolean_ specifying whether to show/hide the mesh lines on the cross-section
- The default value is _False_.

### `bShow3DMouse`

- A _Boolean_ specifying whether to show the 3D mouse.
- The default value is _True_.

### `bFlip`

- A _Boolean_ specifying whether to switches the display range of the model to the opposite side of the cross-section.
- The default value is _False_.

### `bBoxView`

- A _Boolean_ specifying whether to cut and display the model in a box that is on the top of the 3D mouse.
- The default value is _False_.

### `bTransparency`

- A _Boolean_ specifying whether to display the hidden part with the transparency.
- The default value is _False_.

### `dTransparency`

- A _Double_ specifying the percentage of the transparency of the hidden part.
- The default value is 0.0.

### `iTransparencyColor`

- An _Integer_ specifying the color of the hidden part when displaying it in the transparency.
- The default value is 0.

### `dlTranslationMatrix`

- A _Double List_ specifying the transformation matrix of the cross-section.
- The default value is [-1,0,0,0,0,-1,0,0,0,0,-1,0,0,0,0,1].

### `dlPosition`

- A _Double List_ specifying the coordinate (X, Y, Z) of the 3D Mouse.
- The default value is [1e-10,1e-10,1e-10].

### `dlPreviousPosition`

- A _Double List_ specifying the previous coordinate (X, Y, Z) of the 3D Mouse.
- The default value is [0,0,0].

### `dlRotationCenter`

- A _Double List_ specifying the coordinate of the center of rotation (X, Y, Z).
- The default value is [1e-10,1e-10,1e-10].

### `dlDirectAngle`

- A _List of Double_ specifying the direction angle.
- The default value is [0,0,0].

### `dSize`

- A _Double_ specifying the size value
- The default value is 0.25.

### `dPlaneSize`

- A _Double_ specifying the plane size value.
- The default value is 0.2.

### `dBoxSize`

- A _Double_ specifying the box size.
- The default value is 0.025.
