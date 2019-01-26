This font is made with FontForge.

When it comes to advanced typographical features, FontForge's UI is rarely conducive to implementing them. Therefore we use feature files and scripts for all advanced typography.

To build from development SFD:

* Run fontforge as `PYTHONPATH=. fontforge KJV1611.sfd`
* Re-encode as UTF-8 BMP
* Merge `features.fea` file
* Execute `script.txt`
* Generate `.otf` font
* Exit _without saving!_
