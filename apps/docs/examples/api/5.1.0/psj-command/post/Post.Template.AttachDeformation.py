# Title:   Post.Template.AttachDeformation()
# Desc:    Attach the current deformation settings to the specified template
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.AttachDeformation
# ---
Post.Template.Create(strName="Deformation_Template", strComment="Attach Deformation Template")
template = Post.Template.AttachDeformation(strName="Deformation_Template",   # [hl:start]
                                        postDataVizOptDeform=POST_DATA_VIZ_OPT_DEFORM(
                                            bEachDirectionRatio=True, 
                                            dlEachDirectionRatio=[0.05, 0.05, 0.05]))  # [hl:end]
JPT.Debugger(template)
