#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scrypt
Version  : 0.8.6
Release  : 1
URL      : https://files.pythonhosted.org/packages/01/6f/3c8dd0f18f73ceddfbdd606c0c895ebb66748606682d77da3743c7c0c56f/scrypt-0.8.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/6f/3c8dd0f18f73ceddfbdd606c0c895ebb66748606682d77da3743c7c0c56f/scrypt-0.8.6.tar.gz
Summary  : Bindings for the scrypt key derivation function library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: scrypt-python3
Requires: scrypt-license
Requires: scrypt-python
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
Requires: scrypt-python3

%description python
python components for the scrypt package.


%package python3
Summary: python3 components for the scrypt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the scrypt package.


%prep
%setup -q -n scrypt-0.8.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533785599
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/scrypt
cp LICENSE %{buildroot}/usr/share/doc/scrypt/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/scrypt/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
