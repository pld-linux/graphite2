#
# Conditional build:
%bcond_without	python	 # Python module (any)
%bcond_without	python2	 # CPython 2.x module
%bcond_without	python3	 # CPython 3.x module

%if %{without python}
%undefine	with_python2
%undefine	with_python3
%endif
Summary:	Font rendering capabilities for complex non-Roman writing systems
Summary(pl.UTF-8):	Wsparcie renderowania złożonych systemów pisma nierzymskiego
Name:		graphite2
Version:	1.3.14
Release:	5
License:	LGPL v2.1+ or GPL v2+ or MPL
Group:		Libraries
Source0:	https://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tgz
# Source0-md5:	1bccb985a7da01092bfb53bb5041e836
Patch0:		%{name}-fix_wrong_linker_opts.patch
Patch1:		%{name}-includes-libs-perl.patch
Patch2:		%{name}-python.patch
URL:		http://graphite.sil.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
# the rest for tests only
BuildRequires:	freetype-devel >= 2
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libicu-devel
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.605
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphite is a project within SIL's Non-Roman Script Initiative and
Language Software Development groups to provide rendering capabilities
for complex non-Roman writing systems. Graphite can be used to create
"smart fonts" capable of displaying writing systems with various
complex behaviors. With respect to the Text Encoding Model, Graphite
handles the "Rendering" aspect of writing system implementation.

%description -l pl.UTF-8
Graphite to projekt w ramach grup SIL Non-Roman Script Initiative
(inicjatywy pism nierzymskich SIL) oraz Language Software Development
(tworzenia oprogramowania językowego) mający na celu zapewnienie
wsparcia dla złożonych systemów pisma nierzymskiego. Graphite może być
używany do tworzenia "inteligentnych fontów", będących w stanie
wyświelać systemy pisma o różnych złożonych zachowaniach.
Uwzględniając model kodowania tekstu (Text Encoding Model) Graphite
obsługuje aspekt renderowania całości implementacji systemów pisma.

%package devel
Summary:	Header files for graphite2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graphite2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for graphite2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki graphite2.

%package -n python-graphite2
Summary:	Python 2 interface for graphite2 library
Summary(pl.UTF-8):	Interfejs Pythona 2 do biblioteki graphite2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-modules >= 1:2.7

%description -n python-graphite2
Python 2 interface for graphite2 library.

%description -n python-graphite2 -l pl.UTF-8
Interfejs Pythona 2 do biblioteki graphite2

%package -n python3-graphite2
Summary:	Python 3 interface for graphite2 library
Summary(pl.UTF-8):	Interfejs Pythona 3 do biblioteki graphite2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-modules >= 1:3.2

%description -n python3-graphite2
Python 3 interface for graphite2 library.

%description -n python3-graphite2 -l pl.UTF-8
Interfejs Pythona 3 do biblioteki graphite2

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%build
install -d build
cd build
%cmake .. \
	-DGRAPHITE2_VM_TYPE=direct

%{__make}
cd ..

%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# cmake's fake (with no dependencies); also obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgraphite2.la

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog doc/*.txt
%attr(755,root,root) %{_bindir}/gr2fonttest
%attr(755,root,root) %{_libdir}/libgraphite2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite2.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgraphite2.so
%{_includedir}/graphite2
%{_pkgconfigdir}/graphite2.pc
%{_datadir}/graphite2

%if %{with python2}
%files -n python-graphite2
%defattr(644,root,root,755)
%{py_sitescriptdir}/graphite2
%{py_sitescriptdir}/graphite2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-graphite2
%defattr(644,root,root,755)
%{py3_sitescriptdir}/graphite2
%{py3_sitescriptdir}/graphite2-%{version}-py*.egg-info
%endif
