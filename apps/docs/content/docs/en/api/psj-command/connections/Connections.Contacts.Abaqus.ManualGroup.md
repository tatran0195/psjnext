---
title: "Connections.Contacts.Abaqus.ManualGroup()"
description: "Define the contact set between the specified group for Abaqus. Create a group with master and slave surfaces beforehand to define the contact in the contact settings"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Abaqus > Manual Group"
---

## Description

Define the contact set between the specified group for Abaqus. Create a group with master and slave surfaces beforehand to define the contact in the contact settings.

## Syntax

```psj
Connections.Contacts.Abaqus.ManualGroup(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ContactAbaqus _1" -->
### `strName`

- The new Abaqus Contact name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactType`

- The behavior type of contact definition. The behavior type of contact definition is one of the following:
  - 0: General (Sliding Contact)
  - 1: Tied (Shell-Solid contact)
  - 2: All with self - Automatic contact detection

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactAlgorithm`

- The contact setting target entity.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.
  - 1: Node to Face - Contact between node and shell or solid element faces.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAdjustWidth`

- A value to adjust the initial positions of the surfaces specified. This is required when the _iTied_ parameter is used with ON value. This argument is used only when _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dExtensionZone`

- A value that is equal to a fraction of the end segment or facet edge length by which Abaqus extends the master surface to avoid numerical round-off errors associated with contact modeling. The value given must lie between 0.0 and 0.2. This parameter affects only node-to-surface contact. This argument is used only when _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMaxPenetration`

- The maximum distance by which a point on the slave surface must penetrate the master surface before Abaqus abandons the current increment and tries again with a smaller increment. This parameter does not apply to contact pairs that use the finite-sliding, surface-to-surface contact formulation. This argument is used only when _iContactType=0_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSmallSliding`

- Whether to use the small-sliding contact formulation. This parameter is not allowed with self-contact. This argument is used only when _iContactType=0_.
  - 0: OFF
  - 1: ON

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSmoothAngle`

- The degree of smoothing used for element-based master surfaces in the finite-sliding, node-to-surface contact formulation. The value given must lie between 0.0 and 0.5. This parameter does not affect contact pairs with analytical rigid surfaces or contact formulations other than the finite-sliding, node-to-surface contact formulation. This argument is used only when _iContactType=0_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFrictionType`

- The friction characteristics type. This argument is used only when _iContactType=0_.
  - 0: None
  - 1: General
  - 2: Lagrange
  - 3: Rough
  - 4: Static & Kinetic

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFrictionCoeff1`

- The first friction coefficient to be defined in terms of slip rate. This argument is used only when _iFrictionType=1_ or _iFrictionType=2_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dFrictionCoeff2`

- The second friction coefficient to be defined in terms of slip rate. This argument is used only when _iFrictionType=1_ or _iFrictionType=2_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dShearStressLimit`

- An optional equivalent shear stress limit, so that regardless of the magnitude of the contact pressure stress, sliding will occur if the magnitude of the equivalent shear stress reaches this value. A value of zero is not allowed. This argument is used only when _iFrictionType=1_ or _iFrictionType=2_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSlipTolerance`

- The maximum allowable elastic slip for surface dimension ratio. This argument is used only when _iFrictionType=1_ or _iFrictionType=4_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStaticFrictionCoeff`

- The static friction coefficient. This argument is used only when _iFrictionType=4_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dKineticFrictionCoeff`

- The dynamic friction coefficient. This argument is used only when _iFrictionType=4_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dDecayCoeff`

- The decay coefficient. This argument is used only when _iFrictionType=4_.

<!-- @since:5.0.1 @type:Integer @optional @default:False -->
### `bAdjustPosition`

- Whether to adjust the position of surfaces in the contact pair. This argument is used only when _iContactType=1_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dPositionTolerance`

- The tolerance of position of surfaces used for adjustment. This argument is used only when _bAdjustPosition=1_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFormulationType`

- The how Abaqus generates the contact constraint coefficients.  This argument is used only when _iContactType=0_.
  - 0: Node to Surface
  - 1: Surface to Surface

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iTied`

- Whether the surfaces in the contact pair are to be tied together for the duration of the analysis. This argument is used only when _iContactType=0_.
  - 0: Not specified - Not want to tie the surfaces together.
  - 1: ON - Tie the surfaces together.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPressureOverclosureType`

- A contact pressure-overclosure relationship.
  - 0: Hard Contact - Pressure-overclosure relationship without physical softening.
  - 1: Exponential - Exponential pressure-overclosure relationship.
  - 2: Linear - Linear pressure-overclosure relationship.
  - 3: Tabular - Piecewise linear pressure-overclosure relationship in tabular form.
  - 4: None

<!-- @since:5.0.1 @type:Integer @optional @default:False -->
### `bAllowSeparation`

- Whether to allow separation of the two surfaces once contact has been established. This argument is used when _iPressureOverclosureType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dContactStiffness`

- The slope of the pressure-overclosure curve. This value must be positive and is required when _iPressureOverclosureType=2_.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshPressureOverclosure`

- The tabular data of Pressure-Overclosure used for exponential pressure-overclosure relationship. This argument must be specified when _iPressureOverclosureType=1_ or _iPressureOverclosureType=3_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iThermalConductanceDef`

- The contact characteristic definition method of heat conduction.
  - 0: None
  - 1: Clearance Dependency
  - 2: Pressure Dependency
  - 3: Clearance & Pressure Dependency

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bClearanceTemperatureDependency`

- Whether the tabular data have Temperature-Dependent property.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iClearanceDependencies`

- The number of field variables in the data table. This argument must be specified when _iThermalConductanceDef=1_ or _iThermalConductanceDef=3_.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshClearanceData`

- The tabular data of clearance dependency.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPressureTemperatureDependency`

- The enable/disable using temperature dependency data.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPressureDependencies`

- The number of the field variables.

<!-- @since:5.0.1 @type:Table Sheet @optional @default:[] -->
### `tshPressureData`

- The table of pressure dependency.

<!-- @since:5.0.1 @type:List[Pair of Cursor] @optional @default:[] -->
### `crplTargets`

- The list or pair of group master face and group slave face. The _crplTargets_ and _crContactAbaqus_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crContactAbaqus`

- An existing Abaqus Contact (Manual Group). If this parameter is used, the specified contact settings will be modified. Otherwise, a new contact settings will be created. The _crplTargets_ and _crContactAbaqus_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactColor`

- The contact color.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _S", 
                        crlTargets=[Face(24)])

created _contact = Connections.Contacts.Abaqus.ManualGroup(strName="ContactAbaqus _1", 
                                                          dAdjustWidth=DFLT _DBL,
                                                          dExtensionZone=DFLT _DBL, 
                                                          dMaxPenetration=DFLT _DBL, 
                                                          iSmallSliding=1,
                                                          dSmoothAngle=DFLT _DBL,
                                                          iFrictionType=1, 
                                                          dFrictionCoeff1=DFLT _DBL, 
                                                          dFrictionCoeff2=DFLT _DBL, 
                                                          dShearStressLimit=DFLT _DBL,
                                                          dSlipTolerance=DFLT _DBL, 
                                                          dStaticFrictionCoeff=DFLT _DBL, 
                                                          dKineticFrictionCoeff=DFLT _DBL,
                                                          dDecayCoeff=DFLT _DBL, 
                                                          bAdjustPosition=1, 
                                                          dPositionTolerance=DFLT _DBL, 
                                                          iFormulationType=1, 
                                                          iTied=1,
                                                          iPressureOverclosureType=1, 
                                                          dContactStiffness=DFLT _DBL, 
                                                          tshPressureOverclosure=[0, 
                                                                                  0],
                                                          iThermalConductanceDef=3, 
                                                          tshClearanceData=[1, 
                                                                            2, 
                                                                            DFLT _DBL, 
                                                                            DFLT _DBL],
                                                          tshPressureData=[1, 
                                                                          2, 
                                                                          DFLT _DBL, 
                                                                          DFLT _DBL], 
                                                          crplTargets=[CursorPair(Group(1), 
                                                                                  Group(2))],
                                                          iContactColor=16711680)

JPT.Debugger(created _contact)
```
