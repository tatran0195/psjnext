---
title: "Properties.ElemRelatedInfo.Rod()"
description: "Modify information such as direction vectors and end releases for the selected rod elements, individually"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > ElemRelatedInfo > Rod"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Set Rod Parameter","Modify information such as direction vectors and end releases for the selected rod elements, individually"]}
   [param_removed_unexpectedly] Param 'listEricontEndProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Modify information such as direction vectors and end releases for the selected rod elements, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Rod(...)
```

## Inputs

### `listERIRodData` @type(List\[ERIROD\_DATA class]) @default(\[]) @since(5.1.0)

- The element related information of rod.

### `listEricontEndProp` @type(ERICONT\_END\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The ericont end property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {19-25}
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
Properties.Rod(
    strName="ROD_1", 
    iPropertyColor=3742001, 
    crMat=Material(5), 
    dArea=2e-07, 
    crlTargets=[Elem(89, 88, 87)])
ret = Properties.ElemRelatedInfo.Rod(
        listERIRodData=[
            ERIROD_DATA(
                iElemId=87, 
                iPropId=1, 
                iEndA=79, 
                iEndB=78)])
print(ret)
```
