# Title:   Post.Template.AttachViewPoint()
# Desc:    Attach the current view point settings to the specified template
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post/Post.Template.AttachViewPoint
# ---
Post.Template.Create(strName="ViewPoint_Template", strComment="Attach View Point Template")
template = Post.Template.AttachViewPoint(strName="ViewPoint_Template",   # [hl:start]
                                        postDataVizOptViewPoint=POST_DATA_VIZ_OPT_VIEWPOINT(
                                            dlTranslationMatrix=[-0.707107, -0.5, 0.5, 0.0, 0.707107, -0.5, 0.5, 0.0, -4.49147e-08, 0.707107, 0.707107, 0.0, 0.0, 0.0, 0.0, 1.0], 
                                            dlCenter=[0.016, 0.005, 0.0025], 
                                            dScaleFactor=0.0115058))  # [hl:end]
JPT.Debugger(template)
