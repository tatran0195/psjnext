---
title: EXTEND_FACE_MESH
id: EXTEND_FACE_MESH
---

## Description

A data type used to control the mesh settings of extended face.

## Attributes

### `iLengthToFace`

- An _Integer_ specifying the destination method.
    - 0: Length
    - 1: To Face
- The default value is 0.

### `dLengthToFace`

- A _Double_ specifying the length value when _iLengthToFace_=0.
- The default value is 0.01.

### `bUseDivision`

- A _Boolean_ specifying whether to use the mesh division or mesh size method.
    - _True_: Num of Divisions
    - _False_: Mesh Size
- The default value is True.

### `iNumOfDivisions`

- An _Integer_ specifying the number of divisions.
- The default value is 3.

### `dMeshSize`

- A _Double_ specifying the mesh size.
- The default value is 0.001.

### `dBiasFactor`

- A _Double_ specifying the bias factor.
- The default value is 1.

### `iElemType`

- An _Integer_ specifying the element type.
    - 0: Tri3
    - 1: Quad4
- The default value is 0.

### `dLength`

- A _Double_ specifying the length value when [_iMetric_](./EXTEND_FACE_DIRECTION#imetric)=4,
  [_iMethod_](./EXTEND_FACE_DIRECTION#imethod)=4.
- The default value is 0.01.

### `dMeshSizeAxis`

- A _Double_ specifying the mesh size (Axis) value when [_iMetric_](./EXTEND_FACE_DIRECTION#imetric)=4.
  [_iMethod_](./EXTEND_FACE_DIRECTION#imethod)=4.
- The default value is 0.01.

### `dArcRadius`

- A _Double_ specifying the arc radius value when [_iMetric_](./EXTEND_FACE_DIRECTION#imetric)=4,
  [_iMethod_](./EXTEND_FACE_DIRECTION#imethod)=0.
- The default value is 0.01.

### `dAngleOffset`

- A _Double_ specifying the angle offset value when [_iMetric_](./EXTEND_FACE_DIRECTION#imetric)=4,
  [_iMethod_](./EXTEND_FACE_DIRECTION#imethod)=2.
- The default value is 45.

### `dArcLength`

- A _Double_ specifying the arc length value when
  [_iMetric_](./EXTEND_FACE_DIRECTION#imetric)=4,[_iMethod_](./EXTEND_FACE_DIRECTION#imethod)=3.
- The default value is 7.85E-3.

### `dArcNodesNum`

- A _Double_ specifying the arc node number when [_iMetric_](./EXTEND_FACE_DIRECTION#imetric)=4.
- The default value is 5.0.
