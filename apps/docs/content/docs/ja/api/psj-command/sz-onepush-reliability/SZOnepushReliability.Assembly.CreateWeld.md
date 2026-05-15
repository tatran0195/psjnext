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

<!-- @since:5.0.1 @required -->
### crlWelds

- Specify the welds.

<!-- @since:5.0.1 @required -->
### dMeshSize

- Specify the mesh size.

<!-- @since:5.0.1 @required -->
### iRrate

- Specify the rrate.

<!-- @since:5.0.1 @required -->
### dFilletRadius

- Specify the fillet radius.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
SZOnepushReliability.Assembly.CreateWeld(crlWelds, dMeshSize, iRrate, dFilletRadius)
```
