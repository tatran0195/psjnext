---
title: "Connections.Contacts.TSSS.ManualGroup()"
description: "Define contact settings between specified groups for TechnoStar SunShine solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > SunShine > Manual Group"
---
<!-- REVIEW FLAGS — requires human review
   [param_removed_unexpectedly] Param 'tssolverContact' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

This method defines a contact setting between specified groups for TechnoStar SunShine solver.

## Syntax

```psj
Connections.Contacts.TSSS.ManualGroup(...)
```

## Inputs

### `strName` @type(String) @default("ContactTS\_SS\_1")

- The contact name.

### `sunshineContact` @type(SUNSHINE\_CONTACT) @default(SUNSHINE\_CONTACT) @since(5.1.0)

- The Sunshine contact parameters.

### `crplTarget` @type(List\[Pairs of Cursor]) @default(\[])

- The pair of master and slave groups.

### `crEdit` @type(Cursor) @default(None)

- An existing SunShine contact setting. If this argument is specified, the specified SunShine contact setting will be modified. If unspecified, a new SunShine contact setting will be created.

### `iColor` @type(Integer) @default(0)

- The contact-to-display marker color.

### `iMethod` @type(Integer) @default(1)

- The method.

### `tssolverContact` @type(SUNSHINE\_CONTACT) @default(SUNSHINE\_CONTACT) @deprecated @until(5.1.0)

- The Sunshine contact parameters.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj {10-12}
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=4803000)

Connections.Contacts.SunShine.ManualFace(crlMasterFaces=[Face(24)], crlSlaveFaces=[Face(49)],
    strName="ContactSunShine_1", sunshineContact=SUNSHINE_CONTACT(dERROR=0.001, dFRIC=0.5,
    dSLIDE=DFLT_DBL, iICOORD=DFLT_INT, dSFACT=DFLT_DBL, dSFACTT=0.5, dCDAMP=DFLT_DBL),
    iContactColor=16711680)

Connections.Contacts.TSSS.ManualGroup(strName="ContactSunShine_2", iColor=16711680,
    sunshineContact=SUNSHINE_CONTACT(dERROR=1e-06, dFRIC=0.5, dSLIDE=DFLT_DBL, iICOORD=DFLT_INT,
    dSFACT=DFLT_DBL, dSFACTT=0.5, dCDAMP=DFLT_DBL), crplTarget=[CursorPair(Group(1), Group(2))])
```
