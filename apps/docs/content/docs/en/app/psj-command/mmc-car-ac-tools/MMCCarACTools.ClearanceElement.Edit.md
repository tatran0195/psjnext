---
title: "MMCCarACTools.ClearanceElement.Edit()"
description: "Edit clearance elment"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MMCCarACTools > ClearanceElement > Edit"
---

## Description

Edit clearance elment

## Syntax

```psj
MMCCarACTools.ClearanceElement.Edit(dDx, dDy, dDz, dLx, dLy, dLz, crlTargets, crlDestNode, poslDestPoint)
```

## Inputs

### `dDx` @type(Double) @required

- The dx.

### `dDy` @type(Double) @required

- The dy.

### `dDz` @type(Double) @required

- The dz.

### `dLx` @type(Double) @required

- The lx.

### `dLy` @type(Double) @required

- The ly.

### `dLz` @type(Double) @required

- The lz.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

### `crlDestNode` @type(List\[Cursor]) @required

- The dest node.

### `poslDestPoint` @type(Position List) @required

- The dest point.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ClearanceElement.Edit(dDx, dDy, dDz, dLx, dLy, dLz, crlTargets, crlDestNode, poslDestPoint)
```
