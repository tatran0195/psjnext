---
title: NASTRAN_OUTPUT_REQUEST
id: NASTRAN_OUTPUT_REQUEST
---

## Description

A data type uses to control parameters of Nastran Output Request

## Attributes

### `iValueDisplacement`

- An _Integer_ specifying the displacement output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueSpcforces`

- An _Integer_ specifying the single point constraint force output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueOload`

- An _Integer_ specifying the applied load output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueMpcforces`

- An _Integer_ specifying the multi-point constraint force output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueStress`

- An _Integer_ specifying the element stress output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueStrain`

- An _Integer_ specifying the element strain output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueForce`

- An _Integer_ specifying the element forces output request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueGpforces`

- An _Integer_ specifying the Grid Point Force Output Request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueNlstress`

- An _Integer_ specifying the Nonlinear Element Stress Output.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueStrainenergy`

- An _Integer_ specifying the strain energy output in selected elements.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueKineticenergy`

- An _Integer_ specifying the kinetic energy output in selected elements.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueBcresults`

- An _Integer_ specifying the contact result output.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueBgresults`

- An _Integer_ specifying the glue result output.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueSdisplacement`

- An _Integer_ specifying value the displacement in the solution set.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueAcceleration`

- An _Integer_ specifying the form and type of acceleration vector output.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueVelocity`

- An _Integer_ specifying the form and type of velocity vector output.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueMeffmass`

- An _Integer_ specifying the Modal Effective Mass Output Request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is 0.

### `iValueThermal`

- An _Integer_ specifying the Temperature Output Request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iValueFlux`

- An _Integer_ specifying the Flux, Gradient, or Particle Velocity Output Request.
    - 0: NONE.
    - DFLT_INT: ALL.
- The default value is DFLT_INT.

### `iTypeDisplacement`

- An _Integer_ specifying the type of displacement output. This value is calculated by using OR operator between the
  following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
    - 1043: PLOT&RPRINT&PSDF.
    - 3091: PLOT&RPRINT&PSDF&ATOC.
    - 5139: PLOT&RPRINT&PSDF&CRMS.
    - 8211: PLOT&RPRINT&RALL.
- The default value is 1.

### `iTypeSpcforces`

- An _Integer_ specifying the type of single point constraint force output request. This value is calculated by using OR
  operator between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeOload`

- An _Integer_ specifying the type of the applied load output request. This value is calculated by using OR operator
  between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeMpcforces`

- An _Integer_ specifying the type of multi point constraint force output request. This value is calculated by using OR
  operator between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeStress`

- An _Integer_ specifying the type of element stress output request. This value is calculated by using OR operator
  between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
    - 1043: PLOT&RPRINT&PSDF.
    - 3091: PLOT&RPRINT&PSDF&ATOC.
    - 5139: PLOT&RPRINT&PSDF&CRMS.
    - 8211: PLOT&RPRINT&RALL.
- The default value is 1.

### `iTypeStrain`

- An _Integer_ specifying the type of element strain output request. This value is calculated by using OR operator
  between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 1.

### `iTypeForce`

- An _Integer_ specifying the type of element forces output request. This value is calculated by using OR operator
  between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeGpforces`

- An _Integer_ specifying the type of Grid Point Force Output Request. This value is calculated by using OR operator
  between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeNlstress`

- An _Integer_ specifying the type of Nonlinear Element Stress Output. This value is calculated by using OR operator
  between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeStrainenergy`

- An _Integer_ specifying the type of strain energy output in selected elements. This value is calculated by using OR
  operator between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeKineticenergy`

- An _Integer_ specifying the type of kinetic energy output in selected elements. This value is calculated by using OR
  operator between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeBcresults`

- An _Integer_ specifying the type of contact result output. This value is calculated by using OR operator between the
  following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeBgresults`

- An _Integer_ specifying the type of glue result output. This value is calculated by using OR operator between the
  following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeSdisplacement`

- An _Integer_ specifying the type of displacement in the solution set. This value is calculated by using OR operator
  between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeAcceleration`

- An _Integer_ specifying the type of acceleration vector output. This value is calculated by using OR operator between
  the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
    - 1043: PLOT&RPRINT&PSDF.
    - 3091: PLOT&RPRINT&PSDF&ATOC.
    - 5139: PLOT&RPRINT&PSDF&CRMS.
    - 8211: PLOT&RPRINT&RALL.
- The default value is 0.

### `iTypeVelocity`

- An _Integer_ specifying the type of velocity vector output. This value is calculated by using OR operator between the
  following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
    - 1043: PLOT&RPRINT&PSDF.
    - 3091: PLOT&RPRINT&PSDF&ATOC.
    - 5139: PLOT&RPRINT&PSDF&CRMS.
    - 8211: PLOT&RPRINT&RALL.
- The default value is 0.

### `iTypeMeffmass`

- An _Integer_ specifying the type of Modal Effective Mass Output Request. This value is calculated by using OR operator
  between the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeThermal`

- An _Integer_ specifying the type of Temperature Output Request. This value is calculated by using OR operator between
  the following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.

### `iTypeThermal`

- An _Integer_ specifying the type of Flux　Output Request. This value is calculated by using OR operator between the
  following options:
- For example, if PLOT and PRINT type were selected, then the type value = 1 | 2 = 3.
- The output value of each type are as follows.
    - 0: NONE.
    - 1: PLOT.
    - 2: PRINT.
    - 4: PUNCH.
    - 8: MAG PHASE.
    - 16: REAL PHASE.
    - 32: SORT1.
    - 64: SORT2.
    - 128: CORNER.
- The default value is 0.
