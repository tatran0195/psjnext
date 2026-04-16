---
title: EXTEND_FACE_OPTION
id: EXTEND_FACE_OPTION
---

## Description

A data type used to control the geometric settings for the extended face.

## Attributes

### `bMergeFaces`

- A _Boolean_ specifying whether to merge the extended face to the target face.
- The default value is 0 (OFF).

### `bMergeEdges`

- A _Boolean_ specifying whether to merge edges by a specified angle.
- The default value is 0 (OFF).

### `dMergeEdges`

- A _Double_ specifying angle value at which the edges can be merged.
- The default value is 0 (OFF).

### `bConnect`

- A _Boolean_ specifying whether to connect the extended face and target face by share nodes.
- The default value is 0 (OFF).

### `bCreateNewPart`

- A _Boolean_ specifying whether to create the extended face as a new part.
- The default value is 0 (OFF).

### `strPartName`

- A _String_ specifying the name of newly created part.
- The default value is "Extend 1".
