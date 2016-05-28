#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pryr
Version  : 0.1.2
Release  : 16
URL      : http://cran.r-project.org/src/contrib/pryr_0.1.2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/pryr_0.1.2.tar.gz
Summary  : Tools for Computing on the Language
Group    : Development/Tools
License  : GPL-2.0
Requires: R-pryr-lib
Requires: R-Rcpp
Requires: R-stringr
BuildRequires : R-Rcpp
BuildRequires : R-stringr
BuildRequires : clr-R-helpers

%description
# pryr (rhymes with pry bar)
[![Build Status](https://travis-ci.org/hadley/pryr.png?branch=master)](https://travis-ci.org/hadley/pryr)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/pryr)](http://cran.r-project.org/web/packages/pryr)
[![Coverage Status](https://img.shields.io/codecov/c/github/hadley/pryr/master.svg)](https://codecov.io/github/hadley/pryr?branch=master)

%package lib
Summary: lib components for the R-pryr package.
Group: Libraries

%description lib
lib components for the R-pryr package.


%prep
%setup -q -c -n pryr

%build

%install
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
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library pryr
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pryr


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pryr/DESCRIPTION
/usr/lib64/R/library/pryr/INDEX
/usr/lib64/R/library/pryr/Meta/Rd.rds
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
/usr/lib64/R/library/pryr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pryr/libs/pryr.so
