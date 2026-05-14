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

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name of the new property.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crMaterial`

- The material will be applied for cohesive property.

<!-- @since:5.0.1 @type:Integer @required -->
### `iResponse`

- The response characteristics.
  - 0: Traction Separation.
  - 1: Continuum.
  - 2: Gasket.

<!-- @since:5.0.1 @type:Boolean @required -->
### `bSpecifyThick`

- The initial thickness.
  - _False_: Geometry - Calculated from the coordinate values of the node.
  - _True_: Specified - Specified by user input.

<!-- @since:5.0.1 @type:Double @required -->
### `dInitialThick`

- The initial thickness value when bSpecifyThick is false.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The entities to be applied the composite property. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The existing cohesive property. If this argument is not _None_, the specified cohesive property will be modified. Otherwise, a new cohesive property will be created. The _crlTargets_ and _crEdit_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFLG`

- The Duplication checking option. This option is used only for reassigning cohesive property for the Part which already had cohesive property. The purpose is to let user can control the Duplication could be allowed when creating cohesive property for Part or Element.
  - -1: Disable check duplication option, creating cohesive property item without checking duplication in selected Part or Element. This option allow creating multi-duplicated cohesive property item for same part
  - 0: Enable check duplication option, the property will be assigned only to bodies that do not have the property assigned yet
  - 1: Enable check duplication option, the Part or element which is already existing cohesive property will be changed to new cohesive property

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iId`

- The property identification number. This number must be unique with respect to all other property identification numbers.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSolverType`

- The solver type.
  - 0: ABAQUS.
  - 1: ADVC.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iADVCResponseType`

- The ADVC response type.
  - 0: Continuum.
  - 1: Continuum2.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iADVCStackDir`

- The ADVC stack direction.
  - 0: blank.
  - 1: 0.
  - 2: 1.
  - 3: 2.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableADVCThickness`

- Whether or not enable ADVC thickness.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dADVCThickness`

- The ADVC thickness when enable ADVC thickness.

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
