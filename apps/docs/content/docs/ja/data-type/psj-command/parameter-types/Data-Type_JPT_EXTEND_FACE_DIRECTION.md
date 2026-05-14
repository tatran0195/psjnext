---
title: EXTEND_FACE_DIRECTION
id: EXTEND_FACE_DIRECTION
---

## Description

A data type used to control the direction settings for extended face.

## Attributes

### `iMetric`

- An _Integer_ specifying the method to create the face.
  - 0: Coordinate
  - 1: 2 Nodes
  - 2: Element Edge
  - 3: Offset
  - 4: Cylinder
- The default value is 0.

### `iCoordinateSystem`

- An _Integer_ specifying the referent coordinate system when _iMetric_=0.
- The default value is 0 (Global).

### `iDirection`

- An _Integer_ specifying direction to extend the face when iMetric=0.
  - 0: By Components
  - 1: By Angles
- The default value is 0.

### `dComponentX`

- A _Double_ specifying X direction when iDirection=0.
- The default value is 1.

### `dComponentY`

- A _Double_ specifying Y direction when iDirection=0.
- The default value is 1.

### `dComponentZ`

- A _Double_ specifying Z direction when iDirection=0.
- The default value is 1.

### `dAngleTheta`

- A _Double_ specifying theta value when _iDirection_=1.
- The default value is 45.

### `dAnglePhi`

- A _Double_ specifying phi value when _iDirection_=1.
- The default value is 45.

### `bBothDirections`

- A _Boolean_ specifying whether to extend the face in both direction.
- The default value is _False_.

### `bReverseDirection`

- A _Boolean_ specifying whether to create a face in the opposite direction.
- The default value is _False_.

### `iMethod`

- An _Integer_ specifying method to create the face when _iMetric_=4.
  - 0: To Axis
  - 1: To Face
  - 2: Arc Angle
  - 3: Arc Length
  - 4: Sweep
- The default value is 0.

### `iAxisPlane`

- An _Integer_ specifying axis plane when _iMethod_=0.
  - 0: XY
  - 1: YZ
  - 2: ZX
- The default value is 0.

### `dZXY`

    - A _Double_ specifying parameter of Z / X / Y
    - The default value is 0.001.
