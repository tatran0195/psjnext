---
title: "Connections.Contacts.Abaqus.ManualGroup()"
description: "Define the contact set between the specified group for Abaqus. Create a group with master and slave surfaces beforehand to define the contact in the contact settings"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > Abaqus > Manual Group"
---

## Description

Define the contact set between the specified group for Abaqus. Create a group with master and slave surfaces beforehand to define the contact in the contact settings.

## Syntax

```psj
Connections.Contacts.Abaqus.ManualGroup(...)
```

## Inputs

### `strName` @type(String) @default("ContactAbaqus\_1")

- The new Abaqus Contact name.

### `iContactType` @type(Integer) @default(0)

- The behavior type of contact definition. The behavior type of contact definition is one of the following:
  - 0: General (Sliding Contact)
  - 1: Tied (Shell-Solid contact)
  - 2: All with self - Automatic contact detection

### `iContactAlgorithm` @type(Integer) @default(0)

- The contact setting target entity.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.
  - 1: Node to Face - Contact between node and shell or solid element faces.

### `dAdjustWidth` @type(Double) @default(0.0)

- A value to adjust the initial positions of the surfaces specified. This is required when th&#x65;_&#x69;Tie&#x64;_&#x70;arameter is used with ON value. This argument is used only whe&#x6E;_&#x69;ContactType=0_.

### `dExtensionZone` @type(Double) @default(0.0)

- A value that is equal to a fraction of the end segment or facet edge length by which Abaqus extends the master surface to avoid numerical round-off errors associated with contact modeling. The value given must lie between 0.0 and 0.2. This parameter affects only node-to-surface contact. This argument is used only whe&#x6E;_&#x69;ContactType=0_.

### `dMaxPenetration` @type(Double) @default(0.0)

- The maximum distance by which a point on the slave surface must penetrate the master surface before Abaqus abandons the current increment and tries again with a smaller increment. This parameter does not apply to contact pairs that use the finite-sliding, surface-to-surface contact formulation. This argument is used only whe&#x6E;_&#x69;ContactType=0_.

### `iSmallSliding` @type(Integer) @default(0)

- Whether to use the small-sliding contact formulation. This parameter is not allowed with self-contact. This argument is used only whe&#x6E;_&#x69;ContactType=0_.
  - 0: OFF
  - 1: ON

### `dSmoothAngle` @type(Double) @default(0.0)

- The degree of smoothing used for element-based master surfaces in the finite-sliding, node-to-surface contact formulation. The value given must lie between 0.0 and 0.5. This parameter does not affect contact pairs with analytical rigid surfaces or contact formulations other than the finite-sliding, node-to-surface contact formulation. This argument is used only whe&#x6E;_&#x69;ContactType=0_.

### `iFrictionType` @type(Integer) @default(0)

- The friction characteristics type. This argument is used only whe&#x6E;_&#x69;ContactType=0_.
  - 0: None
  - 1: General
  - 2: Lagrange
  - 3: Rough
  - 4: Static & Kinetic

### `dFrictionCoeff1` @type(Double) @default(0.0)

- The first friction coefficient to be defined in terms of slip rate. This argument is used only whe&#x6E;_&#x69;FrictionType=&#x31;_&#x6F;&#x72;_&#x69;FrictionType=2_.

### `dFrictionCoeff2` @type(Double) @default(0.0)

- The second friction coefficient to be defined in terms of slip rate. This argument is used only whe&#x6E;_&#x69;FrictionType=&#x31;_&#x6F;&#x72;_&#x69;FrictionType=2_.

### `dShearStressLimit` @type(Double) @default(0.0)

- An optional equivalent shear stress limit, so that regardless of the magnitude of the contact pressure stress, sliding will occur if the magnitude of the equivalent shear stress reaches this value. A value of zero is not allowed. This argument is used only whe&#x6E;_&#x69;FrictionType=&#x31;_&#x6F;&#x72;_&#x69;FrictionType=2_.

### `dSlipTolerance` @type(Double) @default(0.0)

- The maximum allowable elastic slip for surface dimension ratio. This argument is used only whe&#x6E;_&#x69;FrictionType=&#x31;_&#x6F;&#x72;_&#x69;FrictionType=4_.

### `dStaticFrictionCoeff` @type(Double) @default(0.0)

- The static friction coefficient. This argument is used only whe&#x6E;_&#x69;FrictionType=4_.

### `dKineticFrictionCoeff` @type(Double) @default(0.0)

- The dynamic friction coefficient. This argument is used only whe&#x6E;_&#x69;FrictionType=4_.

### `dDecayCoeff` @type(Double) @default(0.0)

- The decay coefficient. This argument is used only whe&#x6E;_&#x69;FrictionType=4_.

### `bAdjustPosition` @type(Integer) @default(False)

- Whether to adjust the position of surfaces in the contact pair. This argument is used only whe&#x6E;_&#x69;ContactType=1_.

### `dPositionTolerance` @type(Double) @default(0.0)

- The tolerance of position of surfaces used for adjustment. This argument is used only whe&#x6E;_&#x62;AdjustPosition=1_.

### `iFormulationType` @type(Integer) @default(0)

- How Abaqus generates the contact constraint coefficients.  This argument is used only whe&#x6E;_&#x69;ContactType=0_.
  - 0: Node to Surface
  - 1: Surface to Surface

### `iTied` @type(Integer) @default(0)

- Whether the surfaces in the contact pair are to be tied together for the duration of the analysis. This argument is used only whe&#x6E;_&#x69;ContactType=0_.
  - 0: Not specified - Not want to tie the surfaces together.
  - 1: ON - Tie the surfaces together.

### `iPressureOverclosureType` @type(Integer) @default(0)

- A contact pressure-overclosure relationship.
  - 0: Hard Contact - Pressure-overclosure relationship without physical softening.
  - 1: Exponential - Exponential pressure-overclosure relationship.
  - 2: Linear - Linear pressure-overclosure relationship.
  - 3: Tabular - Piecewise linear pressure-overclosure relationship in tabular form.
  - 4: None

### `bAllowSeparation` @type(Integer) @default(False)

- Whether to allow separation of the two surfaces once contact has been established. This argument is used whe&#x6E;_&#x69;PressureOverclosureType=0_.

### `dContactStiffness` @type(Double) @default(0.0)

- The slope of the pressure-overclosure curve. This value must be positive and is required whe&#x6E;_&#x69;PressureOverclosureType=2_.

### `tshPressureOverclosure` @type(Table Sheet) @default(\[])

- The tabular data of Pressure-Overclosure used for exponential pressure-overclosure relationship. This argument must be specified whe&#x6E;_&#x69;PressureOverclosureType=&#x31;_&#x6F;&#x72;_&#x69;PressureOverclosureType=3_.

### `iThermalConductanceDef` @type(Integer) @default(0)

- The contact characteristic definition method of heat conduction.
  - 0: None
  - 1: Clearance Dependency
  - 2: Pressure Dependency
  - 3: Clearance & Pressure Dependency

### `bClearanceTemperatureDependency` @type(Boolean) @default(False)

- Whether the tabular data have Temperature-Dependent property.

### `iClearanceDependencies` @type(Integer) @default(0)

- The number of field variables in the data table. This argument must be specified whe&#x6E;_&#x69;ThermalConductanceDef=&#x31;_&#x6F;&#x72;_&#x69;ThermalConductanceDef=3_.

### `tshClearanceData` @type(Table Sheet) @default(\[])

- The tabular data of clearance dependency.

### `bPressureTemperatureDependency` @type(Boolean) @default(False)

- Enable/disable using temperature dependency data.

### `iPressureDependencies` @type(Integer) @default(0)

- Number of the field variables.

### `tshPressureData` @type(Table Sheet) @default(\[])

- The table of pressure dependency.

### `crplTargets` @type(List\[Pair of Cursor]) @default(\[])

- The list or pair of group master face and group slave face. Th&#x65;_&#x63;rplTarget&#x73;_&#x61;n&#x64;_&#x63;rContactAbaqu&#x73;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `crContactAbaqus` @type(Cursor) @default(None)

- An existing Abaqus Contact (Manual Group). If this parameter is used, the specified contact settings will be modified. Otherwise, a new contact settings will be created. Th&#x65;_&#x63;rplTarget&#x73;_&#x61;n&#x64;_&#x63;rContactAbaqu&#x73;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `iContactColor` @type(Integer) @default(0)

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus_1_Manual_Face_S", 
                        crlTargets=[Face(24)])

created_contact = Connections.Contacts.Abaqus.ManualGroup(strName="ContactAbaqus_1", 
                                                          dAdjustWidth=DFLT_DBL,
                                                          dExtensionZone=DFLT_DBL, 
                                                          dMaxPenetration=DFLT_DBL, 
                                                          iSmallSliding=1,
                                                          dSmoothAngle=DFLT_DBL,
                                                          iFrictionType=1, 
                                                          dFrictionCoeff1=DFLT_DBL, 
                                                          dFrictionCoeff2=DFLT_DBL, 
                                                          dShearStressLimit=DFLT_DBL,
                                                          dSlipTolerance=DFLT_DBL, 
                                                          dStaticFrictionCoeff=DFLT_DBL, 
                                                          dKineticFrictionCoeff=DFLT_DBL,
                                                          dDecayCoeff=DFLT_DBL, 
                                                          bAdjustPosition=1, 
                                                          dPositionTolerance=DFLT_DBL, 
                                                          iFormulationType=1, 
                                                          iTied=1,
                                                          iPressureOverclosureType=1, 
                                                          dContactStiffness=DFLT_DBL, 
                                                          tshPressureOverclosure=[0, 
                                                                                  0],
                                                          iThermalConductanceDef=3, 
                                                          tshClearanceData=[1, 
                                                                            2, 
                                                                            DFLT_DBL, 
                                                                            DFLT_DBL],
                                                          tshPressureData=[1, 
                                                                          2, 
                                                                          DFLT_DBL, 
                                                                          DFLT_DBL], 
                                                          crplTargets=[CursorPair(Group(1), 
                                                                                  Group(2))],
                                                          iContactColor=16711680)

JPT.Debugger(created_contact)
```
