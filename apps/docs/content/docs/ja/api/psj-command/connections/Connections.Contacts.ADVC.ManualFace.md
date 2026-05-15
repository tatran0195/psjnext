---
title: "Connections.Contacts.ADVC.ManualFace()"
description: "Define contact settings between specified faces for the ADVC solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > ADVC > ManualFace"
macro _link: "[ContactManualFaceADVC](../../macro/connections/ContactManualFaceADVC)"
---

## Description

Define contact settings between specified faces for the ADVC solver.

## Syntax

```psj
Connections.Contacts.ADVC.ManualFace(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlMasterFaces

- Specify the master faces.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### crlSlaveFaces

- Specify the slave faces.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the contact name.
- The default value is "ContactADVC".

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the behavior type of the contact definition. The behavior type of contact definition is one of the following.
  - 0: General Type (Sliding Contact)
  - 1: Tied Type (Shell-Solid contact)
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSlidingType

- Specify the sliding type.
  - 0: Blank.
  - 1: Finite sliding.
  - 2: Small sliding.
  - 3: Not sliding.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iInitialState

- Specify the initial contact state.
  - 0: Blank.
  - 1: Auto - Auto-detect.
  - 2: Open - Start analysis from the non-contact state
  - 3: Close - Start analysis from the contact state .
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dInitialStateTol

- Specify the the tolerance value to determine the initial contact state.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dKineticFrictionCoef

- Specify the dynamic coefficient of friction.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dExponentialCoef

- Specify the exponential damping coefficient.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iBehavior

- Specify the the presence or absence of contact.
  - 0: Blank.
  - 1: Separation - Remove the contact restraint when the tensile force is generated.
  - 2: No Separation - Binding on all of the contact pairs that were found at the beginning of the contact search.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dClearance

- Specify the clearance amount.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iAdjustToClearance

- Specify whether or not avoid the collapse element in accordance with node movement by Adjust function. This argument is active when _iSlidingType=0_ or _iSlidingType=2_.
  - 0: Blank.
  - 1: Yes.
  - 2: No.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dInterference

- Specify the interference.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iAdjustToInterference

- Specify whether or not adjust to interference. This argument is active when _iSlidingType=1_ or _iSlidingType=3_.
  - 0: Blank.
  - 1: Yes.
  - 2: No.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAutoShrink

- Specify the presence or absence of penetration elimination.
  - 0: Blank.
  - 1: Yes.
  - 2: No.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAdjust

- Specify the whether or not move the slave node on the master surface so that the clearance goes to zero.
  - 0: Blank.
  - 1: Yes - Move all of the slave node.
  - 2: Value - Defines the distance to enable the node movement.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAdjustValue

- Specify the distance to enable the node movement.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dFrictionCoef

- Specify the coefficient of static friction.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMaxShear

- Specify the maximum shear stress.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dElasticSlip

- Specify the allowable amount of slip.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSlipTolerance

- Specify the allowable slip tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSearchWidth

- Specify the inside and outside determination parameter in the direction of the contact surface.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSearchGap

- Specify the normal direction search distance for the gap surface.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dSearchDepth

- Specify the the normal direction search distance for the penetration surface.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCriticalPenetration

- Specify the critical penetration amount.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iEstimationImpactTime

- Specify the contact pairs using prediction of collision and release time.
  - 0: Blank.
  - 1: Yes.
  - 2: No.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iFormula

- Specify the contact formulation type.
  - 0: Blank.
  - 1: Node to Segment: Node - Face contact
  - 2: Segment to Segment: Face - Face contact.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iConstraintType

- Specify the contact constraint type.
  - 0: Blank.
  - 1: Lagrange - Lagrange undetermined multiplier method.
  - 2: Penalty - Penalty method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iThermalDataType

- Specify the heat transfer coefficient of clearance dependency.
  - 0: Blank.
  - 1: Clearance Dependency - Define the heat transfer coefficient of the clearance dependency.
  - 2: Pressure Dependency  - Define the heat transfer coefficient of the pressure dependency.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iTypeId

- Specify the type ID.
  - 0:
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bTemperatureDependency

- Specify whether or not using temperature dependency data .
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iNumDependencies

- Specify the number of dependencies.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshTableClearance

- Specify the table of clearance dependency.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bStabilized

- Specify whether or not stabilization parameter is defined.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iStabilizeType

- Specify the type of contact stabilization coefficient.
  - 0: Blank.
  - 1: Stiffness - Stiffness ratio.
  - 2: Area - Area ratio.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dResidualFactor

- Specify the residual factor used to define the correction coefficient C1.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dEffectiveDist

- Specify the effective distance that is used to define the correction coefficient C2.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCN

- Specify the normal direction stabilization coefficient.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dCT

- Specify the tangential direction stabilization coefficient.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crlClearances

- Specify the list of clearances data.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crContactADVC

- Specify an existing contact settings item. If this parameter is used, the specified contact settings item will be modified. If it is left _None_, a new contact settings item will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### dSearchAngle

- Specify the search angle of normal vector of the master/slave surface
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iConstraintTypeExplicit

- Specify the contact constraint type in the explicit dynamic analysis.
  - 0: Blank.
  - 1: Kinematic: Constraint method.
  - 2: Penalty: Penalty method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPenaltyFact

- Specify the the penalty scale factor.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dPenaltyFactExplicit

- Specify the penalty scale factor in the explicit dynamic analysis.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the contact color.
- The default value is 16711680.

<!-- @since:5.0.1 @optional -->
### iAlgorithm

- Specify the contact setting target entity.
  - 0: Face to Face
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method type.
  - 0: MANUAL\_FACE.
  - 1: MANUAL\_GROUP.
  - 2: BY\_GROUP\_MATRIX.
  - 3: SHARE\_FACE.
  - 4: AUTO\_SETTING.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bPressureTemperatureDependency

- Specify whether or not using pressure temperature dependency data .
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iPressureDependencies

- Specify the number of pressure dependencies.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshPressureData

- Specify the table of pressure dependency.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iTyingType

- Specify the TyingType.
  - 0: Blank
  - 1: Rigid
  - 2: Shear Tying

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6250449)

created _contact = Connections.Contacts.ADVC.ManualFace(crlMasterFaces=[Face(24)], 
                                                       crlSlaveFaces=[Face(49)], 
                                                       strName="ContactADVC1", 
                                                       iInitialState=1, 
                                                       dInitialStateTol=1.0, 
                                                       dKineticFrictionCoef=1.0, 
                                                       dExponentialCoef=1.0, 
                                                       iBehavior=1, 
                                                       iAdjustToClearance=2, 
                                                       dInterference=2.0, 
                                                       iAdjustToInterference=1, 
                                                       iAdjust=2, 
                                                       dFrictionCoef=1.0, 
                                                       dMaxShear=1.0, 
                                                       dElasticSlip=1.0, 
                                                       dSlipTolerance=1.0, 
                                                       dSearchWidth=1.0, 
                                                       dSearchGap=1.0, 
                                                       dSearchDepth=1.0, 
                                                       dCriticalPenetration=1.0, 
                                                       iFormula=1, 
                                                       iThermalDataType=2, 
                                                       iTypeId=1, 
                                                       tshTableClearance=[1, 
                                                                          2, 
                                                                          0, 
                                                                          0], 
                                                       bStabilized=True, 
                                                       iStabilizeType=2, 
                                                       dSearchAngle=1.0, 
                                                       iConstraintTypeExplicit=2, 
                                                       dPenaltyFact=1.0, 
                                                       dPenaltyFactExplicit=1.0, 
                                                       tshPressureData=[1, 
                                                                        2, 
                                                                        0, 
                                                                        0])

JPT.Debugger(created _contact)
```
