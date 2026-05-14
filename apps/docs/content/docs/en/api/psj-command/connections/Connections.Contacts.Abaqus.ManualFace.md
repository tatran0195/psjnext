---
title: "Connections.Contacts.Abaqus.ManualFace()"
description: "Define contact settings between specified faces for the Abaqus solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Abaqus > ManualFace"
---

## Description

Define contact settings between specified faces for the Abaqus solver.

## Syntax

```psj
Connections.Contacts.Abaqus.ManualFace(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ContactAbaqus _1" -->
### `strName`

- The contact name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactAlgorithm`

- The type of contact connection.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.
  - 1: Node to Face - Contact between node and shell or solid element faces.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactType`

- The behavior type of contact definition. The behavior type of contact definition is one of the following.
  - 0: General Type (Sliding Contact)
  - 1: Tied Type (Shell-Solid contact)
  - 2: All with self Type

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAlg`

- The contact setting target entity.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAdjustVal`

- The adjustment width of the initial node position.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dExtensionZone`

- The extended area.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMaxPenetration`

- The maximum penetration distance value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSmallSliding`

- The consideration of small-slip.
  - 0: OFF
  - 1: ON

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSmooth`

- The smoothing angle.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFrictionType`

- The friction characteristics type. The friction characteristics type is one of the following.
  - 0: None
  - 1: General
  - 2: Lagrange
  - 3: Rough
  - 4: Static & Kinetic

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFrictionCoef1`

- The friction coefficient 1 when Friction type is set as General or Lagrange.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFrictionCoef2`

- The friction coefficient 2 when Friction type is set as General or Lagrange.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dShearLimit`

- The Shear stress limit when Friction type is set as General or Lagrange.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSlipTol`

- The maximum allowable elastic slip for surface dimension ratio when Friction type is set as General or Static & Kinetic.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStaticFrictionCoef`

- The Coefficient of static friction when Friction type is set as Static & Kinetic.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dKineticFrictionCoef`

- The Coefficient of dynamic friction when Friction type is set as Static & Kinetic.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDecayCoef`

- The Reduction factor when Friction type is set as Static & Kinetic.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdjust`

- The consideration of adjustment.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dPositionTol`

- The position tolerance value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFormula`

- The contact formulation type.
  - 0: Node to Surface
  - 1: Surface to Surface

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTie`

- The fixed conditions and contact pair.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPOCType`

- The Contact thickness of the contact direction behavior, to define the penetration characteristics type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAllowSeparation`

- The separation option when pressure-overclosure type is set as Hard Contact.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSlope`

- The contact stiffness when pressure-overclosure type is set as Linear.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshPOCTsheet`

- The table of pressure-Overclosure when pressure-overclosure type is set as Exponential.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iClearanceType`

- The contact characteristic definition method of heat conduction.
  - 0: None
  - 1: Clearance Dependency
  - 2: Pressure Dependency
  - 3: Clearance & Pressure Dependency

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iClearanceTypeId`

- The clearance dependency type ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTemperatureDependency`

- The enable/disable using temperature dependency data.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDependencies`

- The number of the field variables.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshCDTsheet`

- The table of clearance dependency.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPrsTypeId`

- The pressure dependency type ID.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPrsTemperatureDependency`

- The enable/disable using temperature dependency data.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPrsDependencies`

- The number of the field variables.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshPrsDTsheet`

- The table of pressure dependency.

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplTargets`

- The list or pair of group master face and group slave face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing contact settings item. If this parameter is used, the specified contact settings item will be modified. If it is left _None_, a new contact settings item will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iColor`

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53}
Geometry.Part.Cube(iPartColor=15132254)
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                   strName="Cube _2",
                   iPartColor=6013120)
Geometry.Part.Cube(dlOrigin=[0.011, 0.01, 0.0],
                   strName="Cube _3",
                   iPartColor=5395146)
Tools.Group.CreateGroup(strGroupName="Group1",
                        crlTargets=[Face(73)])
Tools.Group.CreateGroup(strGroupName="Group2",
                        crlTargets=[Face(48)])
Assembly.RightClick.Rename(strNewName="Master",
                           crItem=Group(1))
Assembly.RightClick.Rename(strNewName="Slave",
                           crItem=Group(2))
Meshing.SolidMeshing(crlParts=[Part(1, 2, 3)],
                     bTet10=True,
                     dGradingFactor=1.05,
                     dStretchLimit=0.1,
                     iSpeedVsQual=1,
                     iRegion=1,
                     bSafeMode=False,
                     iParallel=12,
                     bInternalMeshOnly=False,
                     iPartColor=65280)
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _M",
                        crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _S",
                        crlTargets=[Face(49)])

# Create face contact (Abaqus)
creating _status = Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus _1",
                                                         dAdjustWidth=0.01,
                                                         dExtensionZone=DFLT _DBL,
                                                         dMaxPenetration=DFLT _DBL,
                                                         iSmallSliding=1,
                                                         dSmoothAngle=DFLT _DBL,
                                                         iFrictionType=1,
                                                         dFrictionCoeff1=0.015,
                                                         dFrictionCoeff2=DFLT _DBL,
                                                         dShearStressLimit=DFLT _DBL,
                                                         dSlipTolerance=DFLT _DBL,
                                                         dStaticFrictionCoeff=DFLT _DBL,
                                                         dKineticFrictionCoeff=DFLT _DBL,
                                                         dDecayCoeff=DFLT _DBL,
                                                         bAdjustPosition=True,
                                                         dPositionTolerance=DFLT _DBL,
                                                         dContactStiffness=DFLT _DBL,
                                                         tshPressureOverclosure=[0, 0],
                                                         tshClearanceData=[1, 2, DFLT _DBL, DFLT _DBL],
                                                         tshPressureData=[1, 2, DFLT _DBL, DFLT _DBL],
                                                         crplTargets=[CursorPair(Group(3), Group(4))],
                                                         iContactColor=16711680)

JPT.Debugger(creating _status)
```
