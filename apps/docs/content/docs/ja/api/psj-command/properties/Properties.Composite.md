---
title: "Properties.Composite()"
description: "Create 2D Composite Material Shell Property"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Composite"
---

## Description

Define a shell property of 2D composite material.

## Syntax

```psj
Properties.Composite(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the new property.
- The default value is "ComMatShell1".

<!-- @since:5.0.1 @optional -->
### iPropertyColor

- Specify the color of the new property.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iFT

- Specify the Failure Theory for composite materials:
  - 0: No Failure Theory is specified.
  - 1: The Hill theory.
  - 2: The Hoffman theory.
  - 3: The Tsai-Wu theory.
  - 4: The Maximum Strain theory.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dGE

- Specify the Structural Damping coefficient.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iLAM

- Specify the Laminate options:

  - 0: Not specified - All plies must be specified and all stiffness terms are developed.
  - 1: "SYM" - Only plies on one side of the laminate centerline are specified. The plies are numbered starting with 1 for the bottom ply. If the laminate contains an odd number of plies, then model the center ply as half the thickness of the actual center ply.
  - 2: "MEM" - All plies must be specified, but only membrane terms (MID1 on the derived PSHELL entry) are computed.
  - 3: "BEND" - All plies must be specified, but only bending terms (MID2 on the derived PSHELL entry) are computed.
  - 4: "SMEAR" - All plies must be specified, stacking sequence is ignored, MID1=MID2 on the derived PSHELL entry and MID3, MID4 and TS/T and 12I/T\*\*3 terms are set to zero.
  - 5: "SMCORE" - Face plies on one side of the laminate and the core are specified to define a laminate that is symmetric about the midplane of the core. The core is specified last. When calculating face sheet stiffness, stacking sequence of the face sheets is ignored.

- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crMaterial

- Specify the material will be applied for composite property.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### dNSM

- Specify the non-structural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iPID

- Specify the property identification number. This number must be unique with respect to all other property identification numbers.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dSB

- Specify the allowable shear stress of the bonding material (allowable interlaminar shear stress). Required if _iFT_ is also specified.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iSOUT

- Specify whether to control individual ply stress and strain print or punch output.

  - 0: Not specified - Not control individual ply stress and strain print or punch output
  - 1: NO - Not control individual ply stress and strain print or punch output
  - 2: YES - Control individual ply stress and strain print or punch output

- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTREF

- Specify the Reference temperature.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dZ0

- Specify the laminate offsets.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dZOFF

- Specify the amount of offset of the laminate.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the entities to be applied to the composite property.
- The _crlTargets_ and _crCompositeProperty_ arguments are mutually exclusive (one of them must be specified).
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crCompositeProperty

- Specify the existing Composite Property.
  - If this argument is not _None_, the specified Composite Property will be modified.
  - Otherwise, a new Composite Property will be created.
- The _crlTargets_ and _crCompositeProperty_ arguments are mutually exclusive (one of them must be specified).
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crLocalCS

- Specify the local coordinate system used to define the material axis of the element.
- It must be specified if the specified _iOrientationMethod_ is 1 (Coordinate System).
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iOrientationMethod

- Specify method to define the material axis of the element.
  - 0: Theta - Use the _dlOrientationVector_ value.
  - 1: Coordinate System - Use the coordinate system _crLocalCS_. The X-axis of the coordinate system is projected to the element plane.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dlOrientationVector

- Specify orientation angle of the longitudinal direction of each ply with the material axis of the element.
- It must be specified if the specified _iOrientationMethod_ is 0 (Theta).
- The default value is \[DFLT\_DBL, DFLT\_DBL, DFLT\_DBL].

## Return Code

A _Cursor_ specifying the newly created or the modified Composite Property.

## Sample Code

```psj {4-5}
Geometry.Part.Cube()
Properties.Material.Add("Structural _Steel", [Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS _MODULUS, 200000.0), (POISSONS _RATIO, 0.3)])])
Properties.Composite(strName="ComMatShell1", iPropertyColor=16131973, crMaterial=Material(1),
    iPID=1, crlTargets=[Face(26)])
```
