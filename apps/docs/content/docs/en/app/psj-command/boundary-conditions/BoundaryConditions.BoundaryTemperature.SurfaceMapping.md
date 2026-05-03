---
title: "BoundaryConditions.BoundaryTemperature.SurfaceMapping()"
description: "Create surface mapping boundary temperature"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > BoundaryTemperature > SurfaceMapping"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create surface mapping boundary temperature.

## Syntax

```psj
BoundaryConditions.BoundaryTemperature.SurfaceMapping(...)
```

## Inputs

### `strName` @type(String) @default("MappingTemperature")

- The mapping temperature name.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The targets.

### `iMAPPos` @type(Integer) @default(0)

- The map position.
  - 0: MAP\_POS\_SURFACE\_NODE.
    - 1: MAP\_POS\_SOLID\_NODE.
    - 2: MAP\_POS\_SURFACE\_ELEM.
    - 3: MAP\_POS\_SOLID\_ELEM.

### `iViewCp` @type(Integer) @default(0)

- The component index that to be previewed.

### `iCp` @type(Integer) @default(1)

- The component.

### `iSrcType` @type(Integer) @default(0)

- The source type of the fluid analysis solver from which the result file was output.
  - 0: Fluent.
    - 1: Star CD.
    - 2: Convection Text.
    - 3: SZText.
    - 4: ADVC.
    - 5: SubmodelBC ADVC.

### `iMappedCpIndexArr0` @type(Integer) @default(0)

- The mapped component index arr0.

### `iMappedCpIndexArr1` @type(Integer) @default(0)

- The mapped component index arr1.

### `dScaleFactor` @type(Double) @default(1.0)

- The scale factor.

### `posOffset` @type(Position) @default(\[0,0,0])

- The offset.

### `posRotate` @type(Position) @default(\[0,0,0])

- The rotate.

### `dCorScale` @type(Double) @default(1.0)

- The coordinate scale.

### `dSearchRange` @type(Double) @default(0.0)

- The search range.

### `iUnit` @type(Integer) @default(0)

- The unit.
  \- 0: degree Kenvil (K).
  - 1: degree Celsius (deg C).
  - 2: degree Fahrenheit (deg F).

### `strPath` @type(String) @default("")

- The path.

### `crEdit` @type(Cursor) @default(None)

- The cursor of boundary condition need editing.

### `iMappingMethod` @type(Integer) @default(0)

- The mapping method.
  - 0: Mapping Nearest.
    - 1: Mapping CMLS.

### `iSubmodeLBCMappingType` @type(Integer) @default(3)

- The submode load boundary condition mapping type.
  - 0: Mapping type FORCED DISPLACEMENT.
    - 1: Mapping type LOAD FORCE.
    - 2: Mapping type EMPERATURE.
    - 3: Mapping type FORCED TEMPERATURE.
    - 4: Mapping type HEAT FLUX.

### `iMappingFromStepNo` @type(Integer) @default(0)

- The mapping from step number.

### `bSetADVCFile` @type(Boolean) @default(False)

- Whether set ADVC file.

### `strADVCResultFile` @type(String) @default("")

- The ADVC result file.

### `bSetDetATol` @type(Boolean) @default(False)

- Whether set det a tolerance.

### `dDetATol` @type(Double) @default(DFLT\_DBL)

- The det a tolerance.

### `bSetElementSet` @type(Boolean) @default(False)

- Whether set element set.

### `strElementSet` @type(String) @default("all")

- The element set.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
result = BoundaryConditions.BoundaryTemperature.SurfaceMapping(strName="MappingTemperature",
        crlTargets=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0,
        iMappedCpIndexArr1=0, dScaleFactor=1.0, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1.0,
        dSearchRange=0.0, iUnit=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=3,
        iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False,
        dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="all")
        
print(result) #for checking return value
```
