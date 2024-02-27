# mdlint-compat 0.1.0

**A drag-and-drop wrapper for pymarkdownlnt**

mdlint-compat is a wrapper for pymarkdownlnt enabling drag-and-drop
behaviour for users unfamiliar with the command line.  Its use case is
probably fairly uncommon outside of our work environment: an
environment in which markdownlint is used centrally but is unavailable
on user machines.

## Prerequisites

mdlint-compat assumes that you have successfully installed Python 3
using Anaconda.  There are no other prerequisites as mdlint-compat
will install the needed Python packages itself (if required).

## Usage

1. Download the latest release and extract it into a new folder.
1. Open the folder in Windows Explorer.
1. Drag and drop the Markdown file you wish to fix on to the batch script
named `DROP_FILES_HERE.bat`.  mdlint-compat will automatically produce
a fixed version of your file with the extension `.fixed.md`.

> _Many thanks to [@jackdewinter](https://github.com/jackdewinter) for
the [pymarkdown](https://github.com/jackdewinter/pymarkdown) library
and pymarkdownlnt._
