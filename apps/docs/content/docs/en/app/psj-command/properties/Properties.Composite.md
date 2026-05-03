---
title: "Properties.Composite()"
description: "Create 2D Composite Material Shell Property"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Composite"
---

## Description

Define a shell property of 2D composite material.

## Syntax

```psj
Properties.Composite(...)
```

## Inputs

### `strName` @type(String) @default("ComMatShell1")

- The name of the new property.

### `iPropertyColor` @type(Integer) @default("")

- The color of the new property.

### `iFT` @type(Integer) @default(0)

- The Failure Theory for composite materials:
  - 0: No Failure Theory is specified.
  - 1: The Hill theory.
  - 2: The Hoffman theory.
  - 3: The Tsai-Wu theory.
  - 4: The Maximum Strain theory.

### `dGE` @type(Double) @default(DFLT\_DBL)

- The Structural Damping coefficient.

### `iLAM` @type(Integer) @default(0)

- The Laminate options:

  - 0: Not specified - All plies must be specified and all stiffness terms are developed.
  - 1: "SYM" - Only plies on one side of the laminate centerline are specified. The plies are numbered starting with 1 for the bottom ply. If the laminate contains an odd number of plies, then model the center ply as half the thickness of the actual center ply.
  - 2: "MEM" - All plies must be specified, but only membrane terms (MID1 on the derived PSHELL entry) are computed.
  - 3: "BEND" - All plies must be specified, but only bending terms (MID2 on the derived PSHELL entry) are computed.
  - 4: "SMEAR" - All plies must be specified, stacking sequence is ignored, MID1=MID2 on the derived PSHELL entry and MID3, MID4 and TS/T and 12I/T\*\*3 terms are set to zero.
  - 5: "SMCORE" - Face plies on one side of the laminate and the core are specified to define a laminate that is symmetric about the midplane of the core. The core is specified last. When calculating face sheet stiffness, stacking sequence of the face sheets is ignored.

### `crMaterial` @type(Cursor) @default(None)

- The material will be applied for composite property.

### `dNSM` @type(Double) @default(DFLT\_DBL)

- The non-structural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness.

### `iPID` @type(Integer) @default(0)

- The property identification number. This number must be unique with respect to all other property identification numbers.

### `dSB` @type(Double) @default(DFLT\_DBL)

- The allowable shear stress of the bonding material (allowable interlaminar shear stress). Required i&#x66;_&#x69;F&#x54;_&#x69;s also specified.

### `iSOUT` @type(Integer) @default(0)

- Whether to control individual ply stress and strain print or punch output.

  - 0: Not specified - Not control individual ply stress and strain print or punch output
  - 1: NO - Not control individual ply stress and strain print or punch output
  - 2: YES - Control individual ply stress and strain print or punch output

### `dTREF` @type(Double) @default(DFLT\_DBL)

- The Reference temperature.

### `dZ0` @type(Double) @default(DFLT\_DBL)

- The laminate offsets.

### `dZOFF` @type(Double) @default(DFLT\_DBL)

- The amount of offset of the laminate.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The entities to be applied to the composite property.
- Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rCompositePropert&#x79;_&#x61;rguments are mutually exclusive (one of them must be specified).

### `crCompositeProperty` @type(Cursor) @default(None)

- The existing Composite Property.
  - If this argument is no&#x74;_&#x4E;one_, the specified Composite Property will be modified.
  - Otherwise, a new Composite Property will be created.
- Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rCompositePropert&#x79;_&#x61;rguments are mutually exclusive (one of them must be specified).

### `crLocalCS` @type(Cursor) @default(None)

- The local coordinate system used to define the material axis of the element.
- It must be specified if the specifie&#x64;_&#x69;OrientationMetho&#x64;_&#x69;s 1 (Coordinate System).

### `iOrientationMethod` @type(Integer) @default(0)

- Method to define the material axis of the element.
  - 0: Theta - Use th&#x65;_&#x64;lOrientationVecto&#x72;_&#x76;alue.
  - 1: Coordinate System - Use the coordinate syste&#x6D;_&#x63;rLocalCS_. The X-axis of the coordinate system is projected to the element plane.

### `dlOrientationVector` @type(Vector) @default(\[DFLT\_DBL, DFLT\_DBL, DFLT\_DBL])

- Orientation angle of the longitudinal direction of each ply with the material axis of the element.
- It must be specified if the specifie&#x64;_&#x69;OrientationMetho&#x64;_&#x69;s 0 (Theta).

## Return Code

A _Cursor_ specifying the newly created or the modified Composite Property.

## Sample Code

```psj {4-5}
Geometry.Part.Cube()
Properties.Material.Add("Structural_Steel", [Density([(DENSITY, 7.85e-09)]),
    Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])
Properties.Composite(strName="ComMatShell1", iPropertyColor=16131973, crMaterial=Material(1),
    iPID=1, crlTargets=[Face(26)])
```
