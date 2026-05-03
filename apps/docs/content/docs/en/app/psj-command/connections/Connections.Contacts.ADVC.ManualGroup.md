---
title: "Connections.Contacts.ADVC.ManualGroup()"
description: "Define contact settings between specified groups for the ADVC solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > ADVC > ManualGroup"
macro_link: "[ContactADVC](../../macro/connections/ContactADVC)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create ADVC contact Manual Group","Define contact settings between specified groups for the ADVC solver"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Define contact settings between specified groups for the ADVC solver.

## Syntax

```psj
Connections.Contacts.ADVC.ManualGroup(...)
```

## Inputs

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

### `iAdjust2Clearance` @type(Integer) @default(0)

- Whether or not avoid the collapse element in accordance with node movement by Adjust function. This argument is active whe&#x6E;_&#x69;SlidingType=&#x30;_&#x6F;&#x72;_&#x69;SlidingType=2_.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

### `dInterference` @type(Double) @default(DFLT\_DBL)

- The interference.

### `iAdjust2Interference` @type(Integer) @default(0)

- Whether or not adjust to interference. This argument is active whe&#x6E;_&#x69;SlidingType=&#x31;_&#x6F;&#x72;_&#x69;SlidingType=3_.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

### `iAutoShrink` @type(Integer) @default(0)

- The auto shrink.

### `iAdvAdjust` @type(Integer) @default(0)

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

### `dCritialPenetration` @type(Double) @default(DFLT\_DBL)

- The critical penetration amount.

### `iEstimationImpactTime` @type(Integer) @default(0)

- The contact pairs using prediction of collision and release time.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

### `iFormula` @type(Integer) @default(0)

- The formula.

### `iConstraintType` @type(Integer) @default(0)

- The constraint type.

### `iDataType` @type(Integer) @default(0)

- The heat transfer coefficient of clearance dependency.
  - 0: Blank.
  - 1: Clearance Dependency - Define the heat transfer coefficient of the clearance dependency.
  - 2: Pressure Dependency  - Define the heat transfer coefficient of the pressure dependency.

### `iTypeId` @type(Integer) @default(0)

- The type ID.

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

### `crlClearance` @type(List\[Cursor]) @default(\[])

- The list of clearances data.

### `crplTarget` @type(Cursor Pair List) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

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

### `iAlg` @type(Integer) @default(0)

- The contact setting target entity.
  - 0: Face to Face

### `iMethod` @type(Integer) @default(0)

- The method.

### `tshPressureData` @type(Table Sheet) @default(\[]) @since(5.1.0)

- The table of pressure dependency.

### `iTyingType` @type(Integer) @since(5.1.0)

- The TyingType.
  - 0: Blank
  - 1: Rigid
  - 2: Shear Tying

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{}
# Prepare model
Geometry.Part.Cube(
    iPartColor=6409934
)
Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7463537
)

# Prepare groups to set contact
Tools.Group.CreateGroup(
    strGroupName="Group1", crlTargets=[Face(24)]
)
Tools.Group.CreateGroup(
    strGroupName="Group2", crlTargets=[Face(49)]
)

# Create contact by group selection
Connections.Contacts.ADVC.ManualGroup(
    strName="ContactADVC_1", 
    iSlidingType=1, 
    dClearance=0.2, 
    dInterference=0.2, iAdvAdjust=1, 
    crplTarget=[CursorPair(Group(1), Group(2))]
)
```
