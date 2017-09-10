#!/usr/bin/tclsh

set arch "noarch"
set base "gridplus"
set fileurl "http://www.satisoft.com/tcltk/gridplus2/download/gridplus.zip"

set var [list wget $fileurl -O $base.zip]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.zip build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb gridplus.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.zip
