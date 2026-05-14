---
title: "SZOnepushReliability.Assembly.CreateWeld()"
description: "Create welding"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "SZOnepushReliability > Assembly > CreateWeld"
---

## Description

Create welding

## Syntax

```psj
SZOnepushReliability.Assembly.CreateWeld(crlWelds, dMeshSize, iRrate, dFilletRadius)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlWelds`

- The welds.

<!-- @since:5.0.1 @type:Double @required -->
### `dMeshSize`

- The mesh size.

<!-- @since:5.0.1 @type:Integer @required -->
### `iRrate`

- The rrate.

<!-- @since:5.0.1 @type:Double @required -->
### `dFilletRadius`

- The fillet radius.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.Assembly.CreateWeld(crlWelds, dMeshSize, iRrate, dFilletRadius)
```
