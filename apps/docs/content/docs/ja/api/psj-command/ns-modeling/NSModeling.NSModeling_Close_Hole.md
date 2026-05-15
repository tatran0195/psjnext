---
title: "NSModeling.NSModeling _Close _Hole()"
description: "NSModeling NSModeling _Close _Hole"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "NSModeling > NSModeling _Close _Hole"
---

## Description

NSModeling NSModeling\_Close\_Hole

## Syntax

```psj
NSModeling.NSModeling _Close _Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNodes, crlParts)
```

## Inputs

<!-- @since:5.0.1 @required -->
### iType

- Specify the type.

<!-- @since:5.0.1 @required -->
### dMaxLength

- Specify the maximum length.

<!-- @since:5.0.1 @required -->
### bMergeFaces

- Specify the merge faces.

<!-- @since:5.0.1 @required -->
### bSetCenterPoint

- Specify the set center point.

<!-- @since:5.0.1 @required -->
### crlNodes

- Specify the node.

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the part.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
NSModeling.NSModeling _Close _Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNodes, crlParts)
```
