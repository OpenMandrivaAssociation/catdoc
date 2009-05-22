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

