#
# spec file for package gridplus
#

Name:           gridplus
BuildRequires:  tcl >= 8.6
Version:        2.11
Release:        0
Summary:        Grid based layout system for Tcl/Tk
Url:            http://www.satisoft.com/tcltk/gridplus2/
License:        TCL
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       tcl >= 8.6
Requires:       tk >= 8.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        gridplus.zip

%description
GRIDPLUS is a "Grid" based GUI builder system which builds on,
simplifies and extends the existing Tk grid manager.

%prep
%setup -q -n %{name}

%build

%install
dir=%buildroot%tcl_noarchdir/%name%version
mkdir -m755 -p $dir
chmod a-x *.tcl
cp -a *.tcl $dir

%files
%defattr(-,root,root)
%doc LICENSE.GRIDPLUS
%tcl_noarchdir

%changelog

