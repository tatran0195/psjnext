---
title: "Connections.Contacts.ADVC.ContactTable()"
description: "Create contacts for ADVC solver by using table"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > ADVC > ContactTable"
---

## Description

Create contacts for ADVC solver by using table.

## Syntax

```psj
Connections.Contacts.ADVC.ContactTable(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ContactADVC" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactType`

- The contact type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSlidingType`

- The sliding type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInitialState`

- The initial state.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dInitialStateTol`

- The initial state tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dKineticFrictionCoef`

- The kinetic friction coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExponentialCoef`

- The exponential coefficient .

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBehavior`

- The behavior.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dClearance`

- The clearance.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdjust2Clearance`

- The adjust2 clearance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dInterference`

- The interference.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdjust2Interference`

- The adjust2 interference.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAutoShrink`

- The auto shrink.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdvAdjust`

- The adv adjust.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAdjustValue`

- The adjust value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFrictionCoef`

- The friction coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxShear`

- The maximum shear.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dElasticSlip`

- The elastic slip.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSlipTolerance`

- The slip tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchWidth`

- The search width.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchGap`

- The search gap.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchDepth`

- The search depth.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCritialPenetration`

- The critial penetration.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEstimationImpactTime`

- The estimation impact time.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFormula`

- The formula.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConstraintType`

- The constraint type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDataType`

- The data type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTypeId`

- The type ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTemperatureDependency`

- The temperature dependency.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNumDependencies`

- The number dependencies.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshTableClearance`

- The table clearance.

<!-- @since:5.0.1 @type:Boolean @optional @default:0 -->
### `bStabilized`

- The stabilized.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iStabilizeType`

- The stabilize type.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dResidualFactor`

- The residual factor.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dEffectiveDist`

- The effective dist.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCN`

- The c n.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCT`

- The c t.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlClearance`

- The clearance.

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplTarget`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchAngle`

- The search angle.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConstraintTypeExplicit`

- The constraint type explicit.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPenaltyFact`

- The penalty fact.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPenaltyFactExplicit`

- The penalty fact explicit.

<!-- @since:5.0.1 @type:Integer @optional @default:16711680 -->
### `iColor`

- The color.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAlg`

- The algorithm.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], 
                   strName="Cube _3", 
                   iPartColor=6417130)
Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], 
                   strName="Cube _4", 
                   iPartColor=6053060)

created _contact = Connections.Contacts.ADVC.ContactTable(strName="ContactADVC", 
                                                         iContactType=0, 
                                                         iSlidingType=0, 
                                                         iInitialState=0, 
                                                         dInitialStateTol=DFLT _DBL, 
                                                         dKineticFrictionCoef=DFLT _DBL, 
                                                         dExponentialCoef=DFLT _DBL, 
                                                         iBehavior=0, 
                                                         dClearance=DFLT _DBL, 
                                                         iAdjust2Clearance=0, 
                                                         dInterference=DFLT _DBL, 
                                                         iAdjust2Interference=0, 
                                                         iAutoShrink=0, 
                                                         iAdvAdjust=0, 
                                                         dAdjustValue=DFLT _DBL, 
                                                         dFrictionCoef=DFLT _DBL, 
                                                         dMaxShear=DFLT _DBL, 
                                                         dElasticSlip=DFLT _DBL, 
                                                         dSlipTolerance=DFLT _DBL, 
                                                         dSearchWidth=DFLT _DBL, 
                                                         dSearchGap=DFLT _DBL, 
                                                         dSearchDepth=DFLT _DBL, 
                                                         dCritialPenetration=DFLT _DBL, 
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
                                                         dResidualFactor=DFLT _DBL, 
                                                         dEffectiveDist=DFLT _DBL, 
                                                         dCN=DFLT _DBL, 
                                                         dCT=DFLT _DBL, 
                                                         crlClearance=[], 
                                                         crplTarget=[], 
                                                         crEdit=None, 
                                                         dSearchAngle=DFLT _DBL, 
                                                         iConstraintTypeExplicit=0, 
                                                         dPenaltyFact=DFLT _DBL, 
                                                         dPenaltyFactExplicit=DFLT _DBL, 
                                                         iColor=16711680, 
                                                         iAlg=0, 
                                                         iMethod=0)

JPT.Debugger(created _contact)
```
