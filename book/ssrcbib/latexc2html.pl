#!/usr/bin/perl
#
# This script filters LaTeX character sequences into html.
#
# $Id$

while (<STDIN>) {
  s/\\ / /g;
  s/\\\&/\&amp\;/g;
  s/\-\-\-/\&mdash\;/g;		# Do this before ndash!
  s/\-\-/\&ndash\;/g;
  s/\\c([cCsStT])/\&${1}cedil\;/g;
  s/\\ug/g/g;
  s/\\i/i/g;
  s/\\\^([aeiouAEIOU])/\&${1}circ\;/g;
  s/\\\"([aeiouAEIOU])/\&${1}uml\;/g;
  s/\\\'([aceiou])/\&${1}acute\;/g;
  s/\\\`([aeiou])/\&${1}grave\;/g;
  s/\\\/([oO])/\&${1}slash\;/g;
  s/\\v(.)/${1}&#780\;/g;	# Adds a caron to previous letter
  s/\\\.(.)/${1}&#775\;/g;	# Adds dot above to previous letter
  s/\~/\&nbsp;/g;
  s/\\,/\&nbsp;/g;
  print;
}
