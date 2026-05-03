---
title: "SZOnepushReliability.Assembly.CreateWeld()"
description: "Create welding"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "SZOnepushReliability > Assembly > CreateWeld"
---

## Description

Create welding

## Syntax

```psj
SZOnepushReliability.Assembly.CreateWeld(crlWelds, dMeshSize, iRrate, dFilletRadius)
```

## Inputs

### `crlWelds` @type(List\[Cursor]) @required

- The welds.

### `dMeshSize` @type(Double) @required

- The mesh size.

### `iRrate` @type(Integer) @required

- The rrate.

### `dFilletRadius` @type(Double) @required

- The fillet radius.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.Assembly.CreateWeld(crlWelds, dMeshSize, iRrate, dFilletRadius)
```
