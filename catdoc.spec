%define name catdoc
%define version 0.94.2
%define release %mkrel 1

Summary: Converts MS-Word file to text
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.wagner.pp.ru/pub/catdoc/%{name}-%{version}.tar.gz
Source1: test-catdoc.tar.bz2
Source2: catdoc-charset-from-glibc-charmap.pl
Patch0: catdoc-0.93.4-mandir.patch
Patch1: catdoc-0.93.4-setvbuf-is-dangerous.patch
Patch2: catdoc-0.93.4-cmd-end-of-line-ends-paragraph.patch
License: GPL
Group: Office
URL: http://vitus.wagner.pp.ru/software/catdoc/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: glibc-i18ndata
Requires: tk

%description 
CATDOC is program which reads MS-Word file and prints readable
ASCII text to stdout, just like Unix cat command.
It also able to produce correct escape sequences if some UNICODE
charachers have to be represented specially in your typesetting system
such as (La)TeX.

It features runtime configuration, proper charset handling,
user-definable output formats and support
for Word97 files, which contain UNICODE internally.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_5x --with-install-root="$RPM_BUILD_ROOT" --with-input=cp1252 --with-output=8859-1
%make

zcat /usr/share/i18n/charmaps/MACINTOSH.gz | perl %{SOURCE2} > charsets/cp10000.txt

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/catdoc



%changelog
* Fri May 22 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.94.2-1mdv2010.0
+ Revision: 378612
- Updated to 0.94.2.
  Updated URL.
  Updated patches.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.94-1mdv2008.1
+ Revision: 122999
- kill re-definition of %%buildroot on Pixel's request


* Wed Jul 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.94-1mdk
- New release 0.94
- Drop Patches 1, 3

* Mon Dec 06 2004 Pixel <pixel@mandrakesoft.com> 0.93.4-3mdk
- handle cmd "end-of-line" as \par (was done for \r, but not \n)
- add charset cp10000 (really is macintosh)

* Thu Nov 18 2004 Pixel <pixel@mandrakesoft.com> 0.93.4-2mdk
- handle \handlecpgXXX
- default source_charset is now cp1252 (as it should be (?))
- default target_charset is now 8859-15
- better RTF_UNICODE_CHAR patch
- add test-catdoc.tar.bz2 which contain my tests

* Fri Nov 12 2004 Pixel <pixel@mandrakesoft.com> 0.93.4-1mdk
- new release
- cleanup and adapt 
- fix mandir
- add RTF_UNICODE_CHAR patch to handle a RTF file with a mac charset which has "d\u233\'8etruire"
- uncomment the 
  CONFIGURE_TOP="${CONFIGURE_TOP:-.}"; 
  CFLAGS="${CFLAGS:--O2 -fomit-frame-pointer -pipe -march=i586 -mtune=pentiumpro }" ; export CFLAGS ; 
  CXXFLAGS="${CXXFLAGS:--O2 -fomit-frame-pointer -pipe -march=i586 -mtune=pentiumpro }" ; export CXXFLAGS ; 
  FFLAGS="${FFLAGS:--O2 -fomit-frame-pointer -pipe -march=i586 -mtune=pentiumpro }" ; export FFLAGS ; 
  cputoolize -c $CONFIGURE_TOP ; 
  (cd $CONFIGURE_TOP; [ -f configure.in -o -f configure.ac ] && libtoolize --copy --force) ; 
  [ -f $CONFIGURE_TOP/configure.in -o -f $CONFIGURE_TOP/configure.ac ] && 
  CONFIGURE_XPATH="--x-includes=/usr/X11R6/include --x-libraries=/usr/X11R6/lib" 
  $CONFIGURE_TOP/configure i586-mandriva-linux-gnu \
	--program-prefix= \
 	--prefix=/usr \
	--exec-prefix=/usr \
	--bindir=/usr/bin \
	--sbindir=/usr/sbin \
	--sysconfdir=/etc \
	--datadir=/usr/share \
	--includedir=/usr/include \
	--libdir=/usr/lib \
	--libexecdir=/usr/lib \
	--localstatedir=/var/lib \
	--sharedstatedir=/usr/com \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info \
    $CONFIGURE_XPATH (which still worked !)

* Wed Apr 21 2004 Michael Scherer <misc@mandrake.org> 0.93.1-1mdk 
- 0.93.1
- update Url

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.91.5-4mdk
- rebuild

* Thu Jan 23 2003 lenny@mandrakesoft.com 0.91.5-3mdk
- rebuild

* Thu Nov 21 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.91.5-2mdk
- Fix unpackaged files

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.91.5-1mdk
- 0.91.5

* Sun Jan 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.91.4-1mdk
- updated to 0.91.4

* Fri Jan 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.90.3-4mdk
- rebuild

* Wed Aug 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.90.3-3mdk 
- BM
- macros

* Tue Apr 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.90.3-2mdk
- fix group
- fix files section

* Mon Sep 06 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- First spec file for Mandrake distribution.

