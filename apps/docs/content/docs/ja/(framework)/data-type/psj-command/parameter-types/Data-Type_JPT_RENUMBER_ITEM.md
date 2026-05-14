---
title: RENUMBER_ITEM
---

## Description

A data type uses to control parameters of Renumber Item

## Attributes

### `crTarget`

- A _Cursor_ specifying the target to perform renumbering on its target type. The target is Part or Group
- The default value is None.

### `iBeginID`

- An _Integer_ specifying the start ID.
- The default value is 0.

### `iTargetType`

- An _Integer_ specifying the target type to be renumbered. The target type can be Node, 3D Element, 2D Element, 1D
  Element, Edge, or Face.
- The default value is 0.
-

### `iCount`

- An _Integer_ specifying the number of target contained in part/group.
- The default value is 0.

### `iIncrement`

- An _Integer_ specifying the increment.
- The default value is 0.

### `iOrder`

- An _Integer_ specifying order.
- The default value is 0.

### `iMethod`

- An _Integer_ specifying method.
- The default value is 0.

### `crRefCoord`

- A _Cursor_ specifying referent coordinate.
- The default value is None.

### `ilCoordOrder`

- A _List of Integer_ specifying coordinate order.
- The default value is [0, 0, 0].

### `ilOffset`

- A _List of Integer_ specifying offset.
- The default value is [0, 0, 0].

### `dlCoordTolerance`

- A _List of Double_ specifying the coordinate tolerance.
- The default value is [0.0, 0.0, 0.0].

### `iConflictStrategy`

- An _Integer_ specifying the conflict resolution strategy.
- The default value is 0.

### `iSolver`

- An _Integer_ specifying the solver.
- The default value is 0.

### `bEnable`

- A _Boolean_ specifying whether to renumber the target.
- The default value is _False_.
