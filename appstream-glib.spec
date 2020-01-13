%define _disable_ld_no_undefined 1
%define api 5
%define major 8
%define gmajor 1.0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define girname %mklibname %{name}-gir %{gmajor}
%define url_ver	%(echo %{version} | cut -d. -f1,2)
%global optflags %{optflags} -I%{_includedir}/libstemmer

Name:		appstream-glib
Version:	0.7.16.20200113
Release:	1
Summary:	Library for reading and writing AppStream metadata
Group:		System/Libraries
License:	LGPLv2+
Url:		http://people.freedesktop.org/~hughsient/appstream-glib/
Source0:	https://github.com/hughsie/appstream-glib/archive/master/appstream-glib-master.tar.gz

BuildRequires:	meson
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.1
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0) >= 1.1.1
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libpng16)
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(libgcab-1.0)
BuildRequires:  pkgconfig(popt)
BuildRequires:	pkgconfig(rpm)
BuildRequires:	libstemmer-devel
BuildRequires:	gcab
BuildRequires:	gperf
#BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl

%description
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%package -n appstream-util
Summary:	Utility to do simple operations on AppStream metadata
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n appstream-util
Utility to do simple operations on AppStream metadata.

Sub-commands understood by this utility include: 'install', 'uninstall',
'dump' and 'convert'.

%files -n appstream-util
%{_bindir}/appstream-util
%{_bindir}/appstream-builder
%{_bindir}/appstream-compose
%{_datadir}/bash-completion/completions/appstream-util
%{_datadir}/bash-completion/completions/appstream-builder
%{_libdir}/asb-plugins-%{api}/libasb_plugin_*.so
%{_mandir}/man1/appstream-builder.1*
%{_mandir}/man1/appstream-util.1*
%{_mandir}/man1/appstream-compose.1*

#---------------------------------------------
%package -n %{libname}
Summary:	Library for reading and writing AppStream metadata
Group:		System/Libraries
Requires:	%{name}-i18n >= %{EVRD}
Obsoletes:	%{mklibname appstream-builder 8} < 0.7.15
Provides:	%{mklibname appstream-builder 8} = 0.7.15

%description -n %{libname}
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

#---------------------------------------------
%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{mklibname appstream-builder-gir 1.0} < 0.7.15
Provides:	%{mklibname appstream-builder-gir 1.0} = 0.7.15

%description -n %{girname}
GObject Introspection interface description for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/AppStreamGlib-%{gmajor}.typelib

#---------------------------------------------
%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -n %{devname}
%{_includedir}/lib%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/AppStreamGlib-%{gmajor}.gir
%{_datadir}/aclocal/appstream-xml.m4
%{_datadir}/aclocal/appdata-xml.m4
%{_datadir}/installed-tests/appstream-glib
%{_datadir}/gettext/its/appdata.its
%{_datadir}/gettext/its/appdata.loc
#---------------------------------------------

%package i18n
Summary:	Library for reading and writing AppStream metadata - translations
Group:		System/Internationalization
BuildArch:	noarch

%description i18n
This package contains translations used by %{name}.

%files i18n -f %{name}.lang

#---------------------------------------------

%prep
%autosetup -p1 -n appstream-glib-master
%meson \
  -Dgtk-doc=false \
  -Dstemmer=true \
  -Ddep11=true

%build
%meson_build

%install
%meson_install

%{find_lang} %{name}
