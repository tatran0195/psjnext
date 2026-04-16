# Title:   Properties.ElemRelatedInfo.Gap()
# Desc:    Modify information such as direction vectors and end releases for the selected gap elements, individually
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/properties/Properties.ElemRelatedInfo.Gap
# ---
Geometry.Part.Cube(iPartColor=6409934)
Connections.Gaps.TwoNodes(
    crlMaster=[Node(6)], 
    crlSlave=[Node(8)], 
    iOriMode=1, 
    strName="GAP_1", 
    dlOriVec=[0.0, 0.0, 0.0])
ret = Properties.ElemRelatedInfo.Gap(  # [hl:start]
        listERIGapData=[
            ERIGAP_DATA(
                iElemId=1090, 
                iEndA=6, 
                iEndB=8, 
                dlOrientVec=[0.0, 1.0, 0.0])])  # [hl:end]
print(ret)
