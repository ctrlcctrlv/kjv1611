This font is made with FontForge. You will also need `ttx` and `sfnt2woff` to do a complete build.

When it comes to advanced typographical features, FontForge's UI is rarely conducive to implementing them. Therefore we use feature files and scripts for all advanced typography.

To build from development SFD:

* Run fontforge as `PYTHONPATH=. fontforge KJV1611.sfd`
* Re-encode as UTF-8 BMP
* Merge `features.fea` file
* Execute `script.txt`
* Generate `.otf` font
* Exit _without saving!_
* Run `post-build.sh`
