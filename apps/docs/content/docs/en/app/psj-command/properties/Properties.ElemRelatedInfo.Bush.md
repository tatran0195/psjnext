---
title: "Properties.ElemRelatedInfo.Bush()"
description: "Modify information such as direction vectors and end releases for the selected bush elements, individually"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > ElemRelatedInfo > Bush"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Set Shell Parameter","Modify information such as direction vectors and end releases for the selected bush elements, individually"]}
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

Modify information such as direction vectors and end releases for the selected bush elements, individually

## Syntax

```psj
Properties.ElemRelatedInfo.Bush(...)
```

## Inputs

### `listERIBushData` @type(List\[ERIBUSH\_DATA class]) @default(\[]) @since(5.1.0)

- The element related information of bush.

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

```psj {6-12}
Geometry.Part.Cube(iPartColor=6409934)
Connections.SpringsDampers.Bush.TwoNodes(
    crlMaster=[Node(53)], 
    crlSlave=[Node(61)], 
    iOriMode=1)
ret = Properties.ElemRelatedInfo.Bush(
    listERIBushData=[
        ERIBUSH_DATA(
            iElemId=1089, 
            iEndA=53, 
            iEndB=61, 
            dlOrientVec=[0.0, 1.0, 0.0])])
print(ret)
```
