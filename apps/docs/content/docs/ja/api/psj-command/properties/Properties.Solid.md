---
title: "Properties.Solid()"
description: "Apply Solid property on the selected entities"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Solid"
macro _link: "[Property3DSolid](../../macro/properties/Property3DSolid)"
---

## Description

Apply Solid property on the selected entities.

## Syntax

```psj
Properties.Solid(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the property name.
- The default value is "Solid Property".

<!-- @since:5.0.1 @optional -->
### iPID

- Specify the property identification number (ID number).
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crMaterial

- Specify the pre-defined material in the User's Database library for the solid property.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iCordM

- Specify the material Coordinate System(CS). In case of there is a user's Coordinate System existed in model and user want to assign that CS, the value will be taken by local CS's ID number.
  - If _iCordM=-2_: None of Coordinate System
  - If _iCordM=-1_: Element Coordinate System
  - If _iCordM=0_: Global Coordinate System
  - If _iCordM=ID_: User's Coordinate System by using ID
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iIN

- Specify the Integration Network (NASTRAN solver).
  - If _iIN=0_: Disable Integration network
  - If _iIN=1_: Using the Quadratic function
  - If _iIN=2_: Using the Cubic function
  - If _iIN=3_: Using the BUBBLE function
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOutLoc

- Specify the Stress output position (NASTRAN solver).
  - If _iOutLoc=0_: Disable output location
  - If _iOutLoc=1_: Using Stress of a Gaussian Point
  - If _iOutLoc=2_: Using Stress at the node
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iISOP

- Specify the Integration Schema method (NASTRAN solver).
  - If _iISOP=0_: Disable Integration method
  - If _iISOP=1_: Using the reduced Shear Integration Schema method
  - If _iISOP=2_: Using the standard Iso-parametric Integration Schema method
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iFLflag

- Specify the Fluid element flag (NASTRAN solver).
  - If _iFLflag=0_: Disable Fluid element
  - If _iFLflag=1_: Using a Fluid element
  - If _iFLflag=2_: Using the Structural element
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iModifiedElem

- Specify a bitmask-type flag used to switch the modified element type (ABAQUS solver). Based on the specified value, the element formulation and handling within the mesh are switched.
  - If _iModifiedElem=0_: Don't use any Modified element (binary 000000)
  - If _iModifiedElem=1_: Using the Hybrid element (binary 000001)
  - If _iModifiedElem=2_: Using the Non-conforming element (binary 000010)
  - If _iModifiedElem=4_: Using the Modified element (binary 000100)
  - If _iModifiedElem=8_: Using the Degenerate Integral element (binary 001000)
  - If _iModifiedElem=16_: Using the element for Thermal Structural coupling analysis (binary 010000)
  - If _iModifiedElem=32_: Using the Acoustic elements (binary 100000)
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iModifiedElemADVC

- Specify a bitmask-type flag used to switch the modified element type (ADVC solver). Based on the specified value, the element formulation and handling within the mesh are switched.
  - If _iModifiedElemADVC=0_: Don't use any Modified element (binary 000000)
  - If _iModifiedElemADVC=2_: Using the Non-conforming element (binary 000010)
  - If _iModifiedElemADVC=4_: Using the Modified element (binary 000100)
  - If _iModifiedElemADVC=8_: Using the Degenerate Integral element (binary 001000)
  - If _iModifiedElemADVC=256_: Using the First-order solid element (binary 100000000)
  - If _iModifiedElemADVC=512_: Using the Incompatible solid element (binary 1000000000)
  - If _iModifiedElemADVC=1024_: Using the u-p formulation solid element (binary 10000000000)
- The default value is 0.

### `bHasDynaRemesh`

- A _Boolean_ enable/disable the configuration setting related to LS-Dyna (LS-Dyna Solver).
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dDynaRemeshVal1

- Specify the minimum edge length when the LS-Dyna configuration setting is set as _True_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dDynaRemeshVal2

- Specify the maximum edge length when the LS-Dyna configuration setting is set as _True_.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iAbaqusPropHGtype

- Specify the ABAQUS property Hourglass Control type for element.
  - If _iAbaqusPropHGtype=0_: Using Default settings
  - If _iAbaqusPropHGtype=1_: Using the Enhanced setting
  - If _iAbaqusPropHGtype=2_: Using the Stiffness setting
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dDispHG

- Specify the displacement hourglass scaling factor. This will become required input when Hourglass Control type is stiffness setting.
- The default value is 0.0.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the list of Solid target (Part, Solid Element) will be added property.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Solid property setting item. If this parameter is used, the specified Solid property setting item will be modified. If it is left _None_, a new Solid property setting item will be created.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iFLG

- Specify the Duplication checking option. This option is used only for reassigning Solid property for the Part which already had Solid property. The purpose is to let user can control the Duplication could be allowed when creating Solid property for Part or Solid Element.
  - If _iFLG=-1_: Disable check duplication option, creating Solid property item without checking duplication in selected Part or Solid Element. This option allow creating multi-duplicated Solid property item for same part
  - If _iFLG=0_: Enable check duplication option, the property will be assigned only to bodies that do not have the property assigned yet
  - If _iFLG=1_: Enable check duplication option, the Part or Solid element which is already existing Solid property will be changed to new Solid property
- The default value is 0.

## Return Code

A _Cursor_ specifying the created solid property.

## Sample Code

```psj {21,22,23,24,25,26}
Geometry.Part.Cube()
Properties.Material.Add("Structural _Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]),
                         Elastic([(YOUNGS _MODULUS, 
                                   200000.0), 
                                  (POISSONS _RATIO, 
                                   0.3)])])

Meshing.SolidMeshing(crlParts=[Part(1)], 
                     bTet10=True, 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1, 
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=16, 
                     bInternalMeshOnly=False, 
                     iPartColor=65280)

created _prop =  Properties.Solid(strName="Solid Property 1", 
                                 crMaterial=Material(1), 
                                 iCordM=-2, 
                                 dDispHG=DFLT _DBL, 
                                 crlTargets=[Part(1)], 
                                 iFLG=-1)

JPT.Debugger(created _prop)
```
