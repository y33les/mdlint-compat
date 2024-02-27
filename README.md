# mdlint-compat 0.1.0

**A drag-and-drop wrapper for pymarkdownlnt**

mdlint-compat is a wrapper for pymarkdownlnt enabling drag-and-drop
behaviour for users unfamiliar with the command line.  Its use case is
probably fairly uncommon outside of our work environment: an
environment in which markdownlint is used centrally but is unavailable
on user machines.

Although not support by pymarkdownlnt itself, mdlint-compat supports
the enable/disable behaviour of markdownlint, meaning that linting can
be turned off like so:

```markdown
This text will be linted.

<!-- markdownlint-disable -->

This text will not be linted.
Make as many questionable decisions as you like here!

<!-- markdownlint-enable -->

This text will be linted again.
```

This wrapper makes use of pymarkdownlnt's default ruleset.  Excluding
or adding rules is beyond the necessary scope of mdlint-compat, but
can be achieved by modifying line 43 of `lint.py` if required.

## Prerequisites

mdlint-compat assumes that you have successfully installed Python 3
using Anaconda.  There are no other prerequisites as mdlint-compat
will install the needed Python packages itself (if required).

## Usage

1. Download the latest release (the ZIP file) and extract it into a
   new folder.
1. Open the folder in Windows Explorer.
1. Copy the Markdown file you wish to fix into the folder containing
   mdlint-compat.
1. Drag and drop your Markdown file on to the batch script named
   `DROP_FILES_HERE.bat`.  mdlint-compat will automatically produce a
   fixed version of your file with the extension `.fixed.md`.
    - **N.B.:** Your Markdown file _must_ end with the extension `.md`
      or pymarkdownlnt will fail!

---

> _Many thanks to [@jackdewinter](https://github.com/jackdewinter) for
the [pymarkdown](https://github.com/jackdewinter/pymarkdown) library
and pymarkdownlnt._
