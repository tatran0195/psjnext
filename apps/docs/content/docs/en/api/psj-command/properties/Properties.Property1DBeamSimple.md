---
title: "Properties.Property1DBeamSimple()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Property1DBeamSimple"
macro _link: "[Property1DBeamSimple](../../macro/properties/Property1DBeamSimple)"
---

## Description

## Syntax

```psj
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT _DBL,DFLT _DBL,DFLT _DBL], crlTargets=[], crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @required -->
### `iId`

- The ID.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSection`

- The section.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMat`

- The material.

<!-- @since:5.0.1 @type:Vector @optional @default:[DFLT _DBL,DFLT _DBL,DFLT _DBL] -->
### `vecOrient`

- The orient.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT _DBL,DFLT _DBL,DFLT _DBL], crlTargets=[], crEdit=None)
```
