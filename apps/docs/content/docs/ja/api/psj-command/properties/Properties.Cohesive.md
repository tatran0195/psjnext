---
title: "Properties.Cohesive()"
description: "Create the property 3d Cohesive for solid element"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Cohesive"
macro _link: "[Prop3DCohesive](../../macro/properties/Prop3DCohesive)"
---

## Description

Create the property 3d Cohesive for solid element.

## Syntax

```psj
Properties.Cohesive(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name of the new property.

<!-- @since:5.0.1 @required -->
### crMaterial

- Specify the material will be applied for cohesive property.

<!-- @since:5.0.1 @required -->
### iResponse

- Specify the response characteristics.
  - 0: Traction Separation.
  - 1: Continuum.
  - 2: Gasket.

<!-- @since:5.0.1 @required -->
### bSpecifyThick

- Specify the initial thickness.
  - _False_: Geometry - Calculated from the coordinate values of the node.
  - _True_: Specified - Specified by user input.

<!-- @since:5.0.1 @required -->
### dInitialThick

- Specify the initial thickness value when bSpecifyThick is false.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the entities to be applied the composite property. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the existing cohesive property. If this argument is not _None_, the specified cohesive property will be modified. Otherwise, a new cohesive property will be created. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iFLG

- Specify the Duplication checking option. This option is used only for reassigning cohesive property for the Part which already had cohesive property. The purpose is to let user can control the Duplication could be allowed when creating cohesive property for Part or Element.
  - -1: Disable check duplication option, creating cohesive property item without checking duplication in selected Part or Element. This option allow creating multi-duplicated cohesive property item for same part
  - 0: Enable check duplication option, the property will be assigned only to bodies that do not have the property assigned yet
  - 1: Enable check duplication option, the Part or element which is already existing cohesive property will be changed to new cohesive property
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iId

- Specify the property identification number. This number must be unique with respect to all other property identification numbers.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSolverType

- Specify the solver type.
  - 0: ABAQUS.
  - 1: ADVC.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iADVCResponseType

- Specify the ADVC response type.
  - 0: Continuum.
  - 1: Continuum2.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iADVCStackDir

- Specify the ADVC stack direction.
  - 0: blank.
  - 1: 0.
  - 2: 1.
  - 3: 2.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iEnableADVCThickness

- Specify whether or not enable ADVC thickness.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dADVCThickness

- Specify the ADVC thickness when enable ADVC thickness.
- The default value is DFLT\_DBL.

## Return Code

A _Cursor_ specifying the created cohesive property.

## Sample Code

```psj {21,22,23,24,25,26,27,28,29}
Geometry.Part.Cube()

Properties.Material.Add("Structural _Steel", 
                        [Density([(DENSITY, 
                                   7.85e-09)]), 
                        Elastic([(YOUNGS _MODULUS, 
                                  200000.0), 
                                 (POISSONS _RATIO, 
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

created _prop = Properties.Cohesive(strName="Cohensive Property 1", 
                                   iPropertyColor=13708224, 
                                   crMaterial=Material(1), 
                                   iResponse=0, 
                                   bSpecifyThick=False, 
                                   dInitialThick=DFLT _DBL, 
                                   crlTargets=[Part(1)], 
                                   iFLG=-1, 
                                   iId=2)

JPT.Debugger(created _prop)
```
