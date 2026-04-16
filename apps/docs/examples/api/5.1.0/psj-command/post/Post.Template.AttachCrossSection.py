# Title:   Post.Template.AttachCrossSection()
# Desc:    Attach the current cross section settings to the specified template
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.AttachCrossSection
# ---
Post.Template.Create(strName="Cross Section", strComment="Attach Cross Section Template")
template = Post.Template.AttachCrossSection(strName="Cross Section",   # [hl:start]
                                        postDataVizOptCrossSection=POST_DATA_VIZ_OPT_CROSS_SECTION(
                                            bCapping=False, 
                                            bCuttingEdge=True, 
                                            bSectionElem=True, 
                                            bMeshLine=True, 
                                            dlTranslationMatrix=[1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.016, 0.005, 0.0025, 1.0], 
                                            dlPosition=[0.016, 0.005, 0.0025]))  # [hl:end]
JPT.Debugger(template)
