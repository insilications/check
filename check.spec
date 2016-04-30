#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : check
Version  : 0.10.0
Release  : 13
URL      : http://downloads.sourceforge.net/check/check-0.10.0.tar.gz
Source0  : http://downloads.sourceforge.net/check/check-0.10.0.tar.gz
Summary  : A unit test framework for C
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 LGPL-2.0+ LGPL-2.1
Requires: check-bin
Requires: check-lib
Requires: check-doc
BuildRequires : cmake
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libsubunit)
BuildRequires : sed

%description
About Check
-----------
Check is a unit testing framework for C. It features a simple interface
for defining unit tests, putting little in the way of the
developer. Tests are run in a separate address space, so Check can
catch both assertion failures and code errors that cause segmentation
faults or other signals. The output from unit tests can be used within
source code editors and IDEs.

%package bin
Summary: bin components for the check package.
Group: Binaries

%description bin
bin components for the check package.


%package dev
Summary: dev components for the check package.
Group: Development
Requires: check-lib
Requires: check-bin

%description dev
dev components for the check package.


%package doc
Summary: doc components for the check package.
Group: Documentation

%description doc
doc components for the check package.


%package lib
Summary: lib components for the check package.
Group: Libraries

%description lib
lib components for the check package.


%prep
%setup -q -n check-0.10.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/checkmk

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/check/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
