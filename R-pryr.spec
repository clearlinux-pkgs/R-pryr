#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pryr
Version  : 0.1.4
Release  : 54
URL      : https://cran.r-project.org/src/contrib/pryr_0.1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pryr_0.1.4.tar.gz
Summary  : Tools for Computing on the Language
Group    : Development/Tools
License  : GPL-2.0
Requires: R-pryr-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-assertthat
BuildRequires : R-Rcpp
BuildRequires : R-assertthat
BuildRequires : buildreq-R

%description
# pryr (rhymes with pry bar)
[![Build Status](https://travis-ci.org/hadley/pryr.png?branch=master)](https://travis-ci.org/hadley/pryr)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/pryr)](https://cran.r-project.org/package=pryr)
[![codecov.io](http://codecov.io/github/hadley/pryr/coverage.svg?branch=master)](http://codecov.io/github/hadley/pryr?branch=master)

%package lib
Summary: lib components for the R-pryr package.
Group: Libraries

%description lib
lib components for the R-pryr package.


%prep
%setup -q -c -n pryr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552782517

%install
export SOURCE_DATE_EPOCH=1552782517
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pryr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pryr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pryr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  pryr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pryr/DESCRIPTION
/usr/lib64/R/library/pryr/INDEX
/usr/lib64/R/library/pryr/Meta/Rd.rds
/usr/lib64/R/library/pryr/Meta/features.rds
/usr/lib64/R/library/pryr/Meta/hsearch.rds
/usr/lib64/R/library/pryr/Meta/links.rds
/usr/lib64/R/library/pryr/Meta/nsInfo.rds
/usr/lib64/R/library/pryr/Meta/package.rds
/usr/lib64/R/library/pryr/NAMESPACE
/usr/lib64/R/library/pryr/R/pryr
/usr/lib64/R/library/pryr/R/pryr.rdb
/usr/lib64/R/library/pryr/R/pryr.rdx
/usr/lib64/R/library/pryr/help/AnIndex
/usr/lib64/R/library/pryr/help/aliases.rds
/usr/lib64/R/library/pryr/help/paths.rds
/usr/lib64/R/library/pryr/help/pryr.rdb
/usr/lib64/R/library/pryr/help/pryr.rdx
/usr/lib64/R/library/pryr/html/00Index.html
/usr/lib64/R/library/pryr/html/R.css
/usr/lib64/R/library/pryr/tests/testthat.R
/usr/lib64/R/library/pryr/tests/testthat/helper-object_size.R
/usr/lib64/R/library/pryr/tests/testthat/test-active-binding.r
/usr/lib64/R/library/pryr/tests/testthat/test-bytes.r
/usr/lib64/R/library/pryr/tests/testthat/test-ftype.r
/usr/lib64/R/library/pryr/tests/testthat/test-method-from-call.r
/usr/lib64/R/library/pryr/tests/testthat/test-object_size.R
/usr/lib64/R/library/pryr/tests/testthat/test-track-copy.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pryr/libs/pryr.so
/usr/lib64/R/library/pryr/libs/pryr.so.avx2
/usr/lib64/R/library/pryr/libs/pryr.so.avx512
