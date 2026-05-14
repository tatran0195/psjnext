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

<!-- @since:5.0.1 @type:Cursor @required -->
### `crPart`

- The part.

<!-- @since:5.0.1 @type:Vector @optional @default:[0.0,0.0,0.0] -->
### `vecCenter`

- The center.

<!-- @since:5.0.1 @type:Double @optional @default:5.0 -->
### `dRadius`

- The radius.

<!-- @since:5.0.1 @type:Double @optional @default:0.5 -->
### `dMeshSize`

- The mesh size.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Integer @optional @default:3 -->
### `iLayer`

- The layer.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bMakeCenterNode`

- The make center node.

<!-- @since:5.0.1 @type:String @optional @default:"HexBall _1" -->
### `strName`

- The part name.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {1-2}
HexModeling.BallHexa(crPart=None, vecCenter=[0.0,0.0,0.0], dRadius=5.0, dMeshSize=0.5, iType=0, 
    iLayer=3, bMakeCenterNode=True, strPartName="HexBall _1")
```
