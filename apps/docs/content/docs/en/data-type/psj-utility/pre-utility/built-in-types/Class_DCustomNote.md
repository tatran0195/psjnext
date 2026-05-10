---
title: DCustomNote
id: DCustomNote
---

## Description

This is an instance of a DCustomNote class, represents a custom note inside Jupiter.

## Properties

| Attribute     | Description                                                                                                                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| typeID        | Type ID of the custom note (ID = 270).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                                                                               |
| tableID       | Table ID of the custom note item (ID = 154). The return value is an [`Int notation of DTable Types`](../enumeration-types/dtable-types)(int).                                                                                             |
| id            | External ID of the custom note.<br />The return value is ID (int).                                                                                                                                                                        |
| name          | Name of the custom note.<br />The return value is a string.                                                                                                                                                                               |
| target_type   | Type of the type of target entity which the custom note is created on. The return value is:<br />0 (None),<br />1 (Node),<br />2 (1D Element),<br />3 (2D Element),<br />4 (3D Element),<br />5 (Face Point),<br /> 6 (Edge Point).<br /> |
| target_pos    | Position coordinate of the Custom Note.<br /> The return value is [`TVector3d.`](../built-in-types/TVector3d)                                                                                                                             |
| target_item   | The target entity which the custom note is created on. The return value is a [`DItem`](../../../psj-command/DItem-types).                                                                                                                 |     |
| parent        | The custom note collection where the new custom note is append.<br /> The return value is [`DCustomNoteCollection.`](../built-in-types/DCustomNoteCollection)                                                                             |
| content       | Content of the Custom Note. <br /> The return value is the list of strings.                                                                                                                                                               |
| font_size     | The font size of the text of Content. <br /> The return value is int.                                                                                                                                                                     |
| font_color    | The color of the text of Content. <br /> The return value is a RGB color.                                                                                                                                                                 |
| font_bold     | Bold text or not in the Content.<br /> The return value is 0 or 1 (bold)                                                                                                                                                                  |
| bgcolor       | The ground color of the Custom Note.<br /> The return value is a RGB color.                                                                                                                                                               |
| outline_width | The width of the note border.<br /> The return value is int.                                                                                                                                                                              |
| outline_color | The color of the note border.<br /> The return value is a RGB color.                                                                                                                                                                      |
| arrow_width   | The thickness of the line extending from the note to the coordinate position.<br />The return value is int.                                                                                                                               |
| arrow_color   | The color of the line extending from the note to the coordinate position.<br />The return value is a RGB color.                                                                                                                           |
| arrow_type    | The shape type that points to the coordinate position.<br /> The return value is 0 (None) or 1 (Arrow)                                                                                                                                    |
| alignment     | The alignment type.<br /> Currently, no setting is available. The return value is always 0.                                                                                                                                               |
