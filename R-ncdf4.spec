#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ncdf4
Version  : 1.17
Release  : 15
URL      : https://cran.r-project.org/src/contrib/ncdf4_1.17.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ncdf4_1.17.tar.gz
Summary  : Interface to Unidata netCDF (Version 4 or Earlier) Format Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-ncdf4-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : netcdf-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-ncdf4 package.
Group: Libraries

%description lib
lib components for the R-ncdf4 package.


%prep
%setup -q -c -n ncdf4
cd %{_builddir}/ncdf4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624484065

%install
export SOURCE_DATE_EPOCH=1624484065
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ncdf4
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ncdf4
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ncdf4
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ncdf4 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ncdf4/DESCRIPTION
/usr/lib64/R/library/ncdf4/HDF5_COPYING
/usr/lib64/R/library/ncdf4/INDEX
/usr/lib64/R/library/ncdf4/Meta/Rd.rds
/usr/lib64/R/library/ncdf4/Meta/features.rds
/usr/lib64/R/library/ncdf4/Meta/hsearch.rds
/usr/lib64/R/library/ncdf4/Meta/links.rds
/usr/lib64/R/library/ncdf4/Meta/nsInfo.rds
/usr/lib64/R/library/ncdf4/Meta/package.rds
/usr/lib64/R/library/ncdf4/NAMESPACE
/usr/lib64/R/library/ncdf4/R/ncdf4
/usr/lib64/R/library/ncdf4/R/ncdf4.rdb
/usr/lib64/R/library/ncdf4/R/ncdf4.rdx
/usr/lib64/R/library/ncdf4/help/AnIndex
/usr/lib64/R/library/ncdf4/help/aliases.rds
/usr/lib64/R/library/ncdf4/help/ncdf4.rdb
/usr/lib64/R/library/ncdf4/help/ncdf4.rdx
/usr/lib64/R/library/ncdf4/help/paths.rds
/usr/lib64/R/library/ncdf4/html/00Index.html
/usr/lib64/R/library/ncdf4/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ncdf4/libs/ncdf4.so
/usr/lib64/R/library/ncdf4/libs/ncdf4.so.avx2
/usr/lib64/R/library/ncdf4/libs/ncdf4.so.avx512
