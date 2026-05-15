---
title: "MidPlane.CreateThickProps()"
description: "create thickness properties for mid-plane"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlane > CreateThickProps"
---

## Description

Create thickness properties for mid-plane

## Syntax

```psj
MidPlane.CreateThickProps(crlParts=[], dThickDiff=0.1, dMaxThick=DFLT _DBL, dMinThick=DFLT _DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT _DBL, dMatOrientY=DFLT _DBL, dMatOrientZ=DFLT _DBL, crCoord=None, dThickness=DFLT _DBL, dBendStiff=DFLT _DBL, dThickRatio=1, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL, dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[])
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dThickDiff

- Specify the thickness difference.
- The default value is 0.1.

<!-- @since:5.0.1 @optional -->
### dMaxThick

- Specify the maximum thickness.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMinThick

- Specify the minimum thickness.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crMatMembrane

- Specify the material membrane.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crMatBend

- Specify the material bend.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crMatShear

- Specify the material shear.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crMatCoupl

- Specify the material couple.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iMatOrientType

- Specify the material orient type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dMatOrientX

- Specify the material orient x.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMatOrientY

- Specify the material orient y.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMatOrientZ

- Specify the material orient z.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dThickness

- Specify the thickness.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dBendStiff

- Specify the bend stiff.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dThickRatio

- Specify the thickness ratio.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### dNSM

- Specify the n s m.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dFiberDist1

- Specify the fiber distance 1.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dFiberDist2

- Specify the fiber distance 2.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dPlateOff

- Specify the plate off.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iNumInterPts

- Specify the number inter pts.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bThickSetting

- Specify the thickness setting.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iEntityType

- Specify the entity type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bDivideProp

- Specify the divide property.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crlRefPart

- Specify the reference part.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlane.CreateThickProps(crlParts=[], dThickDiff=0.1, dMaxThick=DFLT _DBL, dMinThick=DFLT _DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT _DBL, dMatOrientY=DFLT _DBL, dMatOrientZ=DFLT _DBL, crCoord=None, dThickness=DFLT _DBL, dBendStiff=DFLT _DBL, dThickRatio=1, dNSM=DFLT _DBL, dFiberDist1=DFLT _DBL, dFiberDist2=DFLT _DBL, dPlateOff=DFLT _DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[])
```
