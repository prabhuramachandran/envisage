
from enthought.envisage.ui.action.api import Action, ActionSet, Group

# Service Ids used in actions.
ITEXT_EDITOR = 'enthought.plugins.text_editor.api.TextEditorService'

class TextEditorActionSet(ActionSet):
    """ The default action set for the Text Editor plugin.
    """

    groups = [
        Group(
            id = "TextFileGroup",
            path = "MenuBar/File",
            before = "ExitGroup",
        )
    ]

    actions = [
        Action(
            id = "NewFileAction",
            name = "New File",
            class_name='enthought.plugins.text_editor.actions.NewFileAction',
            group='TextFileGroup',
            path="MenuBar/File",
        ),

        Action(
            id = 'OpenFile',
            name = "Open File...",
            class_name='enthought.plugins.text_editor.actions.OpenFileAction',
            group='TextFileGroup',
            path="MenuBar/File",
        ),
    ]


