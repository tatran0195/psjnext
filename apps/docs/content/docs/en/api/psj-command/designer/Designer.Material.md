---
title: "Designer.Material()"
description: "Create a material."
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Designer > Material"
---

## Description

Create a material.

## Syntax

```psj
Designer.Material(strMatName, strPropName, dThickness, crlTargets)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strMatName`

- The material name.

<!-- @since:5.0.1 @type:String @required -->
### `strPropName`

- The property name.

<!-- @since:5.0.1 @type:Double @required -->
### `dThickness`

- The thickness.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Designer.Material(strMatName, strPropName, dThickness, crlTargets)
```
