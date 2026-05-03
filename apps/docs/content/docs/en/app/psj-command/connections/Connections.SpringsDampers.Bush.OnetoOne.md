---
title: "Connections.SpringsDampers.Bush.OnetoOne()"
description: "Create bush connection between target nodes within tolerance."
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > SpringsDampers > Bush > OnetoOne"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create bush connection","Create bush connection between target nodes within tolerance."]}
   [param_decorator_changed] Param 'crlMaster' @default changed from '[]' to '(none)' in v5.1.0
     context: {"param":"crlMaster","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"[]"}
   [param_removed_unexpectedly] Param 'crlSlave' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'iEqual' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_decorator_changed] Param 'dlStiffness' @default changed from '[]' to 'all DFLT_DBL' in v5.1.0
     context: {"param":"dlStiffness","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"[]","toDefault":"all DFLT_DBL"}
   [param_decorator_changed] Param 'dlDampCoef' @default changed from '[]' to 'all DFLT_DBL' in v5.1.0
     context: {"param":"dlDampCoef","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"[]","toDefault":"all DFLT_DBL"}
   [param_decorator_changed] Param 'dlDampConst' @default changed from '[]' to 'all DFLT_DBL' in v5.1.0
     context: {"param":"dlDampConst","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"[]","toDefault":"all DFLT_DBL"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create bush connection between target nodes within tolerance.

## Syntax

```psj
Connections.SpringsDampers.Bush.OnetoOne(...)
```

## Inputs

### `iMethod` @type(Integer) @default(21)

- The method.

### `strName` @type(String) @default("BUSH\_1")

- The name.

### `crlMaster` @type(List\[Cursor]) @required

- The target nodes.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `dTol` @type(Double) @default(DFLT\_DBL)

- The tolerance.

### `iGround` @type(Integer) @default(0)

- The ground.

### `iOriMode` @type(Integer) @default(0)

- The ori mode.

### `poslVector` @type(Position List) @default(\[])

- The vector.

### `dlStiffness` @type(Double List) @default(all DFLT\_DBL)

- The Stiffness 1 to 6.

### `dlDampCoef` @type(Double List) @default(all DFLT\_DBL)

- The Damping Coeff. 1 to 6.

### `dlDampConst` @type(Double List) @default(all DFLT\_DBL)

- The Damping Const. 1 to 6.

### `dRotStrain` @type(Double) @default(DFLT\_DBL)

- The rotation strain.

### `dTransStrain` @type(Double) @default(DFLT\_DBL)

- The trans strain.

### `dRotStress` @type(Double) @default(DFLT\_DBL)

- The rotation stress.

### `dTransStress` @type(Double) @default(DFLT\_DBL)

- The trans stress.

### `crlStiffTbl` @type(Lits of Cursor) @default(all 0:0) @since(5.1.0)

- The Field Data for the table of Stiffness 1 to 6.

### `crlDampCoefTbl` @type(Lits of Cursor) @default(all 0:0) @since(5.1.0)

- The Field Data for the table of Damping Coef. 1 to 6.

### `crlDampConstTbl` @type(Lits of Cursor) @default(all 0:0) @since(5.1.0)

- The Field Data for table of Damping Const. 1 to 6.

### `crEditObj` @type(Cursor) @default(None)

- The edit object.

### `crlSlave` @type(List\[Cursor]) @default(\[]) @deprecated @until(5.1.0)

- The slave.

### `iEqual` @type(Integer) @default(1) @deprecated @until(5.1.0)

- The equal.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj{4-15}
#Prepare Model
Geometry.Part.Cube(iPartColor=6409934)

Connections.SpringsDampers.Bush.OnetoOne(
    strName="BUSH_1", 
    crlMaster=[Node(4, 25, 1, 9, 8, 89, 5, 73)], 
    dTol=0.01, 
    iOriMode=1,  
    poslVector=[0, 0, 0],    
    dlStiffness=[100.0, 200.0, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    dlDampCoef=[500.0, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    dlDampConst=[0.2, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL],
    crlStiffTbl=[Unknown(0, 0, 0, 0, 0, 0)], 
    crlDampCoefTbl=[Unknown(0, 0, 0, 0, 0, 0)], 
    crlDampConstTbl=[Unknown(0, 0, 0, 0, 0, 0)])
```
