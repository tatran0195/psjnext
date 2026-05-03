---
title: "Connections.Contacts.Abaqus.ContactTable()"
description: "Create LBC contact abaqus manual face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > Abaqus > ContactTable"
---

## Description

Create LBC contact abaqus manual face

## Syntax

```psj
Connections.Contacts.Abaqus.ContactTable(strName="", iContactMethod=0, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `iContactMethod` @type(Integer) @default(0)

- The contact method.

### `iContactType` @type(Integer) @default(0)

- The contact type.

### `iAlg` @type(Integer) @default(0)

- The algorithm.

### `dAdjustVal` @type(Double) @default(0.0)

- The adjust value.

### `dExtensionZone` @type(Double) @default(0.0)

- The extension zone.

### `dMaxPenetration` @type(Double) @default(0.0)

- The maximum penetration.

### `iSmallSliding` @type(Integer) @default(0)

- The small sliding.

### `dSmooth` @type(Double) @default(0.0)

- The smooth.

### `iFrictionType` @type(Integer) @default(0)

- The friction type.

### `dFrictionCoef1` @type(Double) @default(0.0)

- The friction coefficient 1.

### `dFrictionCoef2` @type(Double) @default(0.0)

- The friction coefficient 2.

### `dShearLimit` @type(Double) @default(0.0)

- The shear limit.

### `dSlipTol` @type(Double) @default(0.0)

- The slip tolerance.

### `dStaticFrictionCoef` @type(Double) @default(0.0)

- The static friction coefficient .

### `dKineticFrictionCoef` @type(Double) @default(0.0)

- The kinetic friction coefficient .

### `dDecayCoef` @type(Double) @default(0.0)

- The decay coefficient .

### `iAdjust` @type(Integer) @default(0)

- The adjust.

### `dPositonTol` @type(Double) @default(0.0)

- The positon tolerance.

### `iFormula` @type(Integer) @default(0)

- The formula.

### `iTie` @type(Integer) @default(0)

- The tie.

### `iPOCType` @type(Integer) @default(0)

- The POC type.

### `iAllowSeparation` @type(Integer) @default(0)

- The allow separation.

### `dSlope` @type(Double) @default(0.0)

- The slope.

### `tshPOCTsheet` @type(Table Sheet) @default(\[])

- The POC table sheet.

### `iClearanceType` @type(Integer) @default(0)

- The clearance type.

### `iClearanceTypeId` @type(Integer) @default(0)

- The clearance type ID.

### `bTemperatureDependency` @type(Boolean) @default(False)

- The temperature dependency.

### `iDependencies` @type(Integer) @default(0)

- The dependencies.

### `tshCDTsheet` @type(Table Sheet) @default(\[])

- The CD table sheet.

### `iPrsTypeId` @type(Integer) @default(0)

- The pressure type ID.

### `bPrsTemperatureDependency` @type(Boolean) @default(False)

- The pressure temperature dependency.

### `iPrsDependencies` @type(Integer) @default(0)

- The pressure dependencies.

### `tshPrsDTsheet` @type(Table Sheet) @default(\[])

- The pressure d table sheet.

### `crplTarget` @type(Cursor Pair List) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iColor` @type(Integer) @default(0)

- The color.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.Abaqus.ContactTable(strName="", iContactMethod=0, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)
```
