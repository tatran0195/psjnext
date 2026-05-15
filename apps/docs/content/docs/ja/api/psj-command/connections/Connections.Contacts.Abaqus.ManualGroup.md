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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the new Abaqus Contact name.
- The default value is "ContactAbaqus\_1".

<!-- @since:5.0.1 @optional -->
### iContactType

- Specify the behavior type of contact definition. The behavior type of contact definition is one of the following:
  - 0: General (Sliding Contact)
  - 1: Tied (Shell-Solid contact)
  - 2: All with self - Automatic contact detection
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iContactAlgorithm

- Specify the contact setting target entity.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.
  - 1: Node to Face - Contact between node and shell or solid element faces.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dAdjustWidth

- Specify a value to adjust the initial positions of the surfaces specified. This is required when the _iTied_ parameter is used with ON value. This argument is used only when _iContactType=0_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dExtensionZone

- Specify a value that is equal to a fraction of the end segment or facet edge length by which Abaqus extends the master surface to avoid numerical round-off errors associated with contact modeling. The value given must lie between 0.0 and 0.2. This parameter affects only node-to-surface contact. This argument is used only when _iContactType=0_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dMaxPenetration

- Specify the maximum distance by which a point on the slave surface must penetrate the master surface before Abaqus abandons the current increment and tries again with a smaller increment. This parameter does not apply to contact pairs that use the finite-sliding, surface-to-surface contact formulation. This argument is used only when _iContactType=0_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iSmallSliding

- Specify whether to use the small-sliding contact formulation. This parameter is not allowed with self-contact. This argument is used only when _iContactType=0_.
  - 0: OFF
  - 1: ON
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSmoothAngle

- Specify the degree of smoothing used for element-based master surfaces in the finite-sliding, node-to-surface contact formulation. The value given must lie between 0.0 and 0.5. This parameter does not affect contact pairs with analytical rigid surfaces or contact formulations other than the finite-sliding, node-to-surface contact formulation. This argument is used only when _iContactType=0_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iFrictionType

- Specify the friction characteristics type. This argument is used only when _iContactType=0_.
  - 0: None
  - 1: General
  - 2: Lagrange
  - 3: Rough
  - 4: Static & Kinetic
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFrictionCoeff1

- Specify the first friction coefficient to be defined in terms of slip rate. This argument is used only when _iFrictionType=1_ or _iFrictionType=2_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dFrictionCoeff2

- Specify the second friction coefficient to be defined in terms of slip rate. This argument is used only when _iFrictionType=1_ or _iFrictionType=2_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dShearStressLimit

- Specify an optional equivalent shear stress limit, so that regardless of the magnitude of the contact pressure stress, sliding will occur if the magnitude of the equivalent shear stress reaches this value. A value of zero is not allowed. This argument is used only when _iFrictionType=1_ or _iFrictionType=2_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dSlipTolerance

- Specify the maximum allowable elastic slip for surface dimension ratio. This argument is used only when _iFrictionType=1_ or _iFrictionType=4_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStaticFrictionCoeff

- Specify the static friction coefficient. This argument is used only when _iFrictionType=4_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dKineticFrictionCoeff

- Specify the dynamic friction coefficient. This argument is used only when _iFrictionType=4_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dDecayCoeff

- Specify the decay coefficient. This argument is used only when _iFrictionType=4_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bAdjustPosition

- Specify whether to adjust the position of surfaces in the contact pair. This argument is used only when _iContactType=1_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dPositionTolerance

- Specify the tolerance of position of surfaces used for adjustment. This argument is used only when _bAdjustPosition=1_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iFormulationType

- Specify how Abaqus generates the contact constraint coefficients.  This argument is used only when _iContactType=0_.
  - 0: Node to Surface
  - 1: Surface to Surface
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iTied

- Specify whether the surfaces in the contact pair are to be tied together for the duration of the analysis. This argument is used only when _iContactType=0_.
  - 0: Not specified - Not want to tie the surfaces together.
  - 1: ON - Tie the surfaces together.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iPressureOverclosureType

- Specify a contact pressure-overclosure relationship.
  - 0: Hard Contact - Pressure-overclosure relationship without physical softening.
  - 1: Exponential - Exponential pressure-overclosure relationship.
  - 2: Linear - Linear pressure-overclosure relationship.
  - 3: Tabular - Piecewise linear pressure-overclosure relationship in tabular form.
  - 4: None
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bAllowSeparation

- Specify whether to allow separation of the two surfaces once contact has been established. This argument is used when _iPressureOverclosureType=0_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dContactStiffness

- Specify the slope of the pressure-overclosure curve. This value must be positive and is required when _iPressureOverclosureType=2_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### tshPressureOverclosure

- Specify the tabular data of Pressure-Overclosure used for exponential pressure-overclosure relationship. This argument must be specified when _iPressureOverclosureType=1_ or _iPressureOverclosureType=3_.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iThermalConductanceDef

- Specify the contact characteristic definition method of heat conduction.
  - 0: None
  - 1: Clearance Dependency
  - 2: Pressure Dependency
  - 3: Clearance & Pressure Dependency
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bClearanceTemperatureDependency

- Specify whether the tabular data have Temperature-Dependent property.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### iClearanceDependencies

- Specify the number of field variables in the data table. This argument must be specified when _iThermalConductanceDef=1_ or _iThermalConductanceDef=3_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshClearanceData

- Specify the tabular data of clearance dependency.
- The default value is \[].

### `bPressureTemperatureDependency`

- A _Boolean_ enable/disable using temperature dependency data.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### iPressureDependencies

- Specify number of the field variables.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### tshPressureData

- Specify the table of pressure dependency.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crplTargets

- Specify the list or pair of group master face and group slave face. The _crplTargets_ and _crContactAbaqus_ arguments are mutually exclusive. One of them must be specified.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crContactAbaqus

- Specify an existing Abaqus Contact (Manual Group). If this parameter is used, the specified contact settings will be modified. Otherwise, a new contact settings will be created. The _crplTargets_ and _crContactAbaqus_ arguments are mutually exclusive. One of them must be specified.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iContactColor

- Specify the contact color.
- The default value is 0.

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
