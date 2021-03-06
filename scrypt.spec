#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scrypt
Version  : 0.8.17
Release  : 17
URL      : https://files.pythonhosted.org/packages/57/02/040f517985d66e2b453ac1abf50e9e4fde64094f64029add8bbd28b6d331/scrypt-0.8.17.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/02/040f517985d66e2b453ac1abf50e9e4fde64094f64029add8bbd28b6d331/scrypt-0.8.17.tar.gz
Summary  : Bindings for the scrypt key derivation function library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: scrypt-license = %{version}-%{release}
Requires: scrypt-python = %{version}-%{release}
Requires: scrypt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev

%description
Python scrypt_ bindings
        =========================
        
        This is a set of Python_ bindings for the scrypt_ key derivation
        function.

%package license
Summary: license components for the scrypt package.
Group: Default

%description license
license components for the scrypt package.


%package python
Summary: python components for the scrypt package.
Group: Default
Requires: scrypt-python3 = %{version}-%{release}

%description python
python components for the scrypt package.


%package python3
Summary: python3 components for the scrypt package.
Group: Default
Requires: python3-core
Provides: pypi(scrypt)

%description python3
python3 components for the scrypt package.


%prep
%setup -q -n scrypt-0.8.17
cd %{_builddir}/scrypt-0.8.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600113979
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scrypt
cp %{_builddir}/scrypt-0.8.17/LICENSE %{buildroot}/usr/share/package-licenses/scrypt/53471b347f9dfca463c4be7a4fd46b8a05e6f323
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scrypt/53471b347f9dfca463c4be7a4fd46b8a05e6f323

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
