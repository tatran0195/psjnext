---
title: "Properties.Cohesive()"
description: "Create the property 3d Cohesive for solid element"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Cohesive"
macro_link: "[Prop3DCohesive](../../macro/properties/Prop3DCohesive)"
---

## Description

Create the property 3d Cohesive for solid element.

## Syntax

```psj
Properties.Cohesive(...)
```

## Inputs

### `strName` @type(String) @required

- The name of the new property.

### `crMaterial` @type(Cursor) @required

- The material will be applied for cohesive property.

### `iResponse` @type(Integer) @required

- The response characteristics.
  - 0: Traction Separation.
  - 1: Continuum.
  - 2: Gasket.

### `bSpecifyThick` @type(Boolean) @required

- The initial thickness.
  - _False_: Geometry - Calculated from the coordinate values of the node.
  - _True_: Specified - Specified by user input.

### `dInitialThick` @type(Double) @required

- The initial thickness value when bSpecifyThick is false.

### `crlTargets` @type(List\[Cursor]) @required

- The entities to be applied the composite property. Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rEdi&#x74;_&#x61;rguments are mutually exclusive. One of them must be specified

### `crEdit` @type(Cursor) @default(None)

- The existing cohesive property. If this argument is no&#x74;_&#x4E;one_, the specified cohesive property will be modified. Otherwise, a new cohesive property will be created. Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rEdi&#x74;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `iFLG` @type(Integer) @default(0)

- The Duplication checking option. This option is used only for reassigning cohesive property for the Part which already had cohesive property. The purpose is to let user can control the Duplication could be allowed when creating cohesive property for Part or Element.
  - -1: Disable check duplication option, creating cohesive property item without checking duplication in selected Part or Element. This option allow creating multi-duplicated cohesive property item for same part
  - 0: Enable check duplication option, the property will be assigned only to bodies that do not have the property assigned yet
  - 1: Enable check duplication option, the Part or element which is already existing cohesive property will be changed to new cohesive property

### `iId` @type(Integer) @default(0)

- The property identification number. This number must be unique with respect to all other property identification numbers.

### `iSolverType` @type(Integer) @default(0)

- The solver type.
  - 0: ABAQUS.
  - 1: ADVC.

### `iADVCResponseType` @type(Integer) @default(0)

- The ADVC response type.
  - 0: Continuum.
  - 1: Continuum2.

### `iADVCStackDir` @type(Integer) @default(0)

- The ADVC stack direction.
  - 0: blank.
  - 1: 0.
  - 2: 1.
  - 3: 2.

### `iEnableADVCThickness` @type(Integer) @default(0)

- Whether or not enable ADVC thickness.

### `dADVCThickness` @type(Double) @default(DFLT\_DBL)

- The ADVC thickness when enable ADVC thickness.

## Return Code

A _Cursor_ specifying the created cohesive property.

## Sample Code

```psj {21,22,23,24,25,26,27,28,29}
Geometry.Part.Cube()

Properties.Material.Add("Structural_Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]), 
                        Elastic([(YOUNGS_MODULUS, 
                                  200000.0), 
                                 (POISSONS_RATIO, 
                                  0.3)])])

Meshing.SolidMeshing(crlParts=[Part(1)], 
                     dGradingFactor=1.05, 
                     dStretchLimit=0.1, 
                     iSpeedVsQual=1, 
                     iRegion=1, 
                     bSafeMode=False, 
                     iParallel=16, 
                     bInternalMeshOnly=False, 
                     iPartColor=65280)

created_prop = Properties.Cohesive(strName="Cohensive Property 1", 
                                   iPropertyColor=13708224, 
                                   crMaterial=Material(1), 
                                   iResponse=0, 
                                   bSpecifyThick=False, 
                                   dInitialThick=DFLT_DBL, 
                                   crlTargets=[Part(1)], 
                                   iFLG=-1, 
                                   iId=2)

JPT.Debugger(created_prop)
```
