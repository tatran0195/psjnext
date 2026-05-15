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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### iId

- Specify the ID.

<!-- @since:5.0.1 @optional -->
### crSection

- Specify the section.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crMat

- Specify the material.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### vecOrient

- Specify the orient.
- The default value is \[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Properties.Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT _DBL,DFLT _DBL,DFLT _DBL], crlTargets=[], crEdit=None)
```
