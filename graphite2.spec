Summary:	Font rendering capabilities for complex non-Roman writing systems
Name:		graphite2
Version:	1.0.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/silgraphite/graphite2/%{name}-%{version}.tgz
# Source0-md5:	3bf481ca95109b14435125c0dd1f2217
Patch0:		%{name}-1.0.2-no_harfbuzz_tests.patch
Patch1:		%{name}-fix_wrong_linker_opts.patch
Patch2:		%{name}-includes-libs-perl.patch
URL:		http://graphite.sil.org/
BuildRequires:	cmake
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig
BuildRequires:	silgraphite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphite is a project within SIL’s Non-Roman Script Initiative and
Language Software Development groups to provide rendering capabilities
for complex non-Roman writing systems. Graphite can be used to create
"smart fonts" capable of displaying writing systems with various
complex behaviors. With respect to the Text Encoding Model, Graphite
handles the "Rendering" aspect of writing system implementation.

%package devel
Summary:	Header files for graphite2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki graphite2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for graphite2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki graphite2.

%package static
Summary:	Static graphite2 library
Summary(pl.UTF-8):	Statyczna biblioteka graphite2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static graphite2 library.

%description static -l pl.UTF-8
Statyczna biblioteka graphite2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake \
	-DVM_MACHINE_TYPE=direct \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog doc/*.txt
%attr(755,root,root) %{_bindir}/comparerenderer
%attr(755,root,root) %{_bindir}/gr2fonttest
%attr(755,root,root) %{_libdir}/libgraphite2.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libgraphite2.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgraphite2.so
%{_includedir}/graphite2
%{_pkgconfigdir}/graphite2.pc
%{_datadir}/graphite2
