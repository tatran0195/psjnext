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

<!-- @since:5.0.1 @required -->
### dDx

- Specify the dx.

<!-- @since:5.0.1 @required -->
### dDy

- Specify the dy.

<!-- @since:5.0.1 @required -->
### dDz

- Specify the dz.

<!-- @since:5.0.1 @required -->
### dLx

- Specify the lx.

<!-- @since:5.0.1 @required -->
### dLy

- Specify the ly.

<!-- @since:5.0.1 @required -->
### dLz

- Specify the lz.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

<!-- @since:5.0.1 @required -->
### crlDestNode

- Specify the dest node.

<!-- @since:5.0.1 @required -->
### poslDestPoint

- Specify the dest point.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MMCCarACTools.ClearanceElement.Edit(dDx, dDy, dDz, dLx, dLy, dLz, crlTargets, crlDestNode, poslDestPoint)
```
