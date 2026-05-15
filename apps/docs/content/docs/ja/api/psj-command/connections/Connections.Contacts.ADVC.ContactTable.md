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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name.
- The default value is "ContactADVC".

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the contact type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSlidingType

- Specify the sliding type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInitialState

- Specify the initial state.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dInitialStateTol

- Specify the initial state tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dKineticFrictionCoef

- Specify the kinetic friction coefficient .
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dExponentialCoef

- Specify the exponential coefficient .
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iBehavior

- Specify the behavior.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dClearance

- Specify the clearance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iAdjust2Clearance

- Specify the adjust2 clearance.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dInterference

- Specify the interference.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iAdjust2Interference

- Specify the adjust2 interference.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAutoShrink

- Specify the auto shrink.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAdvAdjust

- Specify the adv adjust.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAdjustValue

- Specify the adjust value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dFrictionCoef

- Specify the friction coefficient .
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMaxShear

- Specify the maximum shear.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dElasticSlip

- Specify the elastic slip.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSlipTolerance

- Specify the slip tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSearchWidth

- Specify the search width.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSearchGap

- Specify the search gap.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSearchDepth

- Specify the search depth.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCritialPenetration

- Specify the critial penetration.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iEstimationImpactTime

- Specify the estimation impact time.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iFormula

- Specify the formula.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iConstraintType

- Specify the constraint type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDataType

- Specify the data type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iTypeId

- Specify the type ID.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bTemperatureDependency

- Specify the temperature dependency.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iNumDependencies

- Specify the number dependencies.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshTableClearance

- Specify the table clearance.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bStabilized

- Specify the stabilized.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iStabilizeType

- Specify the stabilize type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dResidualFactor

- Specify the residual factor.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dEffectiveDist

- Specify the effective dist.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCN

- Specify the c n.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCT

- Specify the c t.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crlClearance

- Specify the clearance.
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
### dSearchAngle

- Specify the search angle.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iConstraintTypeExplicit

- Specify the constraint type explicit.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPenaltyFact

- Specify the penalty fact.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dPenaltyFactExplicit

- Specify the penalty fact explicit.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the color.
- The default value is 16711680.

<!-- @since:5.0.1 @optional -->
### iAlg

- Specify the algorithm.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

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
