---
title: "Connections.Contacts.Abaqus.ContactTable()"
description: "Create LBC contact abaqus manual face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Abaqus > ContactTable"
---

## Description

Create LBC contact abaqus manual face

## Syntax

```psj
Connections.Contacts.Abaqus.ContactTable(strName="", iContactMethod=0, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactMethod`

- The contact method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactType`

- The contact type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAlg`

- The algorithm.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAdjustVal`

- The adjust value.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dExtensionZone`

- The extension zone.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMaxPenetration`

- The maximum penetration.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSmallSliding`

- The small sliding.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSmooth`

- The smooth.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFrictionType`

- The friction type.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFrictionCoef1`

- The friction coefficient 1.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFrictionCoef2`

- The friction coefficient 2.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dShearLimit`

- The shear limit.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSlipTol`

- The slip tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStaticFrictionCoef`

- The static friction coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dKineticFrictionCoef`

- The kinetic friction coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDecayCoef`

- The decay coefficient .

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdjust`

- The adjust.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dPositonTol`

- The positon tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFormula`

- The formula.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTie`

- The tie.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPOCType`

- The POC type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAllowSeparation`

- The allow separation.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSlope`

- The slope.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshPOCTsheet`

- The POC table sheet.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iClearanceType`

- The clearance type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iClearanceTypeId`

- The clearance type ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTemperatureDependency`

- The temperature dependency.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDependencies`

- The dependencies.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshCDTsheet`

- The CD table sheet.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPrsTypeId`

- The pressure type ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPrsTemperatureDependency`

- The pressure temperature dependency.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPrsDependencies`

- The pressure dependencies.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshPrsDTsheet`

- The pressure d table sheet.

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplTarget`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iColor`

- The color.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.Abaqus.ContactTable(strName="", iContactMethod=0, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)
```
