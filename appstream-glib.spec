%define _disable_ld_no_undefined 1

%define major	7
%define gmajor	1.0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d
%define girname	%mklibname %{name}-gir %{gmajor}

%define libnameappstream_builder	%mklibname appstream-builder %{major}
%define girnameappstream_builder	%mklibname appstream-builder-gir %{gmajor}

%define url_ver	%(echo %{version} | cut -d. -f1,2)

Name:		appstream-glib
Version:	0.3.0
Release:	1
Summary:	Library for reading and writing AppStream metadata
Group:		System/Libraries
License:	LGPLv2+
URL:		http://people.freedesktop.org/~hughsient/appstream-glib/
Source0:	http://people.freedesktop.org/~hughsient/appstream-glib/releases/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.1
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libpng16)
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	intltool

%description
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%package -n appstream-util
Summary:	Utility to do simple operations on AppStream metadata
Group:		System/Libraries

%description -n appstream-util
Utility to do simple operations on AppStream metadata.

Sub-commands understood by this utility include: 'install', 'uninstall',
'dump' and 'convert'.

%package -n %{libname}
Summary:	Library for reading and writing AppStream metadata
Group:		System/Libraries
Obsoletes:	%{_lib}appstream-glib1.0_1 < 0.1.1-2
Requires:	%{name}-i18n >= %{version}-%{release}

%description -n %{libname}
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%package -n %{libnameappstream_builder}
Summary:	Library for reading and writing AppStream metadata
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}-%{release}

%description -n %{libnameappstream_builder}
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{_lib}appstream-glib1.0_1 < 0.1.1-2

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{girnameappstream_builder}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libnameappstream_builder} = %{version}-%{release}

%description -n %{girnameappstream_builder}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}appstream-glib1.0-devel < 0.1.1-2

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package i18n
Summary:	Library for reading and writing AppStream metadata - translations
Group:		System/Internationalization
BuildArch:	noarch

%description i18n
This package contains translations used by %{name}.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-rpm
%make

%install
%makeinstall_std

# Remove unwanted la files
find %{buildroot} -name "*.la" -delete

%{find_lang} %{name}

%files -n appstream-util
%{_bindir}/appstream-util
%{_bindir}/appstream-builder
%{_datadir}/bash-completion/completions/appstream-util
%{_datadir}/bash-completion/completions/appstream-builder
%{_libdir}/asb-plugins/libasb_plugin_*.so
%{_mandir}/man1/appstream-builder.1*
%{_mandir}/man1/appstream-util.1*

%files -n %{libname}
%doc AUTHORS NEWS
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*
#%{python3_sitearch}/gi/overrides/*

%files -n %{libnameappstream_builder}
%{_libdir}/libappstream-builder.so.%{major}
%{_libdir}/libappstream-builder.so.%{major}.*

%files -n %{girname}
%{_libdir}/girepository-1.0/AppStreamGlib-%{gmajor}.typelib


%files -n %{girnameappstream_builder}
%{_libdir}/girepository-1.0/AppStreamBuilder-%{gmajor}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/appstream-glib/
%{_includedir}/lib%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/appstream-builder.pc
%{_includedir}/libappstream-builder/
%{_libdir}/libappstream-builder.so
%{_datadir}/gir-1.0/AppStreamGlib-%{gmajor}.gir
%{_datadir}/gir-1.0/AppStreamBuilder-%{gmajor}.gir
%{_datadir}/aclocal/appstream-xml.m4
%{_datadir}/installed-tests/appstream-glib

%files i18n -f %{name}.lang

