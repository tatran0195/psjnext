---
title: DPostElem
id: DPostElem
---

## Description

This is an instance of a DPostElem class, represents a Post Element inside Jupiter.

## Properties

| Attribute   | Description                                                                                                                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| typeID      | Type ID of the Post Element (ID = 193).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                                                                 |
| id          | External ID of the Post Element.<br />ID of Post Element is unique.<br />The return value is ID (int).                                                                                                                       |
| type        | Type of the element.<br />The return value is [`ElemType`](../../../psj-command/element-types).                                                                                                                              |
| connectNode | The nodes belong to the Element.<br />The return value is a [DItemVector](../../pre-utility/built-in-types/DItemVector) object stores all information of nodes under [DItem](../../pre-utility/built-in-types/DItem) format. |
