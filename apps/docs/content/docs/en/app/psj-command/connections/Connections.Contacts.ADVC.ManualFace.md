---
title: "Connections.Contacts.ADVC.ManualFace()"
description: "Define contact settings between specified faces for the ADVC solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > ADVC > ManualFace"
macro_link: "[ContactManualFaceADVC](../../macro/connections/ContactManualFaceADVC)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Define contact settings between specified faces for the ADVC solver.

## Syntax

```psj
Connections.Contacts.ADVC.ManualFace(...)
```

## Inputs

### `crlMasterFaces` @type(List\[Cursor])

- The master faces.
- This is the required input.

### `crlSlaveFaces` @type(List\[Cursor])

- The slave faces.
- This is the required input.

### `strName` @type(String) @default("ContactADVC")

- The contact name.

### `iContactType` @type(Integer) @default(0)

- The behavior type of the contact definition. The behavior type of contact definition is one of the following.
  - 0: General Type (Sliding Contact)
  - 1: Tied Type (Shell-Solid contact)

### `iSlidingType` @type(Integer) @default(0)

- The sliding type.
  - 0: Blank.
  - 1: Finite sliding.
  - 2: Small sliding.
  - 3: Not sliding.

### `iInitialState` @type(Integer) @default(0)

- The initial contact state.
  - 0: Blank.
  - 1: Auto - Auto-detect.
  - 2: Open - Start analysis from the non-contact state
  - 3: Close - Start analysis from the contact state .

### `dInitialStateTol` @type(Double) @default(DFLT\_DBL)

- The the tolerance value to determine the initial contact state.

### `dKineticFrictionCoef` @type(Double) @default(DFLT\_DBL)

- The dynamic coefficient of friction.

### `dExponentialCoef` @type(Double) @default(DFLT\_DBL)

- The exponential damping coefficient.

### `iBehavior` @type(Integer) @default(0)

- The the presence or absence of contact.
  - 0: Blank.
  - 1: Separation - Remove the contact restraint when the tensile force is generated.
  - 2: No Separation - Binding on all of the contact pairs that were found at the beginning of the contact search.

### `dClearance` @type(Double) @default(DFLT\_DBL)

- The clearance amount.

### `iAdjustToClearance` @type(Integer) @default(0)

- Whether or not avoid the collapse element in accordance with node movement by Adjust function. This argument is active whe&#x6E;_&#x69;SlidingType=&#x30;_&#x6F;&#x72;_&#x69;SlidingType=2_.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

### `dInterference` @type(Double) @default(DFLT\_DBL)

- The interference.

### `iAdjustToInterference` @type(Integer) @default(0)

- Whether or not adjust to interference. This argument is active whe&#x6E;_&#x69;SlidingType=&#x31;_&#x6F;&#x72;_&#x69;SlidingType=3_.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

### `iAutoShrink` @type(Integer) @default(0)

- The presence or absence of penetration elimination.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

### `iAdjust` @type(Integer) @default(0)

- The whether or not move the slave node on the master surface so that the clearance goes to zero.
  - 0: Blank.
  - 1: Yes - Move all of the slave node.
  - 2: Value - Defines the distance to enable the node movement.

### `dAdjustValue` @type(Double) @default(DFLT\_DBL)

- The distance to enable the node movement.

### `dFrictionCoef` @type(Double) @default(DFLT\_DBL)

- The coefficient of static friction.

### `dMaxShear` @type(Double) @default(DFLT\_DBL)

- The maximum shear stress.

### `dElasticSlip` @type(Double) @default(DFLT\_DBL)

- The allowable amount of slip.

### `dSlipTolerance` @type(Double) @default(DFLT\_DBL)

- The allowable slip tolerance.

### `dSearchWidth` @type(Double) @default(DFLT\_DBL)

- The inside and outside determination parameter in the direction of the contact surface.

### `dSearchGap` @type(Double) @default(DFLT\_DBL)

- The normal direction search distance for the gap surface.

### `dSearchDepth` @type(Double) @default(DFLT\_DBL)

- The the normal direction search distance for the penetration surface.

### `dCriticalPenetration` @type(Double) @default(DFLT\_DBL)

- The critical penetration amount.

### `iEstimationImpactTime` @type(Integer) @default(0)

- The contact pairs using prediction of collision and release time.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

### `iFormula` @type(Integer) @default(0)

- The contact formulation type.
  - 0: Blank.
  - 1: Node to Segment: Node - Face contact
  - 2: Segment to Segment: Face - Face contact.

### `iConstraintType` @type(Integer) @default(0)

- The contact constraint type.
  - 0: Blank.
  - 1: Lagrange - Lagrange undetermined multiplier method.
  - 2: Penalty - Penalty method.

### `iThermalDataType` @type(Integer) @default(0)

- The heat transfer coefficient of clearance dependency.
  - 0: Blank.
  - 1: Clearance Dependency - Define the heat transfer coefficient of the clearance dependency.
  - 2: Pressure Dependency  - Define the heat transfer coefficient of the pressure dependency.

### `iTypeId` @type(Integer) @default(0)

- The type ID.
  - 0:

### `bTemperatureDependency` @type(Boolean) @default(False)

- Whether or not using temperature dependency data .

### `iNumDependencies` @type(Integer) @default(0)

- The number of dependencies.

### `tshTableClearance` @type(Table Sheet) @default(\[])

- The table of clearance dependency.

### `bStabilized` @type(Boolean) @default(0)

- Whether or not stabilization parameter is defined.

### `iStabilizeType` @type(Integer) @default(0)

- The type of contact stabilization coefficient.
  - 0: Blank.
  - 1: Stiffness - Stiffness ratio.
  - 2: Area - Area ratio.

### `dResidualFactor` @type(Double) @default(DFLT\_DBL)

- The residual factor used to define the correction coefficient C1.

### `dEffectiveDist` @type(Double) @default(DFLT\_DBL)

- The effective distance that is used to define the correction coefficient C2.

### `dCN` @type(Double) @default(DFLT\_DBL)

- The normal direction stabilization coefficient.

### `dCT` @type(Double) @default(DFLT\_DBL)

- The tangential direction stabilization coefficient.

### `crlClearances` @type(List\[Cursor]) @default(\[])

- The list of clearances data.

### `crContactADVC` @type(Cursor) @default(None)

- An existing contact settings item. If this parameter is used, the specified contact settings item will be modified. If it is lef&#x74;_&#x4E;one_, a new contact settings item will be created.

### `dSearchAngle` @type(Double) @default(DFLT\_DBL)

- The search angle of normal vector of the master/slave surface

### `iConstraintTypeExplicit` @type(Integer) @default(0)

- The contact constraint type in the explicit dynamic analysis.
  - 0: Blank.
  - 1: Kinematic: Constraint method.
  - 2: Penalty: Penalty method.

### `dPenaltyFact` @type(Double) @default(DFLT\_DBL)

- The the penalty scale factor.

### `dPenaltyFactExplicit` @type(Double) @default(DFLT\_DBL)

- The penalty scale factor in the explicit dynamic analysis.

### `iColor` @type(Integer) @default(16711680)

- The contact color.

### `iAlgorithm` @type(Integer) @default(0)

- The contact setting target entity.
  - 0: Face to Face

### `iMethod` @type(Integer) @default(0)

- The method type.
  - 0: MANUAL\_FACE.
  - 1: MANUAL\_GROUP.
  - 2: BY\_GROUP\_MATRIX.
  - 3: SHARE\_FACE.
  - 4: AUTO\_SETTING.

### `bPressureTemperatureDependency` @type(Boolean) @default(False)

- Whether or not using pressure temperature dependency data .

### `iPressureDependencies` @type(Integer) @default(0)

- The number of pressure dependencies.

### `tshPressureData` @type(Table Sheet) @default(\[])

- The table of pressure dependency.

### `iTyingType` @type(Integer) @since(5.1.0)

- The TyingType.
  - 0: Blank
  - 1: Rigid
  - 2: Shear Tying

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

created_contact = Connections.Contacts.ADVC.ManualFace(crlMasterFaces=[Face(24)], 
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

JPT.Debugger(created_contact)
```
