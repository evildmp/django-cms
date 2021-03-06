from __future__ import unicode_literals


# Placeholder operations
ADD_PLUGIN = 'add_plugin'
CHANGE_PLUGIN = 'change_plugin'
DELETE_PLUGIN = 'delete_plugin'
MOVE_PLUGIN = 'move_plugin'
CUT_PLUGIN = 'cut_plugin'
PASTE_PLUGIN = 'paste_plugin'
PASTE_PLACEHOLDER = 'paste_placeholder'
ADD_PLUGINS_FROM_PLACEHOLDER = 'add_plugins_from_placeholder'
CLEAR_PLACEHOLDER = 'clear_placeholder'

# Page operations
MOVE_PAGE = 'move_page'
DELETE_PAGE = 'delete_page'

# Page translation operations
DELETE_PAGE_TRANSLATION = 'delete_page_translation'
PUBLISH_PAGE_TRANSLATION = 'publish_page_translation'

# Static placeholder operations
PUBLISH_STATIC_PLACEHOLDER = 'publish_static_placeholder'

PAGE_OPERATIONS = [MOVE_PAGE, DELETE_PAGE]
PAGE_TRANSLATION_OPERATIONS = [DELETE_PAGE_TRANSLATION, PUBLISH_PAGE_TRANSLATION]
STATIC_PLACEHOLDER_OPERATIONS = [PUBLISH_STATIC_PLACEHOLDER]
