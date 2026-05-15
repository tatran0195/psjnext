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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the new property.
- The default value is "BEAM1".

<!-- @since:5.0.1 @optional -->
### iPropertyColor

- Specify the color of the created property.

<!-- @since:5.0.1 @optional -->
### crCrossSection

- Specify the cross-sectional in the library. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified. Two section types are listed as below:
  - _SectionGeneral()_: The general cross-sectional shape.
  - _SectionLibrary()_: The cross-sectional shape library of Nastran.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iShapeDataType

- Specify the shape data type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crMaterial

- Specify the material will be applied for Beam.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### dSectionArea

- Specify the area of beam cross-section. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dlSectionOrientation

- Specify the orientation of beam cross-section.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dlInertiaMoment

- Specify the three components area moments of inertia, expressed in the principal axis of the BEAM. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is \[0,0,0].

<!-- @since:5.0.1 @optional -->
### dTorsionalConst

- Specify the torsion constant which is involved in the relationship between angle of twist and applied torque along the axis of the beam. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dNSM

- Specify the nonstructural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNSMA

- Specify the nonstructural mass per unit length at end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNSMB

- Specify the nonstructural mass per unit length at end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNSMNode1

- Specify y-coordinate of center of gravity of nonstructural mass for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNSMNode2

- Specify z-coordinate of center of gravity of nonstructural mass for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNSMNode3

- Specify y-coordinate of center of gravity of nonstructural mass for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNSMNode4

- Specify z-coordinate of center of gravity of nonstructural mass for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dShearStiffnessFactorK1

- Specify the area factors for shear for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dShearStiffnessFactorK2

- Specify the area factors for shear for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dShearAreaReliefS1

- Specify the shear relief coefficient due to taper for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dShearAreaReliefS2

- Specify the shear relief coefficient due to taper for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dWrapCoeff1

- Specify the warping coefficient for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dWrapCoeff2

- Specify the warping coefficient for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNA1

- Specify the y-coordinate of neutral axis for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNA2

- Specify the z-coordinate of neutral axis for end A. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNA3

- Specify the y-coordinate of neutral axis for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dNA4

- Specify the z-coordinate of neutral axis for end B. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dStressRecoveryCoeffCy

- Specify the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStressRecoveryCoeffCz

- Specify the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStressRecoveryCoeffDy

- Specify the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStressRecoveryCoeffDz

- Specify the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStressRecoveryCoeffEy

- Specify the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStressRecoveryCoeffEz

- Specify the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStressRecoveryCoeffFy

- Specify the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dStressRecoveryCoeffFz

- Specify the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bPinA1

- Specify whether to remove the connection between the grid point and the translation UX of the BEAM at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinA2

- Specify whether to remove the connection between the grid point and the translation UY of the BEAM at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinA3

- Specify whether to remove the connection between the grid point and the translation UZ of the BEAM at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinA4

- Specify whether to remove the connection between the grid point and the rotation RX of the BEAM at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinA5

- Specify whether to remove the connection between the grid point and the rotation RY of the BEAM at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinA6

- Specify whether to remove the connection between the grid point and the rotation RZ of the BEAM at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinB1

- Specify whether to remove the connection between the grid point and the translation UX of the BEAM at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinB2

- Specify whether to remove the connection between the grid point and the translation UY of the BEAM at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinB3

- Specify whether to remove the connection between the grid point and the translation UZ of the BEAM at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinB4

- Specify whether to remove the connection between the grid point and the rotation RX of the BEAM at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinB5

- Specify whether to remove the connection between the grid point and the rotation RY of the BEAM at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bPinB6

- Specify whether to remove the connection between the grid point and the rotation RZ of the BEAM at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dlOffsetA

- Specify the offset vector of end point A.
- The default value is \[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### dlOffsetB

- Specify the offset vector of end point B.
- The default value is \[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### iLengthUnit

- Specify the local unit as the units of length measurement. Possible values are 0, 1, 2, 3 and 4 that correspond to _mm_, _m_, _ft_, _in_, and _cm_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMassUnit

- Specify the local unit as the units of mass measurement. Possible values are 0, 1 and 2 that correspond to _t_, _kg_, and _kgf\*s^2/mm_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the entities to be applied the BEAM property. Possible targets are BEAM, Edge, 1D Element, and Node. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the existed Beam property to modify it. This option uses only for editing property purpose.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### bTapped

- Specify whether the cross-sectional performance should be changed with node position of the beam element.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dTapArea

- Specify the area of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dlVecTapInertia

- Specify the three components area moments of inertia of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is \[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### dTapTorConst

- Specify the torsional constant of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapNSM

- Specify the nonstructural mass per unit length of tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapStressRecoveryCoeffCy

- Specify the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point C at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapStressRecoveryCoeffCz

- Specify the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point C at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapStressRecoveryCoeffDy

- Specify the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point D at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapStressRecoveryCoeffDz

- Specify the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point D at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapStressRecoveryCoeffEy

- Specify the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point E at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapStressRecoveryCoeffEz

- Specify the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point E at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapStressRecoveryCoeffFy

- Specify the stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point F at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dTapStressRecoveryCoeffFz

- Specify the stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point F at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen for _bTapped_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iIntePtNum

- Specify the integration points of the Beam element.
- The default value is DFLT\_INT.

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
