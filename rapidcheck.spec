Summary:	RapidCheck - C++ framework for property based testing
Summary(pl.UTF-8):	RapidCheck - szkielet C++ do testowania opartego na własnościach
Name:		rapidcheck
Version:	0
%define	gitref	1505cbbce733bde3b78042cf2e9309c0b7f227a2
%define	snap	20230114
%define	rel	1
Release:	0.%{snap}.%{rel}
License:	BSD
Group:		Libraries
Source0:	https://github.com/emil-e/rapidcheck/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	be5af76d09734665f2e1962539f23a58
# 03d122a is v2.4.2 tag
%define	catch_ver	2.4.2
Source1:	https://github.com/catchorg/Catch2/archive/v%{catch_ver}/Catch2-%{catch_ver}.tar.gz
# Source1-md5:	26927b878b1f42633f15a9ef1c4bd8e7
%define	gtest_gitref	e38ef3be887afc0089005e394c5001002e313960
Source2:	https://github.com/google/googletest/archive/%{gtest_gitref}/googletest-%{gtest_gitref}.tar.gz
# Source2-md5:	ed4d7fc957e9cdd07af56926676ebd8d
URL:		https://github.com/emil-e/rapidcheck
BuildRequires:	cmake >= 3.0
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
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for RapidCheck library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RapidCheck.

%prep
%setup -q -n %{name}-%{gitref}

tar xf %{SOURCE1} -C ext/catch --strip-components=1
tar xf %{SOURCE2} -C ext/googletest --strip-components=1

%build
install -d build
cd build
%cmake .. \
	-DRC_ENABLE_CATCH=ON \
	-DRC_ENABLE_GMOCK=ON \
	-DRC_ENABLE_GTEST=ON

%{__make}

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
%attr(755,root,root) %{_libdir}/librapidcheck.so

%files devel
%defattr(644,root,root,755)
%doc doc/*.md
%{_includedir}/rapidcheck
%{_includedir}/rapidcheck.h
%dir %{_datadir}/rapidcheck
%{_datadir}/rapidcheck/cmake
