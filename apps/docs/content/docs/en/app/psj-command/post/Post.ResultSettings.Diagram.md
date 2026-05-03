---
title: "Post.ResultSettings.Diagram()"
description: "Set up the result settings for displaying the diagram"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > ResultSettings > Diagram"
macro_link: "[CmdPostDiagramSettings](../../macro/post/CmdPostDiagramSettings)"
---

## Description

Set up the result settings for displaying the diagram.

## Syntax

```psj
Post.ResultSettings.Diagram(...)
```

## Inputs

### `postDataVizOptDiagram` @type(POST\_DATA\_VIZ\_OPT\_DIAGRAM) @default(POST\_DATA\_VIZ\_OPT\_DIAGRAM)

- All settings of the diagram display.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Diagram(postDataVizOptDiagram=PostDataVizOptDiagram(dRatioModel=0.05, dRatioScreen=0.05))
```
