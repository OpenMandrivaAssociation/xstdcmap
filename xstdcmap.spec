Name:		xstdcmap
Version:	1.0.1
Release:	%mkrel 5
Summary:	X standard colormap utility
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros	>= 1.1.5
BuildRequires:	libx11-devel	>= 1.1.3
BuildRequires:	libxmu-devel	>= 1.0.3

%description
The xstdcmap utility can be used to selectively define standard
colormap properties. It is intended to be run from a user's X startup
script to create standard colormap definitions in order to facilitate
sharing of scarce colormap resources among clients. Where at all
possible, colormaps are created with read-only allocations.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xstdcmap
%{_mandir}/man1/xstdcmap.1*
