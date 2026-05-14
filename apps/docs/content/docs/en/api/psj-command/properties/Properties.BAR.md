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

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name of the new property.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iPropertyId`

- The identify number of the created property.

<!-- @since:5.0.1 @type:Integer @optional -->
### `iPropertyColor`

- The color of the created property.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCrossSection`

- The cross-sectional in the library. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iShapeDataType`

- The shape type from the default list. The _crCrossSection_ and _iShapeDataType_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMaterial`

- The material will be applied for Bar property.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dSectionArea`

- The area of bar cross-section. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:List[Double] @required -->
### `dlSectionOrientation`

- The orientation of bar cross-section.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlInertiaMoment`

- The three components area moments of inertia, expressed in the principal axis of the bar. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDatadTorConst`

- The torsion constant which is involved in the relationship between angle of twist and applied torque along the axis of the bar. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDatadNSM`

- The nonstructural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataShearAreaFactor0`

- The area factor for shear for plane 1. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataShearAreaFactor1`

- The area factor for shear for plane 2. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataStressRecoveryCoeff0`

- The stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataStressRecoveryCoeff1`

- The stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataStressRecoveryCoeff2`

- The stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataStressRecoveryCoeff3`

- The stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataStressRecoveryCoeff4`

- The stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataStressRecoveryCoeff5`

- The stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataStressRecoveryCoeff6`

- The stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dDataStressRecoveryCoeff7`

- The stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen for _crCrossSection_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinA0`

- Whether to remove the connection between the grid point and the translation UX of the bar at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinA1`

- Whether to remove the connection between the grid point and the translation UY of the bar at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinA2`

- Whether to remove the connection between the grid point and the translation UZ of the bar at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinA3`

- Whether to remove the connection between the grid point and the rotation RX of the bar at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinA4`

- Whether to remove the connection between the grid point and the rotation RY of the bar at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinA5`

- Whether to remove the connection between the grid point and the rotation RZ of the bar at end A.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinB0`

- Whether to remove the connection between the grid point and the translation UX of the bar at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinB1`

- Whether to remove the connection between the grid point and the translation UY of the bar at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinB2`

- Whether to remove the connection between the grid point and the translation UZ of the bar at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinB3`

- Whether to remove the connection between the grid point and the rotation RX of the bar at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinB4`

- Whether to remove the connection between the grid point and the rotation RY of the bar at end B.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bDataPinB5`

- Whether to remove the connection between the grid point and the rotation RZ of the bar at end B.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[DFLT _DBL, DFLT _DBL, DFLT _DBL] -->
### `dlDataOffset0`

- The offset vector of end point A.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[DFLT _DBL, DFLT _DBL, DFLT _DBL] -->
### `dlDataOffset1`

- The offset vector of end point B.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalLengthUnit`

- The local unit as the units of length measurement. Possible values are 0, 1, 2, 3 and 4 that correspond to _mm_, _m_, _ft_, _in_, and _cm_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalMassUnit`

- The local unit as the units of mass measurement. Possible values are 0, 1 and 2 that correspond to _t_, _kg_, and _kgf\*s^2/mm_.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The entities to be applied the Bar property. Possible targets are Bar Part, Edge, and 1D Element. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The existing Bar property. If this argument is not _None_, the specified Bar property will be modified. Otherwise, a new Bar property will be created. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.

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
