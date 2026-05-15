---
title: "Post.ResultSettings.Diagram()"
description: "Set up the result settings for displaying the diagram"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > ResultSettings > Diagram"
macro _link: "[CmdPostDiagramSettings](../../macro/post/CmdPostDiagramSettings)"
---

## Description

Set up the result settings for displaying the diagram.

## Syntax

```psj
Post.ResultSettings.Diagram(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### postDataVizOptDiagram

- Specify all settings of the diagram display.
- The default value is [POST\_DATA\_VIZ\_OPT\_DIAGRAM](../../data-type/psj-command/parameter-types/POST _DATA _VIZ _OPT _DIAGRAM).

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {1}
Post.ResultSettings.Diagram(postDataVizOptDiagram=PostDataVizOptDiagram(dRatioModel=0.05, dRatioScreen=0.05))
```
