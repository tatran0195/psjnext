---
title: NASTRAN_ANALYSIS
id: NASTRAN_ANALYSIS
---

## Description

A data type uses to control parameters of Nastran Analysis

## Attributes

### `iSolverType`

- An _Integer_ specifying solver type.
  - 0: Unknown solver type.
  - 1: MSC Nastran solver type.
  - 2: NX Nastran solver type.
  - 3: Dynamic solver type.
  - 4: Dynamic solver type for Designer.
  - 5: Abaqus solver type.
  - 6: Sunshine Solver type.
  - 7: Sunshine Solver type for Designer.
- The default value is 0.

### `iWriteType`

- An _Integer_ specifying the writing type of solver input file.
  - 0: Writing by model.
  - 1: Writing by each body.
  - 2: Writing by bodies.
  - 3: Writing by each body, omitting the prefix in part file names.
- The default value is 0.

### `iGridFormatType`

- An _Integer_ specifying the Grid output format.
  - 0: Single. Small field format output.
  - 1: Double. Large field format output.
  - 2: Single F.P. Specify the floating-point number small field format output.
- The default value is 0.

### `bDeleteFloatingNodes`

- A _Boolean_ enable/disable delete floating nodes at the time of exporting output data.
- The default value is _False_.

### `bContinuanceMarker`

- A _Boolean_ enable/disable Output the continuation pointer + at the time of exporting output data.
- The default value is _False_.

### `bDefineLbcId`

- A _Boolean_ enable/disable the input load, single point constraint and multi-point constraint ID.
- The default value is _False_.

### `iDefinedLoadId`

- An _Integer_ specifying defined load ID.
- The default value is 0.

### `iDefinedSpcId`

- An _Integer_ specifying defined single point constraint ID.
- The default value is 0.

### `iDefinedMpcId`

- An _Integer_ specifying multi-point constraint ID.
- The default value is 0.

### `bUniqueLbcId`

- A _Boolean_ enable/disable the unique boundary ID option.
- The default value is _False_.

### `bUseCASI`

- A _Boolean_ enable/disable Direct solution/Iterative solution.
- The default value is _False_.

### `dEpsilon`

- A _Double_ specifying the convergence parameter in the iterative method.
- The default value is 0.0.

### `iMaxNumOfIter`

- An _Integer_ specifying maximum number of iterator.
- The default value is 0.

### `iNumberOfThreads`

- An _Integer_ specifying number of threads which use for parallelize.
- The default value is 0.

### `iMemory`

- An _Integer_ specifying Define the memory allocation amount(MB).
- The default value is 0.

### `bParamInrel`

- A _Boolean_ enable/disable initial relief option which use to simulate unconstrained structures in a static analysis .
- The default value is _False_.

### `iNcpu`

- An _Integer_ specifying number of CPU.
- The default value is 0.

### `iSolNo`

- An _Integer_ specifying solver number.
- The default value is 0.

### `strIncludeFilePath`

- A _String_ specifying include bdf file path.
- The default value is "".

### `nastranEigen`

- A _[NASTRAN_EIGEN](NASTRAN_EIGEN)_ specifying the Eigenvalues parameter of normal mode Nastran analysis .
- The default value is NASTRAN_EIGEN().

### `nastranEigen126`

- A _[NASTRAN_EIGEN126](NASTRAN_EIGEN126)_ specifying the eigenvalue parameter of Nastran nonlinear frequency analysis.
- The default value is NASTRAN_EIGEN126().

### `nastranFrequency`

- A _[NASTRAN_FREQUENCY](NASTRAN_FREQUENCY)_ specifying the frequency range and number of modes for eigenvalue
  extraction.
- The default value is NASTRAN_FREQUENCY().

### `nastranFreqTimestep`

- A _[NASTRAN_FREQ_TIMESTEP](NASTRAN_FREQ_TIMESTEP)_ specifying the response frequency setting.
- The default value is NASTRAN_FREQ_TIMESTEP().

### `nastranOutputRequest`

- A _[NASTRAN_OUTPUT_REQUEST](NASTRAN_OUTPUT_REQUEST)_ specifying the output request of solver.
- The default value is NASTRAN_OUTPUT_REQUEST().

### `nastranExecControl`

- A _[NASTRAN_EXEC_CONTROL](NASTRAN_EXEC_CONTROL)_ specifying the executive control option.
- The default value is NASTRAN_EXEC_CONTROL().

### `nastranCaseControl`

- A _[NASTRAN_CASE_CONTROL](NASTRAN_CASE_CONTROL)_ specifying the Case Control Option.
- The default value is NASTRAN_CASE_CONTROL().

### `nastranMainLbcSet`

- A _[NASTRAN_MAIN_LBC_SET](NASTRAN_MAIN_LBC_SET)_ specifying main boundary condition setting.
- The default value is NASTRAN_MAIN_LBC_SET().

### `nastranSettings`

- A _[NASTRAN_SETTINGS](NASTRAN_SETTINGS)_ specifying the nastran settings.
- The default value is NASTRAN_SETTINGS().

### `nastranNonlinear`

- A _[NASTRAN_NONLINEAR](NASTRAN_NONLINEAR)_ specifying the nastran nonlinear setting.
- The default value is NASTRAN_NONLINEAR().

### `nastranNonlinearTimestep`

- A _[NASTRAN_NONLINEAR_TIMESTEP](NASTRAN_NONLINEAR_TIMESTEP)_ specifying the nastran nonlinear timestep setting.
- The default value is NASTRAN_NONLINEAR_TIMESTEP().

### `nastranSubcase`

- A _NASTRAN_SUBCASE_ specifying the subcases.
- The default value is [].

### `strSystemCellText`

- A _String_ specifying directly the card to Nastran (System) section.
- The default value is "".

### `strFileManagementText`

- A _String_ specifying directly the text data in file management statement section.
- The default value is "".

### `strExecutiveControlText`

- A _String_ specifying directly the text data to the executive control section.
- The default value is "".

### `strGlobalCaseControlText`

- A _String_ specifying directly the global case control text to solver input file.
- The default value is "".

### `strBulkDataText`

- A _String_ specifying directly the bulk data text to solver input file.
- The default value is "".

### `iExportModelUnitSystem`

- A _Integer_ specifying the unit system for analysis input data.
- The default value is 0.
