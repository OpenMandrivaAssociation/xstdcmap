Name:		xstdcmap
Version:	1.0.3
Release:	1
Summary:	X standard colormap utility
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xmu)
BuildRequires: x11-util-macros >= 1.0.1

%description
The xstdcmap utility can be used to selectively define standard
colormap properties. It is intended to be run from a user's X startup
script to create standard colormap definitions in order to facilitate
sharing of scarce colormap resources among clients. Where at all
possible, colormaps are created with read-only allocations.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xstdcmap
%{_mandir}/man1/xstdcmap.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 671369
- mass rebuild

* Mon Sep 27 2010 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 581414
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdv2010.1
+ Revision: 524471
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 350755
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 226087
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 154298
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 80777
- rebuild for 2008
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

