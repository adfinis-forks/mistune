.. _directives:

Directives
==========

A directive is a generic block of explicit markup that is powerful
and extensible. In mistune v3, there are 2 styles of directives for
now:

1. reStructuredText style
2. fenced style

.. versionchanged:: 3.0

    Fenced style directive is added in 3.0. Because v3 has multiple
    styles of directives, developers can not add each directive into
    ``plugins`` parameter of ``mistune.create_markdown`` directly.
    Instead, each directive should be wrapped by::

        import mistune
        from mistune.directives import FencedDirective, RstDirective
        from mistune.directives import Admonition, TableOfContents

        markdown = mistune.create_markdown(plugins=[
            'math',
            'footnotes',
            # ...
            FencedDirective([
                Admonition(),
                TableOfContents(),
            ]),
        ])

        markdown = mistune.create_markdown(plugins=[
            'math',
            'footnotes',
            # ...
            RstDirective([
                Admonition(),
                TableOfContents(),
            ]),
        ])

A **reStructuredText** style of directive is inspired by reStructuredText_,
and the syntax looks like:

.. code-block:: text

    .. directive-name:: title
       :option-key: option value
       :option-key: option value

       content text here


A **fenced** style of directive looks like a fenced code block, it is
inspired by `markdown-it-docutils`_. The syntax looks like:

.. code-block:: text

    ```{directive-name} title
    :option-key: option value
    :option-key: option value

    content text here
    ```

.. _reStructuredText: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#directives

.. _`markdown-it-docutils`: https://executablebooks.github.io/markdown-it-docutils/


Developers can choose the directive style in their own favor.

Admonitions
-----------

The reStructuredText style syntax:

.. code-block:: text

    .. warning::

       You are looking at the **dev** documentation. Check out our
       [stable](/stable/) documentation instead.

The fenced style syntax:

.. code-block:: text

    ```{warning}
    You are looking at the **dev** documentation. Check out our
    [stable](/stable/) documentation instead.
    ```

Admonitions contains a group of ``directive-name``:

.. code-block:: text

    attention  caution  danger  error
    hint  important  note  tip  warning

To enable admonitions::

    import mistune
    from mistune.directives import Admonition

    markdown = mistune.create_markdown(
        plugins=[
            ...
            RstDirective([Admonition()]),
            # FencedDirective([Admonition()]),
        ]
    )


Table of Contents
-----------------

.. code-block:: text

    .. toc:: Table of Contents
       :max-level: 3

TOC plugin is based on directive. It can add a table of contents section in
the documentation. Let's take an example:

.. code-block:: text

   Here is the first paragraph, and we put TOC below.

   .. toc::

   # H1 title

   ## H2 title

   # H1 title

The rendered HTML will show a TOC at the ``.. toc::`` position. To enable
TOC plugin::

    import mistune
    from mistune.directives import RstDirective, TableOfContents

    markdown = mistune.create_markdown(
        plugins=[
            # ...
            RstDirective([TableOfContents()]),
        ]
    )

Include
-------

.. code-block:: text

    .. include:: hello.md

``include`` is a powerful plugin for documentation generator. With this
plugin, we can embed contents from other files.
