---
title: "Properties.ElemRelatedInfo.Shell()"
description: "Modify information such as direction vectors and end releases for the selected shell elements or elements contained in a face, individually"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > ElemRelatedInfo > Shell"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Set Shell Parameter","Modify information such as direction vectors and end releases for the selected shell elements or elements contained in a face, individually"]}
   [param_removed_unexpectedly] Param 'listErishellThetaProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listErishellCsProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listErishellZoffsProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Modify information such as direction vectors and end releases for the selected shell elements or elements contained in a face, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Shell(...)
```

## Inputs

### `listERIShellData` @type(List\[ERISHELL\_DATA class]) @default(\[]) @since(5.1.0)

- The element related information of shell.

### `listErishellThetaProp` @type(ERISHELL\_THETA\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The erishell theta property.

### `listErishellCsProp` @type(ERISHELL\_CS\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The erishell cs property.

### `listErishellZoffsProp` @type(ERISHELL\_ZOFFS\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The erishell zoffs property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {22-31}
Geometry.Part.Cube(iPartColor=6409934)
Properties.Material.Add(
    strMaterialName="Structural_Steel", 
    dictMaterialProperty={
        'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
        'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
        'POISSONS_RATIO': [0.3]}}, 
        'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
        'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
        'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
    iMaterialID=5, 
    iMaterialColor=10264731)
Properties.Shell(
    crlTargets=[Part(1)], 
    strName="ShellProperty_1", 
    iPropertyId=2, 
    iPropertyColor=3315481, 
    crMatMembrane=Material(5), 
    crMatBend=Material(5), 
    crMatShear=Material(5), 
    dThickness=0.0002)
ret = Properties.ElemRelatedInfo.Shell(
        listERIShellData=[
            ERISHELL_DATA(
                iElemId=117, 
                iPropId=2, 
                dTheta=0.523599), 
            ERISHELL_DATA(
                iElemId=118, 
                iPropId=2, 
                dTheta=0.523599)])
print(ret)
```
