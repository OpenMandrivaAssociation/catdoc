#!/usr/bin/perl -n

m!<U(\w+)>\s*/x(\w+)\s! and print "0x$2    0x$1\n";
