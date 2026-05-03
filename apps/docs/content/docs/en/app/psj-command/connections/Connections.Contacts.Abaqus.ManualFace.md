---
title: "Connections.Contacts.Abaqus.ManualFace()"
description: "Define contact settings between specified faces for the Abaqus solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > Abaqus > ManualFace"
---

## Description

Define contact settings between specified faces for the Abaqus solver.

## Syntax

```psj
Connections.Contacts.Abaqus.ManualFace(...)
```

## Inputs

### `strName` @type(String) @default("ContactAbaqus\_1")

- The contact name.

### `iContactAlgorithm` @type(Integer) @default(0)

- The type of contact connection.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.
  - 1: Node to Face - Contact between node and shell or solid element faces.

### `iContactType` @type(Integer) @default(0)

- The behavior type of contact definition. The behavior type of contact definition is one of the following.
  - 0: General Type (Sliding Contact)
  - 1: Tied Type (Shell-Solid contact)
  - 2: All with self Type

### `iAlg` @type(Integer) @default(0)

- The contact setting target entity.

### `dAdjustVal` @type(Double) @default(0.0)

- The adjustment width of the initial node position.

### `dExtensionZone` @type(Double) @default(0.0)

- The extended area.

### `dMaxPenetration` @type(Double) @default(0.0)

- The maximum penetration distance value.

### `iSmallSliding` @type(Integer) @default(0)

- The consideration of small-slip.
  - 0: OFF
  - 1: ON

### `dSmooth` @type(Double) @default(0.0)

- The smoothing angle.

### `iFrictionType` @type(Integer) @default(0)

- The friction characteristics type. The friction characteristics type is one of the following.
  - 0: None
  - 1: General
  - 2: Lagrange
  - 3: Rough
  - 4: Static & Kinetic

### `dFrictionCoef1` @type(Double) @default(0.0)

- The friction coefficient 1 when Friction type is set as General or Lagrange.

### `dFrictionCoef2` @type(Double) @default(0.0)

- The friction coefficient 2 when Friction type is set as General or Lagrange.

### `dShearLimit` @type(Double) @default(0.0)

- The Shear stress limit when Friction type is set as General or Lagrange.

### `dSlipTol` @type(Double) @default(0.0)

- The maximum allowable elastic slip for surface dimension ratio when Friction type is set as General or Static & Kinetic.

### `dStaticFrictionCoef` @type(Double) @default(0.0)

- The Coefficient of static friction when Friction type is set as Static & Kinetic.

### `dKineticFrictionCoef` @type(Double) @default(0.0)

- The Coefficient of dynamic friction when Friction type is set as Static & Kinetic.

### `dDecayCoef` @type(Double) @default(0.0)

- The Reduction factor when Friction type is set as Static & Kinetic.

### `iAdjust` @type(Integer) @default(0)

- The consideration of adjustment.

### `dPositionTol` @type(Double) @default(0.0)

- The position tolerance value.

### `iFormula` @type(Integer) @default(0)

- The contact formulation type.
  - 0: Node to Surface
  - 1: Surface to Surface

### `iTie` @type(Integer) @default(0)

- The fixed conditions and contact pair.

### `iPOCType` @type(Integer) @default(0)

- The Contact thickness of the contact direction behavior, to define the penetration characteristics type.

### `iAllowSeparation` @type(Integer) @default(0)

- The separation option when pressure-overclosure type is set as Hard Contact.

### `dSlope` @type(Double) @default(0.0)

- The contact stiffness when pressure-overclosure type is set as Linear.

### `tshPOCTsheet` @type(Table Sheet) @default(\[])

- The table of pressure-Overclosure when pressure-overclosure type is set as Exponential.

### `iClearanceType` @type(Integer) @default(0)

- The contact characteristic definition method of heat conduction.
  - 0: None
  - 1: Clearance Dependency
  - 2: Pressure Dependency
  - 3: Clearance & Pressure Dependency

### `iClearanceTypeId` @type(Integer) @default(0)

- The clearance dependency type ID.

### `bTemperatureDependency` @type(Boolean) @default(False)

- Enable/disable using temperature dependency data.

### `iDependencies` @type(Integer) @default(0)

- Number of the field variables.

### `tshCDTsheet` @type(Table Sheet) @default(\[])

- The table of clearance dependency.

### `iPrsTypeId` @type(Integer) @default(0)

- The pressure dependency type ID.

### `bPrsTemperatureDependency` @type(Boolean) @default(False)

- Enable/disable using temperature dependency data.

### `iPrsDependencies` @type(Integer) @default(0)

- Number of the field variables.

### `tshPrsDTsheet` @type(Table Sheet) @default(\[])

- The table of pressure dependency.

### `crplTargets` @type(Cursor Pair List) @default(\[])

- The list or pair of group master face and group slave face.

### `crEdit` @type(Cursor) @default(None)

- An existing contact settings item. If this parameter is used, the specified contact settings item will be modified. If it is lef&#x74;_&#x4E;one_, a new contact settings item will be created.

### `iColor` @type(Integer) @default(0)

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53}
Geometry.Part.Cube(iPartColor=15132254)
Geometry.Part.Cube(dlOrigin=[0.011, 0.0, 0.0], 
                   strName="Cube_2",
                   iPartColor=6013120)
Geometry.Part.Cube(dlOrigin=[0.011, 0.01, 0.0],
                   strName="Cube_3",
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
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M",
                        crlTargets=[Face(24)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S",
                        crlTargets=[Face(49)])

# Create face contact (Abaqus)
creating_status = Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus_1",
                                                         dAdjustWidth=0.01,
                                                         dExtensionZone=DFLT_DBL,
                                                         dMaxPenetration=DFLT_DBL,
                                                         iSmallSliding=1,
                                                         dSmoothAngle=DFLT_DBL,
                                                         iFrictionType=1,
                                                         dFrictionCoeff1=0.015,
                                                         dFrictionCoeff2=DFLT_DBL,
                                                         dShearStressLimit=DFLT_DBL,
                                                         dSlipTolerance=DFLT_DBL,
                                                         dStaticFrictionCoeff=DFLT_DBL,
                                                         dKineticFrictionCoeff=DFLT_DBL,
                                                         dDecayCoeff=DFLT_DBL,
                                                         bAdjustPosition=True,
                                                         dPositionTolerance=DFLT_DBL,
                                                         dContactStiffness=DFLT_DBL,
                                                         tshPressureOverclosure=[0, 0],
                                                         tshClearanceData=[1, 2, DFLT_DBL, DFLT_DBL],
                                                         tshPressureData=[1, 2, DFLT_DBL, DFLT_DBL],
                                                         crplTargets=[CursorPair(Group(3), Group(4))],
                                                         iContactColor=16711680)

JPT.Debugger(creating_status)
```
