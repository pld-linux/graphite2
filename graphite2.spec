Summary:	Font rendering capabilities for complex non-Roman writing systems
Summary(pl.UTF-8):	Wsparcie renderowania złożonych systemów pisma nierzymskiego
Name:		graphite2
Version:	1.3.10
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tgz
# Source0-md5:	b39d5ed21195f8b709bcee548c87e2b5
Patch0:		%{name}-fix_wrong_linker_opts.patch
Patch1:		%{name}-includes-libs-perl.patch
URL:		http://graphite.sil.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
# the rest for tests only
BuildRequires:	freetype-devel >= 2
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libicu-devel
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DGRAPHITE2_VM_TYPE=direct

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# cmake's fake (with no dependencies); also obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgraphite2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*.txt
%attr(755,root,root) %{_bindir}/gr2fonttest
%attr(755,root,root) %{_libdir}/libgraphite2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite2.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgraphite2.so
%{_includedir}/graphite2
%{_pkgconfigdir}/graphite2.pc
%{_datadir}/graphite2
