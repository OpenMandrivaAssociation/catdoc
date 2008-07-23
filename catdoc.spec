%define name catdoc
%define version 0.94
%define release %mkrel 3

Summary: Converts MS-Word file to text
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.45.free.net/pub/catdoc/%{name}-%{version}.tar.bz2
Source1: test-catdoc.tar.bz2
Source2: catdoc-charset-from-glibc-charmap.pl
Patch0: catdoc-0.93.4-mandir.patch
#Patch1: catdoc-0.93.4-fix-wordview-charset_lib.patch.bz2
Patch2: catdoc-0.93.4-setvbuf-is-dangerous.patch
#Patch3: catdoc-0.93.4-RTF-CODEPAGE.patch.bz2
Patch4: catdoc-0.93.4-RTF_UNICODE_CHAR.patch
Patch5: catdoc-0.93.4-cmd-end-of-line-ends-paragraph.patch
License: GPL
Group: Office
URL: http://www.45.free.net/~vitus/ice/catdoc/
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

%setup
%patch0 -p1
#%patch1 -p1
%patch2 -p1
#%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoconf
%configure --with-install-root="$RPM_BUILD_ROOT" --with-input=cp1252 --with-output=8859-1
%make

zcat /usr/share/i18n/charmaps/MACINTOSH.gz | perl %{SOURCE2} > charsets/cp10000.txt

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/catdoc

