---
title: "HexModeling.BallHexa()"
description: "hexa modeling ball hexa"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > BallHexa"
---

## Description

Hexa modeling ball hexa

## Syntax

```psj
HexModeling.BallHexa(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crPart

- Specify the part.

<!-- @since:5.0.1 @optional -->
### vecCenter

- Specify the center.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dRadius

- Specify the radius.
- The default value is 5.0.

<!-- @since:5.0.1 @optional -->
### dMeshSize

- Specify the mesh size.
- The default value is 0.5.

<!-- @since:5.0.1 @optional -->
### iType

- Specify the type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iLayer

- Specify the layer.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### bMakeCenterNode

- Specify the make center node.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the part name.
- The default value is "HexBall\_1".

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {1-2}
HexModeling.BallHexa(crPart=None, vecCenter=[0.0,0.0,0.0], dRadius=5.0, dMeshSize=0.5, iType=0, 
    iLayer=3, bMakeCenterNode=True, strPartName="HexBall _1")
```
