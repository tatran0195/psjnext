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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the contact name.
- The default value is "ContactAbaqus\_1".

<!-- @since:5.0.1 @optional -->
### iContactAlgorithm

- Specify the type of contact connection.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.
  - 1: Node to Face - Contact between node and shell or solid element faces.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the behavior type of contact definition. The behavior type of contact definition is one of the following.
  - 0: General Type (Sliding Contact)
  - 1: Tied Type (Shell-Solid contact)
  - 2: All with self Type
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAlg

- Specify the contact setting target entity.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAdjustVal

- Specify the adjustment width of the initial node position.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dExtensionZone

- Specify the extended area.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxPenetration

- Specify the maximum penetration distance value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iSmallSliding

- Specify the consideration of small-slip.
  - 0: OFF
  - 1: ON
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSmooth

- Specify the smoothing angle.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iFrictionType

- Specify the friction characteristics type. The friction characteristics type is one of the following.
  - 0: None
  - 1: General
  - 2: Lagrange
  - 3: Rough
  - 4: Static & Kinetic
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFrictionCoef1

- Specify the friction coefficient 1 when Friction type is set as General or Lagrange.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dFrictionCoef2

- Specify the friction coefficient 2 when Friction type is set as General or Lagrange.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dShearLimit

- Specify the Shear stress limit when Friction type is set as General or Lagrange.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dSlipTol

- Specify the maximum allowable elastic slip for surface dimension ratio when Friction type is set as General or Static & Kinetic.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStaticFrictionCoef

- Specify the Coefficient of static friction when Friction type is set as Static & Kinetic.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dKineticFrictionCoef

- Specify the Coefficient of dynamic friction when Friction type is set as Static & Kinetic.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dDecayCoef

- Specify the Reduction factor when Friction type is set as Static & Kinetic.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iAdjust

- Specify the consideration of adjustment.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dPositionTol

- Specify the position tolerance value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iFormula

- Specify the contact formulation type.
  - 0: Node to Surface
  - 1: Surface to Surface
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iTie

- Specify the fixed conditions and contact pair.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPOCType

- Specify the Contact thickness of the contact direction behavior, to define the penetration characteristics type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAllowSeparation

- Specify the separation option when pressure-overclosure type is set as Hard Contact.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSlope

- Specify the contact stiffness when pressure-overclosure type is set as Linear.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### tshPOCTsheet

- Specify the table of pressure-Overclosure when pressure-overclosure type is set as Exponential.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iClearanceType

- Specify the contact characteristic definition method of heat conduction.
  - 0: None
  - 1: Clearance Dependency
  - 2: Pressure Dependency
  - 3: Clearance & Pressure Dependency
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iClearanceTypeId

- Specify the clearance dependency type ID.
- The default value is 0.

### `bTemperatureDependency`

- A _Boolean_ enable/disable using temperature dependency data.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iDependencies

- Specify number of the field variables.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshCDTsheet

- Specify the table of clearance dependency.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iPrsTypeId

- Specify the pressure dependency type ID.
- The default value is 0.

### `bPrsTemperatureDependency`

- A _Boolean_ enable/disable using temperature dependency data.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iPrsDependencies

- Specify number of the field variables.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshPrsDTsheet

- Specify the table of pressure dependency.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crplTargets

- Specify the list or pair of group master face and group slave face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing contact settings item. If this parameter is used, the specified contact settings item will be modified. If it is left _None_, a new contact settings item will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iColor

- Specify the contact color.
- The default value is 0.

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
