---
title: "Properties.BAR()"
description: "Apply bar property on the selected entities"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > BAR"
macro _link: "[Property1DBar](../../macro/properties/Property1DBar)"
---

## Description

Apply bar property on the selected entities.

## Syntax

```psj
Properties.BAR(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the new property.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### iPropertyId

- Specify the identify number of the created property.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iPropertyColor

- Specify the color of the created property.

<!-- @since:5.0.1 @optional -->
### crCrossSection

- Specify the cross-sectional in the library. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iShapeDataType

- Specify the shape type from the default list. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crMaterial

- Specify the material will be applied for Bar property.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### dSectionArea

- Specify the area of bar cross-section. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @required -->
### dlSectionOrientation

- Specify the orientation of bar cross-section.

<!-- @since:5.0.1 @optional -->
### dlInertiaMoment

- Specify the three components area moments of inertia, expressed in the principal axis of the bar. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### dDatadTorConst

- Specify the torsion constant which is involved in the relationship between angle of twist and applied torque along the axis of the bar. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDatadNSM

- Specify the nonstructural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataShearAreaFactor0

- Specify the area factor for shear for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataShearAreaFactor1

- Specify the the area factor for shear for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataStressRecoveryCoeff0

- Specify the stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataStressRecoveryCoeff1

- Specify the stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataStressRecoveryCoeff2

- Specify the stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataStressRecoveryCoeff3

- Specify the stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataStressRecoveryCoeff4

- Specify the stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataStressRecoveryCoeff5

- Specify the stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataStressRecoveryCoeff6

- Specify the stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dDataStressRecoveryCoeff7

- Specify the stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### bDataPinA0

- Specify whether to remove the connection between the grid point and the translation UX of the bar at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinA1

- Specify whether to remove the connection between the grid point and the translation UY of the bar at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinA2

- Specify whether to remove the connection between the grid point and the translation UZ of the bar at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinA3

- Specify whether to remove the connection between the grid point and the rotation RX of the bar at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinA4

- Specify whether to remove the connection between the grid point and the rotation RY of the bar at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinA5

- Specify whether to remove the connection between the grid point and the rotation RZ of the bar at end A.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinB0

- Specify whether to remove the connection between the grid point and the translation UX of the bar at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinB1

- Specify whether to remove the connection between the grid point and the translation UY of the bar at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinB2

- Specify whether to remove the connection between the grid point and the translation UZ of the bar at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinB3

- Specify whether to remove the connection between the grid point and the rotation RX of the bar at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinB4

- Specify whether to remove the connection between the grid point and the rotation RY of the bar at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bDataPinB5

- Specify whether to remove the connection between the grid point and the rotation RZ of the bar at end B.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dlDataOffset0

- Specify the offset vector of end point A.
- The default value is \[DFLT\_DBL, DFLT\_DBL, DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### dlDataOffset1

- Specify the offset vector of end point B.
- The default value is \[DFLT\_DBL, DFLT\_DBL, DFLT\_DBL].

<!-- @since:5.0.1 @optional -->
### iLocalLengthUnit

- Specify the local unit as the units of length measurement. Possible values are 0, 1, 2, 3 and 4 that correspond to _mm_, _m_, _ft_, _in_, and _cm_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iLocalMassUnit

- Specify the local unit as the units of mass measurement. Possible values are 0, 1 and 2 that correspond to _t_, _kg_, and _kgf\*s^2/mm_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the entities to be applied the Bar property. Possible targets are Bar Part, Edge, and 1D Element. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the existing Bar property. If this argument is not _None_, the specified Bar property will be modified. Otherwise, a new Bar property will be created. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created bar property.

## Sample Code

```psj {16,17,18,19,20,21,22,23,24,25,26}
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

created _prop = Properties.BAR(strName="BAR2", 
                              iPropertyId=2, 
                              iPropertyColor=15383527, 
                              crCrossSection=SectionGeneral(1), 
                              crMaterial=Material(1), 
                              dSectionArea=1.25664e-07, 
                              dlSectionOrientation=[1.0, 0.0, 0.0], 
                              dlInertiaMoment=[1.257e-15, 1.257e-15, 0.0], 
                              dTorionalConst=2.513e-15, 
                              dShearAreaFactorY=0.9, 
                              dShearAreaFactorZ=0.9, 
                              dStressRecoveryCoeffCy=0.0002, 
                              dStressRecoveryCoeffCz=0.0, 
                              dStressRecoveryCoeffDy=0.0, 
                              dStressRecoveryCoeffDz=0.0002, 
                              dStressRecoveryCoeffEy=-0.0002, 
                              dStressRecoveryCoeffEz=0.0, 
                              dStressRecoveryCoeffFy=0.0, 
                              dStressRecoveryCoeffFz=-0.0002, 
                              crlTargets=[Edge(19)])

JPT.Debugger(created _prop)
```
