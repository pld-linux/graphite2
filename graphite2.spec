Summary:	Font rendering capabilities for complex non-Roman writing systems
Name:		silgraphite
Version:	2.3.1
Release:	1
License:	LGPL v2+ or CPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tar.gz
# Source0-md5:	d35724900f6a4105550293686688bbb3
URL:		http://graphite.sil.org/
BuildRequires:	freetype-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphite is a project within SIL’s Non-Roman Script Initiative and
Language Software Development groups to provide rendering capabilities
for complex non-Roman writing systems. Graphite can be used to create
"smart fonts" capable of displaying writing systems with various
complex behaviors. With respect to the Text Encoding Model, Graphite
handles the "Rendering" aspect of writing system implementation.

%package devel
Summary:	Header files for silgraphite library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki silgraphite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for silgraphite library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki silgraphite.

%package static
Summary:	Static silgraphite library
Summary(pl.UTF-8):	Statyczna biblioteka silgraphite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static silgraphite library.

%description static -l pl.UTF-8
Statyczna biblioteka silgraphite.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/pango/1.6.0/modules/graphite/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libgraphite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite.so.3
%attr(755,root,root) %{_libdir}/libgraphite-ft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite-ft.so.0
%attr(755,root,root) %{_libdir}/libgraphite-xft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgraphite-xft.so.0
%dir %{_libdir}/pango/1.6.0/modules/graphite
%attr(755,root,root) %{_libdir}/pango/1.6.0/modules/graphite/pango-graphite.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgraphite.so
%attr(755,root,root) %{_libdir}/libgraphite-ft.so
%attr(755,root,root) %{_libdir}/libgraphite-xft.so
%{_libdir}/libgraphite.la
%{_libdir}/libgraphite-ft.la
%{_libdir}/libgraphite-xft.la
%{_includedir}/graphite
%{_pkgconfigdir}/silgraphite.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgraphite.a
%{_libdir}/libgraphite-ft.a
%{_libdir}/libgraphite-xft.a
