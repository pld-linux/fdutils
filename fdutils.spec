Summary:	Floppy utilities
Summary(pl):	Narz�dzia do dyskietek
Name:		fdutils
Version:	5.4
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://fdutils.linux.lu/%{name}-%{version}.tar.gz
Patch0:		%{name}-manpages.patch
Patch1:		%{name}-info.patch
ExclusiveArch:	%{ix86}
BuildRequires:	flex
BuildRequires:	tetex
BuildRequires:	texinfo
URL:		http://fdutils.linux.lu/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for formatting floppies and configuring floppy drive.
Floppies can be formatted up to 1992KB.

%description -l pl
Narz�dzia do formatowania dyskietek oraz do konfiguracji stacji
dysk�w. Dyskietki mog� by� formatowane do 1992KB.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1,%{_infodir}}

install src/MAKEFLOPPIES  $RPM_BUILD_ROOT%{_bindir} 
install src/convertfdprm  $RPM_BUILD_ROOT%{_bindir}
install src/diskd         $RPM_BUILD_ROOT%{_bindir}
install src/diskseekd     $RPM_BUILD_ROOT%{_bindir}
install src/fdmount       $RPM_BUILD_ROOT%{_bindir}
install src/fdrawcmd      $RPM_BUILD_ROOT%{_bindir}
install src/floppycontrol $RPM_BUILD_ROOT%{_bindir}
install src/floppymeter   $RPM_BUILD_ROOT%{_bindir}
install src/getfdprm      $RPM_BUILD_ROOT%{_bindir}
install src/superformat   $RPM_BUILD_ROOT%{_bindir}
install src/xdfcopy       $RPM_BUILD_ROOT%{_bindir}

install src/mediaprm $RPM_BUILD_ROOT%{_sysconfdir}

install doc/fdutils.info* $RPM_BUILD_ROOT%{_infodir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1/
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/setfdprm.1
           
gzip -9nf doc/README doc/floppy_formats Changelog CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fix_info_dir

%postun
%fix_info_dir

%files
%defattr(644,root,root,755)
%doc *.gz doc/*gz doc/FAQ.html
%config %{_sysconfdir}/mediaprm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
