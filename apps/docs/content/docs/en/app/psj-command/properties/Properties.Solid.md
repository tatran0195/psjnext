---
title: "Properties.Solid()"
description: "Apply Solid property on the selected entities"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Solid"
macro_link: "[Property3DSolid](../../macro/properties/Property3DSolid)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Apply Solid property on the selected entities.

## Syntax

```psj
Properties.Solid(...)
```

## Inputs

### `strName` @type(String) @default("Solid Property")

- The property name.

### `iPID` @type(Integer) @default(1)

- The property identification number (ID number).

### `crMaterial` @type(Cursor) @default(None)

- The pre-defined material in the User's Database library for the solid property.

### `iCordM` @type(Integer) @default(0)

- The material Coordinate System(CS). In case of there is a user's Coordinate System existed in model and user want to assign that CS, the value will be taken by local CS's ID number.
  - I&#x66;_&#x69;CordM=-2_: None of Coordinate System
  - I&#x66;_&#x69;CordM=-1_: Element Coordinate System
  - I&#x66;_&#x69;CordM=0_: Global Coordinate System
  - I&#x66;_&#x69;CordM=ID_: User's Coordinate System by using ID

### `iIN` @type(Integer) @default(0)

- The Integration Network (NASTRAN solver).
  - I&#x66;_&#x69;IN=0_: Disable Integration network
  - I&#x66;_&#x69;IN=1_: Using the Quadratic function
  - I&#x66;_&#x69;IN=2_: Using the Cubic function
  - I&#x66;_&#x69;IN=3_: Using the BUBBLE function

### `iOutLoc` @type(Integer) @default(0)

- The Stress output position (NASTRAN solver).
  - I&#x66;_&#x69;OutLoc=0_: Disable output location
  - I&#x66;_&#x69;OutLoc=1_: Using Stress of a Gaussian Point
  - I&#x66;_&#x69;OutLoc=2_: Using Stress at the node

### `iISOP` @type(Integer) @default(0)

- The Integration Schema method (NASTRAN solver).
  - I&#x66;_&#x69;ISOP=0_: Disable Integration method
  - I&#x66;_&#x69;ISOP=1_: Using the reduced Shear Integration Schema method
  - I&#x66;_&#x69;ISOP=2_: Using the standard Iso-parametric Integration Schema method

### `iFLflag` @type(Integer) @default(0)

- The Fluid element flag (NASTRAN solver).
  - I&#x66;_&#x69;FLflag=0_: Disable Fluid element
  - I&#x66;_&#x69;FLflag=1_: Using a Fluid element
  - I&#x66;_&#x69;FLflag=2_: Using the Structural element

### `iModifiedElem` @type(Integer) @default(0)

- A bitmask-type flag used to switch the modified element type (ABAQUS solver). Based on the specified value, the element formulation and handling within the mesh are switched.
  - I&#x66;_&#x69;ModifiedElem=0_: Don't use any Modified element (binary 000000)
  - I&#x66;_&#x69;ModifiedElem=1_: Using the Hybrid element (binary 000001)
  - I&#x66;_&#x69;ModifiedElem=2_: Using the Non-conforming element (binary 000010)
  - I&#x66;_&#x69;ModifiedElem=4_: Using the Modified element (binary 000100)
  - I&#x66;_&#x69;ModifiedElem=8_: Using the Degenerate Integral element (binary 001000)
  - I&#x66;_&#x69;ModifiedElem=16_: Using the element for Thermal Structural coupling analysis (binary 010000)
  - I&#x66;_&#x69;ModifiedElem=32_: Using the Acoustic elements (binary 100000)

### `iModifiedElemADVC` @type(Integer) @default(0)

- A bitmask-type flag used to switch the modified element type (ADVC solver). Based on the specified value, the element formulation and handling within the mesh are switched.
  - I&#x66;_&#x69;ModifiedElemADVC=0_: Don't use any Modified element (binary 000000)
  - I&#x66;_&#x69;ModifiedElemADVC=2_: Using the Non-conforming element (binary 000010)
  - I&#x66;_&#x69;ModifiedElemADVC=4_: Using the Modified element (binary 000100)
  - I&#x66;_&#x69;ModifiedElemADVC=8_: Using the Degenerate Integral element (binary 001000)
  - I&#x66;_&#x69;ModifiedElemADVC=256_: Using the First-order solid element (binary 100000000)
  - I&#x66;_&#x69;ModifiedElemADVC=512_: Using the Incompatible solid element (binary 1000000000)
  - I&#x66;_&#x69;ModifiedElemADVC=1024_: Using the u-p formulation solid element (binary 10000000000)

### `bHasDynaRemesh` @type(Boolean) @default(False)

- Enable/disable the configuration setting related to LS-Dyna (LS-Dyna Solver).

### `dDynaRemeshVal1` @type(Double) @default(0.0)

- The minimum edge length when the LS-Dyna configuration setting is set a&#x73;_&#x54;rue_.

### `dDynaRemeshVal2` @type(Double) @default(0.0)

- The maximum edge length when the LS-Dyna configuration setting is set a&#x73;_&#x54;rue_.

### `iAbaqusPropHGtype` @type(Integer) @default(0)

- The ABAQUS property Hourglass Control type for element.
  - I&#x66;_&#x69;AbaqusPropHGtype=0_: Using Default settings
  - I&#x66;_&#x69;AbaqusPropHGtype=1_: Using the Enhanced setting
  - I&#x66;_&#x69;AbaqusPropHGtype=2_: Using the Stiffness setting

### `dDispHG` @type(Double) @default(0.0)

- The displacement hourglass scaling factor. This will become required input when Hourglass Control type is stiffness setting.

### `crlTargets` @type(List\[Cursor]) @required

- The list of Solid target (Part, Solid Element) will be added property.

### `crEdit` @type(Cursor) @default(None)

- An existing Solid property setting item. If this parameter is used, the specified Solid property setting item will be modified. If it is lef&#x74;_&#x4E;one_, a new Solid property setting item will be created.

### `iFLG` @type(Integer) @default(0)

- The Duplication checking option. This option is used only for reassigning Solid property for the Part which already had Solid property. The purpose is to let user can control the Duplication could be allowed when creating Solid property for Part or Solid Element.
  - I&#x66;_&#x69;FLG=-1_: Disable check duplication option, creating Solid property item without checking duplication in selected Part or Solid Element. This option allow creating multi-duplicated Solid property item for same part
  - I&#x66;_&#x69;FLG=0_: Enable check duplication option, the property will be assigned only to bodies that do not have the property assigned yet
  - I&#x66;_&#x69;FLG=1_: Enable check duplication option, the Part or Solid element which is already existing Solid property will be changed to new Solid property

## Return Code

A _Cursor_ specifying the created solid property.

## Sample Code

```psj {21,22,23,24,25,26}
Geometry.Part.Cube()
Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]),
                         Elastic([(YOUNGS_MODULUS, 
                                   200000.0), 
                                  (POISSONS_RATIO, 
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

created_prop =  Properties.Solid(strName="Solid Property 1", 
                                 crMaterial=Material(1), 
                                 iCordM=-2, 
                                 dDispHG=DFLT_DBL, 
                                 crlTargets=[Part(1)], 
                                 iFLG=-1)

JPT.Debugger(created_prop)
```
