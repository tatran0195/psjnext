---
title: "Properties.ElemRelatedInfo.Gap()"
description: "Modify information such as direction vectors and end releases for the selected gap elements, individually"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > ElemRelatedInfo > Gap"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Set Shell Parameter","Modify information such as direction vectors and end releases for the selected gap elements, individually"]}
   [param_removed_unexpectedly] Param 'listEricontEndProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEricontOriVecProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listCidProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEricontDamperLocProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listOcidProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listDamperOffsetVecs' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'listEricontNodeidProp' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Modify information such as direction vectors and end releases for the selected gap elements, individually.

## Syntax

```psj
Properties.ElemRelatedInfo.Gap(...)
```

## Inputs

### `listERIGapData` @type(List\[ERIGAP\_DATA class]) @default(\[]) @since(5.1.0)

- The element related information of gap.

### `listEricontEndProp` @type(ERICONT\_END\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The ericont end property.

### `listEricontOriVecProp` @type(ERICONT\_ORI\_VEC\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The ericont ori vector property.

### `listCidProp` @type(CID\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The cid property.

### `listEricontDamperLocProp` @type(ERICONT\_DAMPER\_LOC\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The ericont damper location property.

### `listOcidProp` @type(OCID\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The ocid property.

### `listDamperOffsetVecs` @type(DAMPER\_OFFSET\_VECS List) @default(\[]) @deprecated @until(5.1.0)

- The damper offset vecs.

### `listEricontNodeidProp` @type(ERICONT\_NODEID\_PROP List) @default(\[]) @deprecated @until(5.1.0)

- The ericont nodeid property.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {8-14}
Geometry.Part.Cube(iPartColor=6409934)
Connections.Gaps.TwoNodes(
    crlMaster=[Node(6)], 
    crlSlave=[Node(8)], 
    iOriMode=1, 
    strName="GAP_1", 
    dlOriVec=[0.0, 0.0, 0.0])
ret = Properties.ElemRelatedInfo.Gap(
        listERIGapData=[
            ERIGAP_DATA(
                iElemId=1090, 
                iEndA=6, 
                iEndB=8, 
                dlOrientVec=[0.0, 1.0, 0.0])])
print(ret)
```
