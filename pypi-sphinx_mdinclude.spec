#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-sphinx_mdinclude
Version  : 0.5.3
Release  : 4
URL      : https://files.pythonhosted.org/packages/9f/53/7a4f8c341066f12795a32d544ead6a1a1f0f7d8ccf7fe3465d994437f44a/sphinx_mdinclude-0.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/9f/53/7a4f8c341066f12795a32d544ead6a1a1f0f7d8ccf7fe3465d994437f44a/sphinx_mdinclude-0.5.3.tar.gz
Summary  : Markdown extension for Sphinx
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx_mdinclude-license = %{version}-%{release}
Requires: pypi-sphinx_mdinclude-python = %{version}-%{release}
Requires: pypi-sphinx_mdinclude-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(flit_core)
BuildRequires : pypi(mistune)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
sphinx-mdinclude
================
Sphinx extension for including or writing pages in Markdown format.

%package license
Summary: license components for the pypi-sphinx_mdinclude package.
Group: Default

%description license
license components for the pypi-sphinx_mdinclude package.


%package python
Summary: python components for the pypi-sphinx_mdinclude package.
Group: Default
Requires: pypi-sphinx_mdinclude-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_mdinclude package.


%package python3
Summary: python3 components for the pypi-sphinx_mdinclude package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_mdinclude)
Requires: pypi(docutils)
Requires: pypi(mistune)
Requires: pypi(pygments)

%description python3
python3 components for the pypi-sphinx_mdinclude package.


%prep
%setup -q -n sphinx_mdinclude-0.5.3
cd %{_builddir}/sphinx_mdinclude-0.5.3
pushd ..
cp -a sphinx_mdinclude-0.5.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686241513
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . mistune
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . mistune
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_mdinclude
cp %{_builddir}/sphinx_mdinclude-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_mdinclude/a8acb8fddf1f0bbb74f235984d15d048f8db4542 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} mistune
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_mdinclude/a8acb8fddf1f0bbb74f235984d15d048f8db4542

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
