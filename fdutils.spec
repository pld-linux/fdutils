Summary:	Floppy utilities
Name:		fdutils
Version:	5.3
Release:	1
Group:		Utilities/System
Group(pl):	Narzêdzia/System
License:	GPL
Vendor:		PLD
URL:		http://fdutils.linux.lu
Source0:	http://fdutils.linux.lu/%{name}-%{version}.tar.gz
BuildArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for formatting floppies and configuring floppy drive.
Floppies can be formatted up to 1992KB.

%description -l pl
Narzêdzia do formatowania dyskietek oraz do konfiguracji stacji
dysków. Dyskietki mog± byæ formatowane do 1992KB.


%prep
%setup -q
%build
./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_%{bindir},%{_mandir}/man{1,4}}}

install -s src/MAKEFLOPPIES  $RPM_BUILD_ROOT%{_bindir} 
install -s src/convertfdprm  $RPM_BUILD_ROOT%{_bindir}
install -s src/diskd         $RPM_BUILD_ROOT%{_bindir}
install -s src/diskseekd     $RPM_BUILD_ROOT%{_bindir}
install -s src/fdmount       $RPM_BUILD_ROOT%{_bindir}
install -s src/fdrawcmd      $RPM_BUILD_ROOT%{_bindir}
install -s src/floppycontrol $RPM_BUILD_ROOT%{_bindir}
install -s src/floppymeter   $RPM_BUILD_ROOT%{_bindir}
install -s src/getfdprm      $RPM_BUILD_ROOT%{_bindir}
install -s src/setfdprm      $RPM_BUILD_ROOT%{_bindir} 
install -s src/superformat   $RPM_BUILD_ROOT%{_bindir}
install -s src/xdfcopy       $RPM_BUILD_ROOT%{_bindir}

install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install doc/*.4 $RPM_BUILD_ROOT%{_mandir}/man4/
           
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*
	doc/FAQ.html doc/README Changelog CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*gz
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_datadir}/doc/%{name}-%{version}/*
%{_mandir}/man*/*
