---
title: "Properties.Beam()"
description: "Apply beam property on the selected entities"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Beam"
---

## Description

Apply beam property on the selected entities.

## Syntax

```psj
Properties.Beam(...)
```

## Inputs

### `strName` @type(String) @default("BEAM1")

- The name of the new property.

### `iPropertyColor` @type(Integer)

- The color of the created property.

### `crCrossSection` @type(Cursor) @default(None)

- The cross-sectional in the library. Th&#x65;_&#x63;rCrossSectio&#x6E;_&#x61;n&#x64;_&#x69;ShapeDataTyp&#x65;_&#x61;rguments are mutually exclusive. One of them must be specified. Two section types are listed as below:
  - _SectionGeneral()_: The general cross-sectional shape.
  - _SectionLibrary()_: The cross-sectional shape library of Nastran.

### `iShapeDataType` @type(Integer) @default(0)

- The shape data type.

### `crMaterial` @type(Cursor) @default(None)

- The material will be applied for Beam.

### `dSectionArea` @type(Double) @default(0.0)

- The area of beam cross-section. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dlSectionOrientation` @type(List\[Double]) @default(\[0,0,0])

- The orientation of beam cross-section.

### `dlInertiaMoment` @type(List\[Double]) @default(\[0,0,0])

- The three components area moments of inertia, expressed in the principal axis of the BEAM. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dTorsionalConst` @type(Double) @default(0.0)

- The torsion constant which is involved in the relationship between angle of twist and applied torque along the axis of the beam. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNSM` @type(Double) @default(DFLT\_DBL)

- The nonstructural mass per unit length which is a contribution to the model mass from features that have negligible structural stiffness. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNSMA` @type(Double) @default(DFLT\_DBL)

- The nonstructural mass per unit length at end A. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNSMB` @type(Double) @default(DFLT\_DBL)

- The nonstructural mass per unit length at end B. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNSMNode1` @type(Double) @default(DFLT\_DBL)

- Y-coordinate of center of gravity of nonstructural mass for end A. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNSMNode2` @type(Double) @default(DFLT\_DBL)

- Z-coordinate of center of gravity of nonstructural mass for end A. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNSMNode3` @type(Double) @default(DFLT\_DBL)

- Y-coordinate of center of gravity of nonstructural mass for end B. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNSMNode4` @type(Double) @default(DFLT\_DBL)

- Z-coordinate of center of gravity of nonstructural mass for end B. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dShearStiffnessFactorK1` @type(Double) @default(0.0)

- The area factors for shear for plane 1. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dShearStiffnessFactorK2` @type(Double) @default(0.0)

- The area factors for shear for plane 2. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dShearAreaReliefS1` @type(Double) @default(DFLT\_DBL)

- The shear relief coefficient due to taper for plane 1. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dShearAreaReliefS2` @type(Double) @default(DFLT\_DBL)

- The shear relief coefficient due to taper for plane 2. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dWrapCoeff1` @type(Double) @default(DFLT\_DBL)

- The warping coefficient for end A. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dWrapCoeff2` @type(Double) @default(DFLT\_DBL)

- The warping coefficient for end B. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNA1` @type(Double) @default(DFLT\_DBL)

- The y-coordinate of neutral axis for end A. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNA2` @type(Double) @default(DFLT\_DBL)

- The z-coordinate of neutral axis for end A. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNA3` @type(Double) @default(DFLT\_DBL)

- The y-coordinate of neutral axis for end B. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dNA4` @type(Double) @default(DFLT\_DBL)

- The z-coordinate of neutral axis for end B. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dStressRecoveryCoeffCy` @type(Double) @default(0.0)

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dStressRecoveryCoeffCz` @type(Double) @default(0.0)

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point C at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dStressRecoveryCoeffDy` @type(Double) @default(0.0)

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dStressRecoveryCoeffDz` @type(Double) @default(0.0)

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point D at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dStressRecoveryCoeffEy` @type(Double) @default(0.0)

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dStressRecoveryCoeffEz` @type(Double) @default(0.0)

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point E at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dStressRecoveryCoeffFy` @type(Double) @default(0.0)

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `dStressRecoveryCoeffFz` @type(Double) @default(0.0)

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point F at which stresses are computed. This argument must be specified when the general section is chosen fo&#x72;_&#x63;rCrossSection_.

### `bPinA1` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UX of the BEAM at end A.

### `bPinA2` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UY of the BEAM at end A.

### `bPinA3` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UZ of the BEAM at end A.

### `bPinA4` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RX of the BEAM at end A.

### `bPinA5` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RY of the BEAM at end A.

### `bPinA6` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RZ of the BEAM at end A.

### `bPinB1` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UX of the BEAM at end B.

### `bPinB2` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UY of the BEAM at end B.

### `bPinB3` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the translation UZ of the BEAM at end B.

### `bPinB4` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RX of the BEAM at end B.

### `bPinB5` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RY of the BEAM at end B.

### `bPinB6` @type(Boolean) @default(False)

- Whether to remove the connection between the grid point and the rotation RZ of the BEAM at end B.

### `dlOffsetA` @type(List\[Double]) @default(\[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL])

- The offset vector of end point A.

### `dlOffsetB` @type(List\[Double]) @default(\[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL])

- The offset vector of end point B.

### `iLengthUnit` @type(Integer) @default(0)

- The local unit as the units of length measurement. Possible values are 0, 1, 2, 3 and 4 that correspond t&#x6F;_&#x6D;m_,_m_,_ft_,_in_, an&#x64;_&#x63;m_.

### `iMassUnit` @type(Integer) @default(0)

- The local unit as the units of mass measurement. Possible values are 0, 1 and 2 that correspond t&#x6F;_&#x74;_,_kg_, an&#x64;_&#x6B;gf\*s^2/mm_.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The entities to be applied the BEAM property. Possible targets are BEAM, Edge, 1D Element, and Node. Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rEdi&#x74;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `crEdit` @type(Cursor) @default(None)

- The existed Beam property to modify it. This option uses only for editing property purpose.

### `bTapped` @type(Boolean) @default(False)

- Whether the cross-sectional performance should be changed with node position of the beam element.

### `dTapArea` @type(Double) @default(DFLT\_DBL)

- The area of tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dlVecTapInertia` @type(Double List) @default(\[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL])

- The three components area moments of inertia of tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapTorConst` @type(Double) @default(DFLT\_DBL)

- The torsional constant of tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapNSM` @type(Double) @default(DFLT\_DBL)

- The nonstructural mass per unit length of tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapStressRecoveryCoeffCy` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point C at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapStressRecoveryCoeffCz` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point C at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapStressRecoveryCoeffDy` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point D at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapStressRecoveryCoeffDz` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point D at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapStressRecoveryCoeffEy` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point E at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapStressRecoveryCoeffEz` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point E at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapStressRecoveryCoeffFy` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the y-coordinate in the BEAM element coordinate system of point F at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `dTapStressRecoveryCoeffFz` @type(Double) @default(DFLT\_DBL)

- The stress recovery coefficients at the z-coordinate in the BEAM element coordinate system of point F at which stresses are computed for tapered Beam. This argument must be specified when the general section is chosen fo&#x72;_&#x62;Tapped_.

### `iIntePtNum` @type(Integer) @default(DFLT\_INT)

- The integration points of the Beam element.

## Return Code

A _Cursor_ specifying the created beam property.

## Sample Code

```psj
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

created_prop = Properties.Beam(strName="BEAM1",
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

JPT.Debugger(created_prop)
```
