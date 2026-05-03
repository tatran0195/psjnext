---
title: "Properties.Shell()"
description: "Assign Shell property to the selected entities"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Shell"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Apply Shell property on the selected entities","Assign Shell property to the selected entities"]}
   [param_decorator_changed] Param 'strName' @default changed from '"Shell Property"' to '"ShellProperty"' in v5.1.0
     context: {"param":"strName","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"\"Shell Property\"","toDefault":"\"ShellProperty\""}
   [param_removed_unexpectedly] Param 'iPID' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_decorator_changed] Param 'dMatOrient1' @default changed from '0.0' to 'DFLT_DBL' in v5.1.0
     context: {"param":"dMatOrient1","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.0","toDefault":"DFLT_DBL"}
   [param_decorator_changed] Param 'dThickness' @default changed from '(none)' to 'DFLT_DBL' in v5.1.0
     context: {"param":"dThickness","fromVersion":"5.0.1","toVersion":"5.1.0","toDefault":"DFLT_DBL"}
   [param_decorator_changed] Param 'dBendStiff' @default changed from '0.0' to 'DFLT_DBL' in v5.1.0
     context: {"param":"dBendStiff","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.0","toDefault":"DFLT_DBL"}
   [param_decorator_changed] Param 'dThickRatio' @default changed from '0.5' to 'DFLT_DBL' in v5.1.0
     context: {"param":"dThickRatio","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.5","toDefault":"DFLT_DBL"}
   [param_decorator_changed] Param 'dNSM' @default changed from '0.0' to 'DFLT_DBL' in v5.1.0
     context: {"param":"dNSM","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.0","toDefault":"DFLT_DBL"}
   [param_decorator_changed] Param 'dFiberDist1' @default changed from '0.0' to 'DFLT_DBL' in v5.1.0
     context: {"param":"dFiberDist1","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.0","toDefault":"DFLT_DBL"}
   [param_decorator_changed] Param 'dFiberDist2' @default changed from '0.0' to 'DFLT_DBL' in v5.1.0
     context: {"param":"dFiberDist2","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.0","toDefault":"DFLT_DBL"}
   [param_decorator_changed] Param 'dPlateOff' @default changed from '0.0' to 'DFLT_DBL' in v5.1.0
     context: {"param":"dPlateOff","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0.0","toDefault":"DFLT_DBL"}
   [param_decorator_changed] Param 'iItgPts' @default changed from '0' to 'DFLT_DBL' in v5.1.0
     context: {"param":"iItgPts","fromVersion":"5.0.1","toVersion":"5.1.0","fromDefault":"0","toDefault":"DFLT_DBL"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Assign Shell property to the selected entities.

## Syntax

```psj
Properties.Shell(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @required

- The target to assign the Shell property. The target can be Part, Face, or 2D Element.

### `strName` @type(String) @default("ShellProperty")

- The property name.

### `iPropertyId` @type(Integer) @default(1) @since(5.1.0)

- The property identification number (ID number).

### `iPropertyColor` @type(Integer) @default(0) @since(5.1.0)

- The property color.

### `crMatMembrane` @type(Cursor) @default(None)

- The material for membrane behavior.

### `crMatBend` @type(Cursor) @default(None)

- The material for bending behavior.

### `crMatShear` @type(Cursor) @default(None)

- The material for lateral shear behavior.

### `crMatCoupl` @type(Cursor) @default(None)

- The material for coupled film-bending behavior.

### `dMatOrient1` @type(Double) @default(DFLT\_DBL)

- The theta angle 1 when material orientation is defined by angle.

### `dThickness` @type(Double) @default(DFLT\_DBL)

- The thickness of element in millimeters.

### `dBendStiff` @type(Double) @default(DFLT\_DBL)

- The bending stiffness parameter.

### `dThickRatio` @type(Double) @default(DFLT\_DBL)

- The thickness ratio of the lateral shear stiffness.

### `dNSM` @type(Double) @default(DFLT\_DBL)

- The Non-Structural Mass which is a contribution to the model mass from features that have negligible structural stiffness.

### `dFiberDist1` @type(Double) @default(DFLT\_DBL)

- The Fiber distances 1 for stress computation from the reference plane.

### `dFiberDist2` @type(Double) @default(DFLT\_DBL)

- The Fiber distances 2 for stress computation from the reference plane.

### `dPlateOff` @type(Double) @default(DFLT\_DBL)

- The offset value from the reference plane.

### `iItgPts` @type(Integer) @default(DFLT\_DBL)

- The integral number of shell elements.

### `iMatOrientType` @type(Integer) @default(0)

- The material orientation type (Angle - 0 or Coordinate system - 1).

### `crLocalCS` @type(Cursor) @default(None)

- The Local coordinate system when material orientation is defined by Coordinate system.
  The X axis of the coordinate system is projected to the element plane.

### `crEdit` @type(Cursor) @default(None)

- An existing Shell property setting item.
  - If this parameter is used, the specified Shell property setting item will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new Shell property setting item will be created.

### `iDuplicateOpt` @type(Integer) @default(0)

- The duplicate option. When the property is already assigned to some of the selected bodies
  - If this value = 6 means the existing property will be changed.
  - If this value = 2 or 7 means the property will be assigned only to bodies that do not have the property assigned yet.

### `iPanelLabelId` @type(Integer) @default(1) @since(5.1.0)

- The panel label ID.

### `strPanelLabelName` @type(String) @default('') @since(5.1.0)

- The panel label name.

### `iPanelLabelERP` @type(Integer) @default(0) @since(5.1.0)

- Whether to enable the ERP function.

### `iTempVariation` @type(Integer) @default(DFLT\_INT) @since(5.1.0)

- The temperature variation value (Natural numbers only).

### `iPID` @type(Integer) @default(1) @deprecated @until(5.1.0)

- The property identification number (ID number).

## Return Code

A _Cursor_ specifying the created shell property.

## Sample Code

```psj {12-18}
Geometry.Part.Cube()
Properties.Material.Add(strMaterialName="Structural_Steel", 
                        dictMaterialProperty={
                          'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
                          'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
                          'POISSONS_RATIO': [0.3]}}, 
                          'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
                          'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
                          'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
                        iMaterialID=5, 
                        iMaterialColor=10264731)
created_prop = Properties.Shell(crlTargets=[Face(26, 24)], 
                              strName="ShellProperty_1", 
                              iPropertyColor=15329791, 
                              crMatMembrane=Material(5), 
                              crMatBend=Material(5), 
                              crMatShear=Material(5), 
                              dThickness=0.01)
JPT.Debugger(created_prop)
```
