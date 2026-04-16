# Title:   Properties.ElemRelatedInfo.Bush()
# Desc:    Modify information such as direction vectors and end releases for the selected bush elements, individually
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.ElemRelatedInfo.Bush
# ---
Geometry.Part.Cube(iPartColor=6409934)
Connections.SpringsDampers.Bush.TwoNodes(
    crlMaster=[Node(53)], 
    crlSlave=[Node(61)], 
    iOriMode=1)
ret = Properties.ElemRelatedInfo.Bush(  # [hl:start]
    listERIBushData=[
        ERIBUSH_DATA(
            iElemId=1089, 
            iEndA=53, 
            iEndB=61, 
            dlOrientVec=[0.0, 1.0, 0.0])])  # [hl:end]
print(ret)
