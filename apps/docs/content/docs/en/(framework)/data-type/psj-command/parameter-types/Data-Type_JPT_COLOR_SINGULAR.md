---
title: COLOR_SINGULAR
id: COLOR_SINGULAR
---

## Description

A data type uses to control the color for each load point, constraint point, rigid element connection point, and
material boundary point.

## Attributes

### `bLoad`

- A _Bool_ specifying whether to change the note color for load points.
- The default value is _False_.

### `bConstraint`

- A _Bool_ specifying whether to change the note color for constraint points.
- The default value is _False_.

### `bRigidElement`

- A _Bool_ specifying whether to change the note color for rigid body element connection points.
- The default value is _False_.

### `bMatBoundary`

- A _Bool_ specifying whether to change the note color for material boundary points.
- The default value is _False_.

### `iPeakColor`

- An _Integer_ specifying the note color for peaks.
- The default value is 16777215.

### `iLoadColor`

- An _Integer_ specifying the note color for load points.
- The default value is 16742655.

### `iConstraintColor`

- An _Integer_ specifying the note color for constraint points.
- The default value is 65535.

### `iRigidElementColor`

- An _Integer_ specifying the note color for rigid body element connection points.
- The default value is 255.

### `iMatBoundaryColor`

- An _Integer_ specifying the note color for material boundary points.
- The default value is 16776960.

### `iDuplicationColor`

- An _Integer_ specifying note color for nodes where the above conditions overlap.
- The default value is 16711680.
