"""
    mistune
    ~~~~~~~

    A fast yet powerful Python Markdown parser with renderers and
    plugins, compatible with sane CommonMark rules.

    Documentation: https://mistune.lepture.com/
"""

from .markdown import Markdown
from .core import BlockState, InlineState, BaseRenderer
from .block_parser import BlockParser
from .inline_parser import InlineParser
from .html_renderer import HTMLRenderer
from .util import escape, escape_url, safe_entity, unikey
from .plugins import import_plugin


def create_markdown(escape=True, hard_wrap=False, renderer='html', plugins=None):
    """Create a Markdown instance based on the given condition.

    :param escape: Boolean. If using html renderer, escape html.
    :param hard_wrap: Boolean. Break every new line into ``<br>``.
    :param renderer: renderer instance, default is HTMLRenderer.
    :param plugins: List of plugins.

    This method is used when you want to re-use a Markdown instance::

        markdown = create_markdown(
            escape=False,
            hard_wrap=True,
        )
        # re-use markdown function
        markdown('.... your text ...')
    """
    if renderer == 'html':
        renderer = HTMLRenderer(escape=escape)

    inline = InlineParser(renderer, hard_wrap=hard_wrap)
    if plugins is not None:
        plugins = [import_plugin(n) for n in plugins]
    return Markdown(inline=inline, plugins=plugins)


html = create_markdown(
    escape=False,
    plugins=['strikethrough', 'footnotes', 'table', 'speedup']
)


__cached_parsers = {}


def markdown(text, escape=True, renderer='html', plugins=None):
    key = (escape, renderer, plugins)
    if key in __cached_parsers:
        return __cached_parsers[key](text)

    md = create_markdown(escape=escape, renderer=renderer, plugins=plugins)
    # improve the speed for markdown parser creation
    __cached_parsers[key] = md
    return md(text)


__all__ = [
    'Markdown', 'HTMLRenderer',
    'BlockParser', 'BlockState', 'BaseRenderer',
    'InlineParser', 'InlineState',
    'escape', 'escape_url', 'safe_entity', 'unikey',
    'html', 'create_markdown', 'markdown',
]

__version__ = '3.0.0rc2'
__homepage__ = 'https://mistune.lepture.com/'
