---
title: "Connections.Contacts.ADVC.ContactTable()"
description: "Create contacts for ADVC solver by using table"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > ADVC > ContactTable"
---

## Description

Create contacts for ADVC solver by using table.

## Syntax

```psj
Connections.Contacts.ADVC.ContactTable(...)
```

## Inputs

### `strName` @type(String) @default("ContactADVC")

- The name.

### `iContactType` @type(Integer) @default(0)

- The contact type.

### `iSlidingType` @type(Integer) @default(0)

- The sliding type.

### `iInitialState` @type(Integer) @default(0)

- The initial state.

### `dInitialStateTol` @type(Double) @default(DFLT\_DBL)

- The initial state tolerance.

### `dKineticFrictionCoef` @type(Double) @default(DFLT\_DBL)

- The kinetic friction coefficient .

### `dExponentialCoef` @type(Double) @default(DFLT\_DBL)

- The exponential coefficient .

### `iBehavior` @type(Integer) @default(0)

- The behavior.

### `dClearance` @type(Double) @default(DFLT\_DBL)

- The clearance.

### `iAdjust2Clearance` @type(Integer) @default(0)

- The adjust2 clearance.

### `dInterference` @type(Double) @default(DFLT\_DBL)

- The interference.

### `iAdjust2Interference` @type(Integer) @default(0)

- The adjust2 interference.

### `iAutoShrink` @type(Integer) @default(0)

- The auto shrink.

### `iAdvAdjust` @type(Integer) @default(0)

- The adv adjust.

### `dAdjustValue` @type(Double) @default(DFLT\_DBL)

- The adjust value.

### `dFrictionCoef` @type(Double) @default(DFLT\_DBL)

- The friction coefficient .

### `dMaxShear` @type(Double) @default(DFLT\_DBL)

- The maximum shear.

### `dElasticSlip` @type(Double) @default(DFLT\_DBL)

- The elastic slip.

### `dSlipTolerance` @type(Double) @default(DFLT\_DBL)

- The slip tolerance.

### `dSearchWidth` @type(Double) @default(DFLT\_DBL)

- The search width.

### `dSearchGap` @type(Double) @default(DFLT\_DBL)

- The search gap.

### `dSearchDepth` @type(Double) @default(DFLT\_DBL)

- The search depth.

### `dCritialPenetration` @type(Double) @default(DFLT\_DBL)

- The critial penetration.

### `iEstimationImpactTime` @type(Integer) @default(0)

- The estimation impact time.

### `iFormula` @type(Integer) @default(0)

- The formula.

### `iConstraintType` @type(Integer) @default(0)

- The constraint type.

### `iDataType` @type(Integer) @default(0)

- The data type.

### `iTypeId` @type(Integer) @default(0)

- The type ID.

### `bTemperatureDependency` @type(Boolean) @default(False)

- The temperature dependency.

### `iNumDependencies` @type(Integer) @default(0)

- The number dependencies.

### `tshTableClearance` @type(Table Sheet) @default(\[])

- The table clearance.

### `bStabilized` @type(Boolean) @default(0)

- The stabilized.

### `iStabilizeType` @type(Integer) @default(0)

- The stabilize type.

### `dResidualFactor` @type(Double) @default(DFLT\_DBL)

- The residual factor.

### `dEffectiveDist` @type(Double) @default(DFLT\_DBL)

- The effective dist.

### `dCN` @type(Double) @default(DFLT\_DBL)

- The c n.

### `dCT` @type(Double) @default(DFLT\_DBL)

- The c t.

### `crlClearance` @type(List\[Cursor]) @default(\[])

- The clearance.

### `crplTarget` @type(Cursor Pair List) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `dSearchAngle` @type(Double) @default(DFLT\_DBL)

- The search angle.

### `iConstraintTypeExplicit` @type(Integer) @default(0)

- The constraint type explicit.

### `dPenaltyFact` @type(Double) @default(DFLT\_DBL)

- The penalty fact.

### `dPenaltyFactExplicit` @type(Double) @default(DFLT\_DBL)

- The penalty fact explicit.

### `iColor` @type(Integer) @default(16711680)

- The color.

### `iAlg` @type(Integer) @default(0)

- The algorithm.

### `iMethod` @type(Integer) @default(0)

- The method.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], 
                   strName="Cube_3", 
                   iPartColor=6417130)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube_4", 
                   iPartColor=6053060)

created_contact = Connections.Contacts.ADVC.ContactTable(strName="ContactADVC", 
                                                         iContactType=0, 
                                                         iSlidingType=0, 
                                                         iInitialState=0, 
                                                         dInitialStateTol=DFLT_DBL, 
                                                         dKineticFrictionCoef=DFLT_DBL, 
                                                         dExponentialCoef=DFLT_DBL, 
                                                         iBehavior=0, 
                                                         dClearance=DFLT_DBL, 
                                                         iAdjust2Clearance=0, 
                                                         dInterference=DFLT_DBL, 
                                                         iAdjust2Interference=0, 
                                                         iAutoShrink=0, 
                                                         iAdvAdjust=0, 
                                                         dAdjustValue=DFLT_DBL, 
                                                         dFrictionCoef=DFLT_DBL, 
                                                         dMaxShear=DFLT_DBL, 
                                                         dElasticSlip=DFLT_DBL, 
                                                         dSlipTolerance=DFLT_DBL, 
                                                         dSearchWidth=DFLT_DBL, 
                                                         dSearchGap=DFLT_DBL, 
                                                         dSearchDepth=DFLT_DBL, 
                                                         dCritialPenetration=DFLT_DBL, 
                                                         iEstimationImpactTime=0,
                                                         iFormula=0, 
                                                         iConstraintType=0, 
                                                         iDataType=0, 
                                                         iTypeId=0, 
                                                         bTemperatureDependency=False, 
                                                         iNumDependencies=0, 
                                                         tshTableClearance=[],
                                                         bStabilized=0, 
                                                         iStabilizeType=0, 
                                                         dResidualFactor=DFLT_DBL, 
                                                         dEffectiveDist=DFLT_DBL, 
                                                         dCN=DFLT_DBL, 
                                                         dCT=DFLT_DBL, 
                                                         crlClearance=[], 
                                                         crplTarget=[], 
                                                         crEdit=None, 
                                                         dSearchAngle=DFLT_DBL, 
                                                         iConstraintTypeExplicit=0, 
                                                         dPenaltyFact=DFLT_DBL, 
                                                         dPenaltyFactExplicit=DFLT_DBL, 
                                                         iColor=16711680, 
                                                         iAlg=0, 
                                                         iMethod=0)

JPT.Debugger(created_contact)
```
