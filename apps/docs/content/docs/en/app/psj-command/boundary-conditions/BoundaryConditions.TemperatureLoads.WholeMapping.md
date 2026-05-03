---
title: "BoundaryConditions.TemperatureLoads.WholeMapping()"
description: "Map temperagure load from solver data or csv."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > TemperatureLoads > WholeMapping"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create mapping pressure","Map temperagure load from solver data or csv."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Map temperagure load from solver data or csv.

## Syntax

```psj
BoundaryConditions.TemperatureLoads.WholeMapping(...)
```

## Inputs

### `strName` @type(String) @default("TemperatureLoadsWholeMapping")

- The name.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `iMAPPos` @type(Integer) @default(0)

- The m a p position.

### `iViewCp` @type(Integer) @default(0)

- The view component.

### `iCp` @type(Integer) @default(1)

- The component.

### `iSrcType` @type(Integer) @default(0)

- The source type.

### `iMappedCpIndexArr0` @type(Integer) @default(0)

- The mapped component index arr0.

### `iMappedCpIndexArr1` @type(Integer) @default(0)

- The mapped component index arr1.

### `iDScaleFactor` @type(Integer) @default(1)

- The d scale factor.

### `posOffset` @type(Position) @default(\[0,0,0])

- The offset.

### `posRotate` @type(Position) @default(\[0,0,0])

- The rotate.

### `dCorScale` @type(Double) @default(1)

- The cor scale.

### `dSearchRange` @type(Double) @default(0)

- The search range.

### `strPath` @type(String) @default("")

- The path.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iMappingMethod` @type(Integer) @default(0)

- The mapping method.

### `iSubmodelBCMappingType` @type(Integer) @default(2)

- The submodel c mapping type.

### `iMappingFromStepNo` @type(Integer) @default(0)

- The mapping from step no.

### `bSetADVCFile` @type(Boolean) @default(False)

- The set ADVC file.

### `strADVCResultFile` @type(String) @default("")

- The ADVC result file.

### `bSetDetATol` @type(Boolean) @default(False)

- The set det a tolerance.

### `dDetATol` @type(Double) @default(DFLT\_DBL)

- The det a tolerance.

### `bSetElementSet` @type(Boolean) @default(False)

- The set element set.

### `strElementSet` @type(String) @default("")

- The element set.

### `iTemperature` @type(Integer) @default(1) @since(5.1.0)

- The unit of temperature.
  - 0: K
  - 1: deg C
  - 2: deg F

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{8-11}
# Put solver data that includes temperature data.
mapping_data_file = "C:/Temp/sol159.op2"

# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

# Map temperature load
BoundaryConditions.TemperatureLoads.WholeMapping(
    strName = "TemperatureLoadsWholeMapping_1", 
    strPath = mapping_data_file, 
    iMappingFromStepNo = 0)
```
