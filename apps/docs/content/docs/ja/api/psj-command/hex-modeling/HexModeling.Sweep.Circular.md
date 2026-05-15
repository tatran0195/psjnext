---
title: "HexModeling.Sweep.Circular()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "HexModeling > Sweep > Circular"
---

## Description

Unknown Description

## Syntax

```psj
HexModeling.Sweep.Circular(crlFaces=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dAngle

- Specify the angle.
- The default value is 360.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is 0.0000001.

<!-- @since:5.0.1 @optional -->
### iLayer

- Specify the layer.
- The default value is 36.

<!-- @since:5.0.1 @optional -->
### vecAxisPt

- Specify the axis point.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### vecAxisVect

- Specify the axis vector.
- The default value is \[1.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### bInterfaceElem

- Specify the interface element.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bExtrusion

- Specify the extrusion.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dTranslationExtrusion

- Specify the translation extrusion.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dBDeleteOriginalParts

- Specify the delete original parts.
- The default value is 0.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
HexModeling.Sweep.Circular(crlFaces=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)
```
