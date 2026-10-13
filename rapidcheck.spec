Summary:	RapidCheck - C++ framework for property based testing
Summary(pl.UTF-8):	RapidCheck - szkielet C++ do testowania opartego na własnościach
Name:		rapidcheck
Version:	0
%define	gitref	2c3c4365aca21ef4e612768fdc95b1ce8b39a651
%define	snap	20261006
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	BSD
Group:		Libraries
Source0:	https://github.com/emil-e/rapidcheck/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	d1a5501ba28881f943de90cab5c87e11
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-pc.patch
URL:		https://github.com/emil-e/rapidcheck
BuildRequires:	cmake >= 3.16
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RapidCheck is a C++ framework for property based testing inspired by
QuickCheck and other similar frameworks. In property based testing,
you state facts about your code that given certain precondition should
always be true. RapidCheck then generates random test data to try and
find a case for which the property doesn't hold. If such a case is
found, RapidCheck tries to find the smallest case (for some definition
of smallest) for which the property is still false and then displays
this as a counterexample. For example, if the input is an integer,
RapidCheck tries to find the smallest integer for which the property
is false.

%description -l pl.UTF-8
RapidCheck to szkielet C++ do testowania opartego na własnościach,
zainspirowany przez QuickCheck i podobne szkielety. W testowaniu
opartym na własnościach ustala się fakty dotyczące kodu, że konkretne
warunki wstępne powinny być prawdziwe. Następnie RapidCheck generuje
losowe dane testowe i próbuje znaleźć przypadek, dla którego własność
nie jest zachowana. Jeśli to się uda, próbuje znaleźć najmniejszy
(zgodnie z pewną definicją) przypadek, dla którego własność jest
nadal fałszywa, a następnie wyświetla ten kontrprzykład. Np. jeśli
wejście jest liczbą całkowitą, RapidCheck próbuje znaleźć najmniejszą
liczbę całkowitą, dla którego własność nie jest spełniona.

%package devel
Summary:	Header files for RapidCheck library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RapidCheck
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for RapidCheck library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RapidCheck.

%prep
%setup -q -n %{name}-%{gitref}
%patch -P0 -p1
%patch -P1 -p1

%build
%cmake -B build \
	-DRC_ENABLE_CATCH=ON \
	-DRC_ENABLE_DOCTEST=ON \
	-DRC_ENABLE_GMOCK=ON \
	-DRC_ENABLE_GTEST=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{_libdir}/librapidcheck.so

%files devel
%defattr(644,root,root,755)
%doc doc/*.md
%{_includedir}/rapidcheck
%{_includedir}/rapidcheck.h
%{_pkgconfigdir}/rapidcheck.pc
%{_pkgconfigdir}/rapidcheck_catch.pc
%{_pkgconfigdir}/rapidcheck_doctest.pc
%{_pkgconfigdir}/rapidcheck_gtest.pc
%dir %{_datadir}/rapidcheck
%{_datadir}/rapidcheck/cmake
