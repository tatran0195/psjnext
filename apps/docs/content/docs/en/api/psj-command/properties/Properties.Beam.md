---
title: "Properties.Beam()"
description: "Apply beam property on the selected entities"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Beam"
---

## Description

Apply beam property on the selected entities.

## Syntax

```psj
Properties.Beam(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"BEAM1" -->
### `strName`

- The name of the new property.

<!-- @since:5.0.1 @type:Integer @optional -->
### `iPropertyColor`

- The color of the created property.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCrossSection`

- The cross-sectional in the library. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified. Two section types are listed as below:
  - _SectionGeneral()_: The general cross-sectional shape.
  - _SectionLibrary()_: The cross-sectional shape library of Nastran.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iShapeDataType`

- The shape data type.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMaterial`

- The material will be applied for Beam.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSectionArea`

- The area of beam cross-section. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0,0,0] -->
### `dlSectionOrientation`

- The orientation of beam cross-section.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0,0,0] -->
### `dlInertiaMoment`

- The three components area moments of inertia, expressed in the principal axis of the BEAM. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTorsionalConst`

- The torsion constant which is involved in the relationship between angle of twist and applied torque along the axis of the beam. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSM`

- The nonstructural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSMA`

- The nonstructural mass per unit length at end A. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSMB`

- The nonstructural mass per unit length at end B. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSMNode1`

- The y-coordinate of center of gravity of nonstructural mass for end A. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSMNode2`

- The z-coordinate of center of gravity of nonstructural mass for end A. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSMNode3`

- The y-coordinate of center of gravity of nonstructural mass for end B. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNSMNode4`

- The z-coordinate of center of gravity of nonstructural mass for end B. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dShearStiffnessFactorK1`

- The area factors for shear for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dShearStiffnessFactorK2`

- The area factors for shear for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dShearAreaReliefS1`

- The shear relief coefficient due to taper for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dShearAreaReliefS2`

- The shear relief coefficient due to taper for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dWrapCoeff1`

- The warping coefficient for end A. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dWrapCoeff2`

- The warping coefficient for end B. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNA1`

- The y-coordinate of neutral axis for end A. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNA2`

- The z-coordinate of neutral axis for end A. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNA3`

- The y-coordinate of neutral axis for end B. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dNA4`

- The z-coordinate of neutral axis for end B. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressRecoveryCoeffCy`

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressRecoveryCoeffCz`

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressRecoveryCoeffDy`

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressRecoveryCoeffDz`

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressRecoveryCoeffEy`

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressRecoveryCoeffEz`

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressRecoveryCoeffFy`

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dStressRecoveryCoeffFz`

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinA1`

- Whether to remove the connection between the grid point and the translation UX of the BEAM at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinA2`

- Whether to remove the connection between the grid point and the translation UY of the BEAM at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinA3`

- Whether to remove the connection between the grid point and the translation UZ of the BEAM at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinA4`

- Whether to remove the connection between the grid point and the rotation RX of the BEAM at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinA5`

- Whether to remove the connection between the grid point and the rotation RY of the BEAM at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinA6`

- Whether to remove the connection between the grid point and the rotation RZ of the BEAM at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinB1`

- Whether to remove the connection between the grid point and the translation UX of the BEAM at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinB2`

- Whether to remove the connection between the grid point and the translation UY of the BEAM at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinB3`

- Whether to remove the connection between the grid point and the translation UZ of the BEAM at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinB4`

- Whether to remove the connection between the grid point and the rotation RX of the BEAM at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinB5`

- Whether to remove the connection between the grid point and the rotation RY of the BEAM at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bPinB6`

- Whether to remove the connection between the grid point and the rotation RZ of the BEAM at end B.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[DFLT _DBL,DFLT _DBL,DFLT _DBL] -->
### `dlOffsetA`

- The offset vector of end point A.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[DFLT _DBL,DFLT _DBL,DFLT _DBL] -->
### `dlOffsetB`

- The offset vector of end point B.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLengthUnit`

- The local unit as the units of length measurement. Possible values are 0, 1, 2, 3 and 4 that correspond to _mm_, _m_, _ft_, _in_, and _cm_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMassUnit`

- The local unit as the units of mass measurement. Possible values are 0, 1 and 2 that correspond to _t_, _kg_, and _kgf\*s^2/mm_.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The entities to be applied the BEAM property. Possible targets are BEAM, Edge, 1D Element, and Node. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The existed Beam property to modify it. This option uses only for editing property purpose.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bTapped`

- Whether the cross-sectional performance should be changed with node position of the beam element.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapArea`

- The area of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double List @optional @default:[DFLT _DBL,DFLT _DBL,DFLT _DBL] -->
### `dlVecTapInertia`

- The three components area moments of inertia of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapTorConst`

- The torsional constant of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapNSM`

- The nonstructural mass per unit length of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapStressRecoveryCoeffCy`

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point C at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapStressRecoveryCoeffCz`

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point C at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapStressRecoveryCoeffDy`

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point D at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapStressRecoveryCoeffDz`

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point D at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapStressRecoveryCoeffEy`

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point E at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapStressRecoveryCoeffEz`

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point E at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapStressRecoveryCoeffFy`

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point F at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTapStressRecoveryCoeffFz`

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point F at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.

<!-- @since:5.0.1 @type:Integer @optional @default:DFLT _INT -->
### `iIntePtNum`

- The integration points of the Beam element.

## Return Code

A _Cursor_ specifying the created beam property.

## Sample Code

```psj
Geometry.Part.Cube()

Properties.Material.Add("Structural _Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]),
                         Elastic([(YOUNGS _MODULUS, 
                                   200000.0), 
                                  (POISSONS _RATIO, 
                                   0.3)])])

Properties.Section.AddGeneral(strName="Circle",
                              iSecGenType=2, 
                              dDsecGensizeT1=0.0002)

created _prop = Properties.Beam(strName="BEAM1",
                               iPropertyColor=3986571, 
                               crCrossSection=SectionGeneral(1), 
                               crMaterial=Material(1), 
                               dSectionArea=1.25664e-07, 
                               dlSectionOrientation=[1.0, 
                                                     0.0, 
                                                     0.0], 
                               dlInertiaMoment=[1.257e-15, 
                                                1.257e-15, 
                                                0.0], 
                               dTorsionalConst=2.513e-15, 
                               dShearStiffnessFactorK1=0.9, 
                               dShearStiffnessFactorK2=0.9, 
                               dStressRecoveryCoeffCy=0.0002, 
                               dStressRecoveryCoeffDz=0.0002, 
                               dStressRecoveryCoeffEy=-0.0002, 
                               dStressRecoveryCoeffFz=-0.0002, 
                               crlTargets=[Edge(18)])

JPT.Debugger(created _prop)
```
