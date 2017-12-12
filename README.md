# Sources for the TFP-2018 webpage

Based on the CADE-26 website.

To make simple edits to the webpage do
the following:

  1. edit the `.txt` files

  2. run `make` at the command-line to generate the `.html` files

  3. check the look of the new content in your browser, e.g. on Mac OS run `open start.html` at the command-line; if there are errors in the html, go back to step 1

  4. push your version to github with `git commit -a` and `git push`

  5. update the public version of the webpage by going to the public update page

For more significant changes, edits may be required to `build.py` which
is intentionally very simple and, I hope, understandable.
