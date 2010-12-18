%define	name	evas
%define version 1.0.0
%define release %mkrel -c beta3 2

%define major 1
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: 	Enlightened canvas library
Name: 		%{name}
Version: 	%{version}
Epoch:		2
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	http://download.enlightenment.org/releases/%{name}-%{version}.beta3.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Conflicts:	%{mklibname evas1}-devel

BuildRequires: 	freetype-devel
BuildRequires: 	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxrender-devel
BuildRequires:	SDL-devel
BuildRequires:	cairo-devel
BuildRequires:	fribidi-devel
BuildRequires:	eina-devel >= 1.0.0
BuildRequires: 	eet-devel >= 1.4.0
BuildRequires:	edb-devel >= 1.0.5.042
BuildRequires:	cairo-devel 
BuildRequires:	png-devel, jpeg-devel 
Buildrequires:	tiff-devel
BuildRequires:	librsvg-devel
Buildrequires:  mesagl-devel
BuildRequires:	ungif-devel, xpm-devel
Buildrequires:	xcb-devel pixman-devel libxcb-util-devel

%description
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary: Enlightened Canvas Libraries
Group: System/Libraries

%description -n %{libname}
Evas canvas libraries.

Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libnamedev
Summary: Enlightened Canvas Library headers and development libraries
Group: System/Libraries
Requires: %{libname} = 2:%{version}
Provides: %{name}-devel = 2:%{version}-%{release}
Conflicts:	%{mklibname evas1}-devel
Obsoletes: %mklibname -d evas 0

%description -n %libnamedev
Evas development headers and development libraries.

%prep
%setup -qn %{name}-%{version}.beta3

%build
%configure2_5x --enable-image-loader-gif \
  --disable-valgrind \
  --enable-image-loader-png \
  --enable-image-loader-jpeg \
  --enable-image-loader-eet \
  --enable-font-loader-eet \
  --enable-image-loader-edb \
  --enable-image-loader-tiff \
  --enable-image-loader-xpm \
  --enable-image-loader-svg \
  --enable-cpu-mmx \
  --enable-cpu-sse \
  --enable-cpu-c \
  --enable-scale-sample \
  --enable-scale-smooth \
  --enable-convert-yuv \
  --enable-small-dither-mask \
  --enable-fontconfig \
  --enable-software-xlib \
  --enable-software-16-x11 \
  --enable-software-xcb \
  --enable-software-sdl \
  --enable-fb \
  --enable-buffer \
  --enable-gl-x11 \
  --disable-gl-glew \
  --enable-xrender-x11 \
  --enable-xrender-xcb \
  --enable-pthreads

# fix libtool issue on release < 2009.1
%if %mdkversion < 200910
perl -pi -e "s/^ECHO.*/ECHO='echo'\necho='echo'\n/" libtool
%endif

%make

%install
rm -fr %buildroot
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/evas
%{_bindir}/evas_cserve
%{_bindir}/evas_cserve_tool

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.%{major}*
%{_libdir}/%name/modules/engines/*/*/*.so
%{_libdir}/%name/modules/loaders/*/*/*.so
%{_libdir}/%name/modules/savers/*/*/*.so

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/libevas.so
%{_libdir}/libevas.*a
%{_libdir}/%name/modules/savers/*/*/*.*a
%{_libdir}/%name/modules/loaders/*/*/*.*a
%{_libdir}/%name/modules/engines/*/*/*.*a
%{_includedir}/*
%{_libdir}/pkgconfig/*
