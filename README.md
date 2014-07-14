Strings Localization
================================

A simple script that makes it easy to export a well-formatted Google spreadsheet into localized strings files for use in Cocoa and Cocoa Touch applications. Adapted from Max Vilimpoc's [localization-spreadsheet-jsonify](https://github.com/nuket/localization-spreadsheet-jsonify).

Step 1
------

Make spreadsheet formatted like [this one](https://docs.google.com/spreadsheet/ccc?key=0AqrUvD5TZZs3dF9ULUh5X1JlakVJRGFHaWRZQmFuZEE).

Step 2
------

**Export it to Cocoa .strings files**:

1. Copy the localize-strings.py to your project folder.
2. Edit localize-strings.py, setting `SHEET_ID` to the ID of your Google Spreadsheet, and `SHEET_NAME` to the name of the sheet used in that Google Spreadsheet.
3. Run localize-strings.py, optionally specifying an output directory as the first argument.
4. Done.

More Info
---------

To see more info about invoking the app, go [here](https://script.google.com/macros/s/AKfycbxLnEUyElPtL01qHnL7pD2hmTmaO7Tc1yLhjJzQpitpuBfxxBU/exec).
