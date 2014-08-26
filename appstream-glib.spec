%define major	1
%define gmajor	1.0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d
%define girname	%mklibname %{name}-gir %{gmajor}

%define url_ver	%(echo %{version} | cut -d. -f1,2)

Name:		appstream-glib
Version:	0.2.5
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
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libpng16)

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

%description -n %{libname}
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

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# Remove unwanted la files
find %{buildroot} -name "*.la" -delete

%files -n appstream-util
%{_bindir}/appstream-util

%files -n %{libname}
%doc AUTHORS NEWS
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*
#%{python3_sitearch}/gi/overrides/*

%files -n %{girname}
%{_libdir}/girepository-1.0/AppStreamGlib-%{gmajor}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/appstream-glib/
%{_includedir}/lib%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/AppStreamGlib-%{gmajor}.gir


%changelog
* Wed May 28 2014 wally <wally> 0.1.6-1.mga5
+ Revision: 627255
- new version 0.1.6
- split out utility to own subpkg

* Wed May 28 2014 wally <wally> 0.1.1-2.mga5
+ Revision: 627245
- fix lib and devel pkg names and summaries
- split out gir typelib
- don't own gtk-doc dir

* Wed Mar 26 2014 ovitters <ovitters> 0.1.1-1.mga5
+ Revision: 608729
- imported package appstream-glib

