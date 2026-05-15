---
title: "Connections.BarBeam()"
description: "Create Connections Bar or Beam"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > BarBeam"
---

## Description

Create Connections Bar or Beam.

## Syntax

```psj
Connections.BarBeam(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @optional -->
### iEType

- Specify the e type.
- The default value is 10.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### crProp

- Specify the property.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### dlOrient

- Specify the orient.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.BarBeam(strName, iEType=10, iMethod=1, crProp=None, dlOrient=[], crlMasterTargets=[], crlSlaveTargets=[])
```
