---
title: "Connections.Contacts.Abaqus.ContactShareFace()"
description: "Create LBC contact abaqus manual group"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Abaqus > ContactShareFace"
---

## Description

Create LBC contact abaqus manual group.

## Syntax

```psj
Connections.Contacts.Abaqus.ContactShareFace(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iContactMethod

- Specify the contact method.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the contact type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAlg

- Specify the algorithm.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAdjustVal

- Specify the adjust value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dExtensionZone

- Specify the extension zone.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxPenetration

- Specify the maximum penetration.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iSmallSliding

- Specify the small sliding.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSmooth

- Specify the smooth.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iFrictionType

- Specify the friction type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFrictionCoef1

- Specify the friction coefficient 1.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dFrictionCoef2

- Specify the friction coefficient 2.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dShearLimit

- Specify the shear limit.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dSlipTol

- Specify the slip tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStaticFrictionCoef

- Specify the static friction coefficient .
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dKineticFrictionCoef

- Specify the kinetic friction coefficient .
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dDecayCoef

- Specify the decay coefficient .
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iAdjust

- Specify the adjust.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPositonTol

- Specify the positon tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iFormula

- Specify the formula.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iTie

- Specify the tie.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPOCType

- Specify the POC type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAllowSeparation

- Specify the allow separation.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSlope

- Specify the slope.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### tshPOCTsheet

- Specify the POC table sheet.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iClearanceType

- Specify the clearance type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iClearanceTypeId

- Specify the clearance type ID.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bTemperatureDependency

- Specify the temperature dependency.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iDependencies

- Specify the dependencies.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshCDTsheet

- Specify the CD table sheet.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iPrsTypeId

- Specify the pressure type ID.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bPrsTemperatureDependency

- Specify the pressure temperature dependency.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iPrsDependencies

- Specify the pressure dependencies.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshPrsDTsheet

- Specify the pressure d table sheet.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crplTarget

- Specify the target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the color.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.Abaqus.ContactShareFace(strName="", iContactMethod=3, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)
```
