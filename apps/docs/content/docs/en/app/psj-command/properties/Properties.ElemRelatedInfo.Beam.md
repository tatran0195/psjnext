---
title: "Properties.ElemRelatedInfo.Beam()"
description: "Modify information such as direction vectors and end releases for the selected beam elements or 1D elements contained within the selected edge, individually"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > ElemRelatedInfo > Beam"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Set Beam Parameter","Modify information such as direction vectors and end releases for the selected beam elements or 1D elements contained within the selected edge, individually"]}
   [param_removed_unexpectedly] Param 'listEribeamEndProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEribeamOriVecProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEribeamOriNodeidProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEribeamOffsetVecA' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEribeamOffsetVecB' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEribeamPinAProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEribeamPinBProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEribeamWarpProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Modify information such as direction vectors and end releases for the selected beam elements or 1D elements contained within the selected edge, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Beam(...)
```

## Inputs

### `listERIBeamData` @type(List\[ERIBEAM\_DATA class]) @default(\[]) @since(5.1.0)

- The element related information of beam.

### `listEribeamEndProp` @type(ERIBEAM\_END\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The eribeam end property.

### `listEribeamOriVecProp` @type(ERIBEAM\_ORI\_VEC\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The eribeam ori vector property.

### `listEribeamOriNodeidProp` @type(ERIBEAM\_ORI\_NODEID\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The eribeam ori nodeid property.

### `listEribeamOffsetVecA` @type(ERIBEAM\_OFFSET\_VEC\_A List) @default(\[]) @deprecated @until(5.1.0)

- The eribeam offset vector a.

### `listEribeamOffsetVecB` @type(ERIBEAM\_OFFSET\_VEC\_B List) @default(\[]) @deprecated @until(5.1.0)

- The eribeam offset vector .

### `listEribeamPinAProp` @type(ERIBEAM\_PIN\_APROP List) @default(\[]) @deprecated @until(5.1.0)

- The eribeam pin a property.

### `listEribeamPinBProp` @type(ERIBEAM\_PIN\_BPROP List) @default(\[]) @deprecated @until(5.1.0)

- The eribeam pin property.

### `listEribeamWarpProp` @type(ERIBEAM\_WARP\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The eribeam warp property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {29-36}
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
Properties.Beam(
    strName="BEAM_1", 
    iPropertyColor=3742001, 
    crMaterial=Material(5), 
    dSectionArea=2e-07, 
    dlSectionOrientation=[DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    dlInertiaMoment=[DFLT_DBL, DFLT_DBL, DFLT_DBL], 
    dStressRecoveryCoeffCy=DFLT_DBL, 
    dStressRecoveryCoeffCz=DFLT_DBL, 
    dStressRecoveryCoeffDy=DFLT_DBL, 
    dStressRecoveryCoeffDz=DFLT_DBL, 
    dStressRecoveryCoeffEy=DFLT_DBL, 
    dStressRecoveryCoeffEz=DFLT_DBL, 
    dStressRecoveryCoeffFy=DFLT_DBL, 
    dStressRecoveryCoeffFz=DFLT_DBL, 
    crlTargets=[Elem(89, 88, 87)])
ret = Properties.ElemRelatedInfo.Beam(
    listERIBeamData=[
        ERIBEAM_DATA(
            iElemId=87, 
            iPropId=1, 
            iEndA=78, 
            iEndB=79, 
            dlOrientVec=[0.0, 0.0, 1.0])])
print(ret)
```
