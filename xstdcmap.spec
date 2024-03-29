Name:		xstdcmap
Version:	1.0.5
Release:	2
Summary:	X standard colormap utility
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xorg-macros)

%description
The xstdcmap utility can be used to selectively define standard
colormap properties. It is intended to be run from a user's X startup
script to create standard colormap definitions in order to facilitate
sharing of scarce colormap resources among clients. Where at all
possible, colormaps are created with read-only allocations.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xstdcmap
%doc %{_mandir}/man1/xstdcmap.1*
