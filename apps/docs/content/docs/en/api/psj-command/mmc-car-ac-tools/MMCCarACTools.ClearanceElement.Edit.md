---
title: "MMCCarACTools.ClearanceElement.Edit()"
description: "Edit clearance elment"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MMCCarACTools > ClearanceElement > Edit"
---

## Description

Edit clearance elment

## Syntax

```psj
MMCCarACTools.ClearanceElement.Edit(dDx, dDy, dDz, dLx, dLy, dLz, crlTargets, crlDestNode, poslDestPoint)
```

## Inputs

<!-- @since:5.0.1 @type:Double @required -->
### `dDx`

- The dx.

<!-- @since:5.0.1 @type:Double @required -->
### `dDy`

- The dy.

<!-- @since:5.0.1 @type:Double @required -->
### `dDz`

- The dz.

<!-- @since:5.0.1 @type:Double @required -->
### `dLx`

- The lx.

<!-- @since:5.0.1 @type:Double @required -->
### `dLy`

- The ly.

<!-- @since:5.0.1 @type:Double @required -->
### `dLz`

- The lz.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlDestNode`

- The dest node.

<!-- @since:5.0.1 @type:Position List @required -->
### `poslDestPoint`

- The dest point.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ClearanceElement.Edit(dDx, dDy, dDz, dLx, dLy, dLz, crlTargets, crlDestNode, poslDestPoint)
```
