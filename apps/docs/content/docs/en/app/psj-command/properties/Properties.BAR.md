---
title: "Properties.BAR()"
description: "Apply bar property on the selected entities"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > BAR"
macro_link: "[Property1DBar](../../macro/properties/Property1DBar)"
---

## Description

Apply bar property on the selected entities.

## Syntax

```psj
Properties.BAR(...)
```

## Inputs

### `strName` @type(String) @default("")

- The name of the new property.

### `iPropertyId` @type(Integer) @default(1)

- The identify number of the created property.

### `iPropertyColor` @type(Integer)

- The color of the created property.

### `crCrossSection` @type(Cursor) @default(None)

- The cross-sectional in the library. Th&#x65;_&#x63;rCrossSectio&#x6E;_&#x61;n&#x64;_&#x69;ShapeDataTyp&#x65;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `iShapeDataType` @type(Integer) @default(0)

- The shape type from the default list. Th&#x65;_&#x63;rCrossSectio&#x6E;_&#x61;n&#x64;_&#x69;ShapeDataTyp&#x65;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `crMaterial` @type(Cursor) @default(None)

- The material will be applied for Bar property.

### `dSectionArea` @type(Double) @default(DFLT\_DBL)

- The area of bar cross-section. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dlSectionOrientation` @type(List\[Double]) @required

- The orientation of bar cross-section.

### `dlInertiaMoment` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The three components area moments of inertia, expressed in the principal axis of the bar. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDatadTorConst` @type(Double) @default(DFLT\_DBL)

- The torsion constant which is involved in the relationship between angle of twist and applied torque along the axis of the bar. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDatadNSM` @type(Double) @default(DFLT\_DBL)

- The nonstructural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataShearAreaFactor0` @type(Double) @default(DFLT\_DBL)

- The area factor for shear for plane 1. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataShearAreaFactor1` @type(Double) @default(DFLT\_DBL)

- The the area factor for shear for plane 2. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataStressRecoveryCoeff0` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataStressRecoveryCoeff1` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataStressRecoveryCoeff2` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataStressRecoveryCoeff3` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataStressRecoveryCoeff4` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataStressRecoveryCoeff5` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataStressRecoveryCoeff6` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the y-coordinate in the BAR element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dDataStressRecoveryCoeff7` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the z-coordinate in the BAR element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `bDataPinA0` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UX of the bar at end A.

### `bDataPinA1` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UY of the bar at end A.

### `bDataPinA2` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UZ of the bar at end A.

### `bDataPinA3` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RX of the bar at end A.

### `bDataPinA4` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RY of the bar at end A.

### `bDataPinA5` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RZ of the bar at end A.

### `bDataPinB0` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UX of the bar at end B.

### `bDataPinB1` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UY of the bar at end B.

### `bDataPinB2` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UZ of the bar at end B.

### `bDataPinB3` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RX of the bar at end B.

### `bDataPinB4` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RY of the bar at end B.

### `bDataPinB5` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RZ of the bar at end B.

### `dlDataOffset0` @type(List\[Double]) @default(\[DFLT\_DBL, DFLT\_DBL, DFLT\_DBL])

- The offset vector of end point A.

### `dlDataOffset1` @type(List\[Double]) @default(\[DFLT\_DBL, DFLT\_DBL, DFLT\_DBL])

- The offset vector of end point B.

### `iLocalLengthUnit` @type(Integer) @default(0)

- The local unit as the units of length measurement. Possible values are 0, 1, 2, 3 and 4 that correspond t&#x6F;_&#x6D;m_,_m_,_ft_,_in_, an&#x64;_&#x63;m_.

### `iLocalMassUnit` @type(Integer) @default(0)

- The local unit as the units of mass measurement. Possible values are 0, 1 and 2 that correspond t&#x6F;_&#x74;_,_kg_, an&#x64;_&#x6B;gf\*s^2/mm_.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The entities to be applied the Bar property. Possible targets are Bar Part, Edge, and 1D Element. Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rEdi&#x74;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `crEdit` @type(Cursor) @default(None)

- The existing Bar property. If this argument is no&#x74;_&#x4E;one_, the specified Bar property will be modified. Otherwise, a new Bar property will be created. Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rEdi&#x74;_&#x61;rguments are mutually exclusive. One of them must be specified.

## Return Code

A _Cursor_ specifying the created bar property.

## Sample Code

```psj {16,17,18,19,20,21,22,23,24,25,26}
Geometry.Part.Cube()

Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]),
                         Elastic([(YOUNGS_MODULUS, 
                                   200000.0), 
                                  (POISSONS_RATIO, 
                                   0.3)])])

Properties.Section.AddGeneral(strName="Circle", 
                              iSecGenType=2, 
                              dDsecGensizeT1=0.0002)

created_prop = Properties.BAR(strName="BAR2", 
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

JPT.Debugger(created_prop)
```
