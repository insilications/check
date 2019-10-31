#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : check
Version  : 0.13.0
Release  : 23
URL      : https://github.com/libcheck/check/releases/download/0.13.0/check-0.13.0.tar.gz
Source0  : https://github.com/libcheck/check/releases/download/0.13.0/check-0.13.0.tar.gz
Summary  : A unit test framework for C
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0+ LGPL-2.1
Requires: check-bin = %{version}-%{release}
Requires: check-lib = %{version}-%{release}
Requires: check-license = %{version}-%{release}
Requires: check-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : pkg-config
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libsubunit)
BuildRequires : sed

%description
# About Check
Check is a unit testing framework for C. It features a simple interface
for defining unit tests, putting little in the way of the
developer. Tests are run in a separate address space, so Check can
catch both assertion failures and code errors that cause segmentation
faults or other signals. The output from unit tests can be used within
source code editors and IDEs.

%package bin
Summary: bin components for the check package.
Group: Binaries
Requires: check-license = %{version}-%{release}

%description bin
bin components for the check package.


%package dev
Summary: dev components for the check package.
Group: Development
Requires: check-lib = %{version}-%{release}
Requires: check-bin = %{version}-%{release}
Provides: check-devel = %{version}-%{release}
Requires: check = %{version}-%{release}

%description dev
dev components for the check package.


%package dev32
Summary: dev32 components for the check package.
Group: Default
Requires: check-lib32 = %{version}-%{release}
Requires: check-bin = %{version}-%{release}
Requires: check-dev = %{version}-%{release}

%description dev32
dev32 components for the check package.


%package doc
Summary: doc components for the check package.
Group: Documentation
Requires: check-man = %{version}-%{release}

%description doc
doc components for the check package.


%package lib
Summary: lib components for the check package.
Group: Libraries
Requires: check-license = %{version}-%{release}

%description lib
lib components for the check package.


%package lib32
Summary: lib32 components for the check package.
Group: Default
Requires: check-license = %{version}-%{release}

%description lib32
lib32 components for the check package.


%package license
Summary: license components for the check package.
Group: Default

%description license
license components for the check package.


%package man
Summary: man components for the check package.
Group: Default

%description man
man components for the check package.


%prep
%setup -q -n check-0.13.0
cd %{_builddir}/check-0.13.0
pushd ..
cp -a check-0.13.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572561581
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static  --disable-subunit  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1572561581
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/check
cp %{_builddir}/check-0.13.0/COPYING.LESSER %{buildroot}/usr/share/package-licenses/check/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/check-0.13.0/doc/example/cmake/COPYING-CMAKE-SCRIPTS.txt %{buildroot}/usr/share/package-licenses/check/77976f406ba34009d9ba5a43b882fe6de68e5175
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/checkmk

%files dev
%defattr(-,root,root,-)
/usr/include/check.h
/usr/include/check_stdint.h
/usr/lib64/libcheck.so
/usr/lib64/pkgconfig/check.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcheck.so
/usr/lib32/pkgconfig/32check.pc
/usr/lib32/pkgconfig/check.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/check/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcheck.so.0
/usr/lib64/libcheck.so.0.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcheck.so.0
/usr/lib32/libcheck.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/check/77976f406ba34009d9ba5a43b882fe6de68e5175
/usr/share/package-licenses/check/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/checkmk.1
