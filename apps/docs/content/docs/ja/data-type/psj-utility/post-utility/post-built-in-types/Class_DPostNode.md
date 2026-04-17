---
title: DPostNode
id: DPostNode
---

## Description

This is an instance of a DPostNode class, represents a Post Node inside Jupiter.

## Properties

| Attribute   | Description                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| typeID      | Type ID of the Post Node (ID = 192).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                                                                |
| id          | External ID of the Post Node.<br />ID of Post Node is unique.<br />The return value is ID (int).                                                                                                                         |
| connectElem | The shared-node elements.<br />The return value is a [DItemVector](../../pre-utility/built-in-types/DItemVector) object stores all information of elements under [DItem](../../pre-utility/built-in-types/DItem) format. |
