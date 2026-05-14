---
title: "Connections.Contacts.ADVC.ContactGroupByMatrix()"
description: "create ADVC contact Group By Matrix"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > ADVC > ContactGroupByMatrix"
macro _link: "[LbcContactAdvc _ContactGroupByMatrix](../../macro/connections/LbcContactAdvc _ContactGroupByMatrix)"
---

## Description

Create ADVC contact Group By Matrix

## Syntax

```psj
Connections.Contacts.ADVC.ContactGroupByMatrix(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ContactADVC" -->
### `strName`

- The contact name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactType`

- The behavior type of the contact definition. The behavior type of contact definition is one of the following.
  - 0: General Type (Sliding Contact)
  - 1: Tied Type (Shell-Solid contact)

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSlidingType`

- The sliding type.
  - 0: Blank.
  - 1: Finite sliding.
  - 2: Small sliding.
  - 3: Not sliding.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInitialState`

- The initial contact state.
  - 0: Blank.
  - 1: Auto - Auto-detect.
  - 2: Open - Start analysis from the non-contact state
  - 3: Close - Start analysis from the contact state .

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dInitialStateTol`

- The tolerance value to determine the initial contact state.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dKineticFrictionCoef`

- The kinetic friction coefficient .

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dExponentialCoef`

- The exponential coefficient .

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iBehavior`

- The presence or absence of contact.
  - 0: Blank.
  - 1: Separation - Remove the contact restraint when the tensile force is generated.
  - 2: No Separation - Binding on all of the contact pairs that were found at the beginning of the contact search.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dClearance`

- The clearance amount.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdjust2Clearance`

- Whether or not avoid the collapse element in accordance with node movement by Adjust function. This argument is active when _iSlidingType=0_ or _iSlidingType=2_.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dInterference`

- The interference.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdjust2Interference`

- Whether or not adjust to interference. This argument is active when _iSlidingType=1_ or _iSlidingType=3_.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAutoShrink`

- The auto shrink.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdvAdjust`

- Whether or not move the slave node on the master surface so that the clearance goes to zero.
  - 0: Blank.
  - 1: Yes - Move all of the slave node.
  - 2: Value - Defines the distance to enable the node movement.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAdjustValue`

- The distance to enable the node movement.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFrictionCoef`

- The coefficient of static friction.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMaxShear`

- The maximum shear stress.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dElasticSlip`

- The allowable amount of slip.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSlipTolerance`

- The allowable slip tolerance.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchWidth`

- The inside and outside determination parameter in the direction of the contact surface.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchGap`

- The normal direction search distance for the gap surface.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchDepth`

- The normal direction search distance for the penetration surface.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCritialPenetration`

- The critical penetration amount.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEstimationImpactTime`

- The contact pairs using prediction of collision and release time.
  - 0: Blank.
  - 1: Yes.
  - 2: No.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFormula`

- The contact formulation type.
  - 0: Blank.
  - 1: Node to Segment: Node - Face contact
  - 2: Segment to Segment: Face - Face contact.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConstraintType`

- The constraint type.
  - 0: Blank.
  - 1: Lagrange - Lagrange undetermined multiplier method.
  - 2: Penalty - Penalty method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDataType`

- The heat transfer coefficient of clearance dependency.
  - 0: Blank.
  - 1: Clearance Dependency - Define the heat transfer coefficient of the clearance dependency.
  - 2: Pressure Dependency  - Define the heat transfer coefficient of the pressure dependency.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTypeId`

- The type ID.
  - 0: CLEARANCE\_DEPENDENCY.
  - 1: PRESSURE\_DEPENDENCY.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTemperatureDependency`

- Whether or not using temperature dependency data .

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iNumDependencies`

- The number of dependencies.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshTableClearance`

- The table of clearance dependency.

<!-- @since:5.0.1 @type:Boolean @optional @default:0 -->
### `bStabilized`

- Whether or not stabilization parameter is defined.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iStabilizeType`

- The type of contact stabilization coefficient.
  - 0: Blank.
  - 1: Stiffness - Stiffness ratio.
  - 2: Area - Area ratio.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dResidualFactor`

- The residual factor used to define the correction coefficient C1.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dEffectiveDist`

- The effective distance that is used to define the correction coefficient C2.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCN`

- The normal direction stabilization coefficient.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dCT`

- The tangential direction stabilization coefficient.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlClearance`

- The list of clearances data.

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplTarget`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing contact settings item. If this parameter is used, the specified contact settings item will be modified. If it is left _None_, a new contact settings item will be created.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSearchAngle`

- The search angle of normal vector of the master/slave surface

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConstraintTypeExplicit`

- The contact constraint type in the explicit dynamic analysis.
  - 0: Blank.
  - 1: Kinematic: Constraint method.
  - 2: Penalty: Penalty method.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPenaltyFact`

- The penalty scale factor.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dPenaltyFactExplicit`

- The penalty scale factor in the explicit dynamic analysis.

<!-- @since:5.0.1 @type:Integer @optional @default:16711680 -->
### `iColor`

- The contact color.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAlg`

- The contact setting target entity.
  - 0: Face to Face

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
<!-- @since:5.1.0 -->
### `iMethod`

- The method.
- Specify 1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {18-24}
# Prepare model
Geometry.Part.Cube(
    iPartColor=6409934
)
Geometry.Part.Cube(
    dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=7463537
)

# Prepare groups to set contact
Tools.Group.CreateGroup(
    strGroupName="Group1", crlTargets=[Face(24)]
)
Tools.Group.CreateGroup(
    strGroupName="Group2", crlTargets=[Face(49)]
)

# Create contact by group matrix
Connections.Contacts.ADVC.ContactGroupByMatrix(
    strName="ContactADVC _1", 
    iSlidingType=1, 
    dClearance=0.2, 
    dInterference=0.2, iAdvAdjust=1, 
    crplTarget=[CursorPair(Group(1), Group(2))]
)
```
