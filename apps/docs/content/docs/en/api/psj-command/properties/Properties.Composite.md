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

<!-- @since:5.0.1 @type:String @optional @default:"ComMatShell1" -->
### `strName`

- The name of the new property.

<!-- @since:5.0.1 @type:Integer @optional @default:"" -->
### `iPropertyColor`

- The color of the new property.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFT`

- The Failure Theory for composite materials:
  - 0: No Failure Theory is specified.
  - 1: The Hill theory.
  - 2: The Hoffman theory.
  - 3: The Tsai-Wu theory.
  - 4: The Maximum Strain theory.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dGE`

- The Structural Damping coefficient.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLAM`

- The Laminate options:

  - 0: Not specified - All plies must be specified and all stiffness terms are developed.
  - 1: "SYM" - Only plies on one side of the laminate centerline are specified. The plies are numbered starting with 1 for the bottom ply. If the laminate contains an odd number of plies, then model the center ply as half the thickness of the actual center ply.
  - 2: "MEM" - All plies must be specified, but only membrane terms (MID1 on the derived PSHELL entry) are computed.
  - 3: "BEND" - All plies must be specified, but only bending terms (MID2 on the derived PSHELL entry) are computed.
  - 4: "SMEAR" - All plies must be specified, stacking sequence is ignored, MID1=MID2 on the derived PSHELL entry and MID3, MID4 and TS/T and 12I/T\*\*3 terms are set to zero.
  - 5: "SMCORE" - Face plies on one side of the laminate and the core are specified to define a laminate that is symmetric about the midplane of the core. The core is specified last. When calculating face sheet stiffness, stacking sequence of the face sheets is ignored.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMaterial`

- The material will be applied for composite property.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSM`

- The non-structural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iPID`

- The property identification number. This number must be unique with respect to all other property identification numbers.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSB`

- The allowable shear stress of the bonding material (allowable interlaminar shear stress). Required if _iFT_ is also specified.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSOUT`

- Whether to control individual ply stress and strain print or punch output.

  - 0: Not specified - Not control individual ply stress and strain print or punch output
  - 1: NO - Not control individual ply stress and strain print or punch output
  - 2: YES - Control individual ply stress and strain print or punch output

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTREF`

- The Reference temperature.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dZ0`

- The laminate offsets.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dZOFF`

- The amount of offset of the laminate.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The entities to be applied to the composite property.
- The _crlTargets_ and _crCompositeProperty_ arguments are mutually exclusive (one of them must be specified).

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCompositeProperty`

- The existing Composite Property.
  - If this argument is not _None_, the specified Composite Property will be modified.
  - Otherwise, a new Composite Property will be created.
- The _crlTargets_ and _crCompositeProperty_ arguments are mutually exclusive (one of them must be specified).

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCS`

- The local coordinate system used to define the material axis of the element.
- It must be specified if the specified _iOrientationMethod_ is 1 (Coordinate System).

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOrientationMethod`

- The method to define the material axis of the element.
  - 0: Theta - Use the _dlOrientationVector_ value.
  - 1: Coordinate System - Use the coordinate system _crLocalCS_. The X-axis of the coordinate system is projected to the element plane.

<!-- @since:5.0.1 @type:Vector @optional @default:[DFLT _DBL, DFLT _DBL, DFLT _DBL] -->
### `dlOrientationVector`

- The orientation angle of the longitudinal direction of each ply with the material axis of the element.
- It must be specified if the specified _iOrientationMethod_ is 0 (Theta).

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
