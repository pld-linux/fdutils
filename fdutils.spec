Summary: Floppy utilities.
Name: fdutils
Version: 5.3
Release: 1
Group: Utilities/Disk
Copyright: GPL
Vendor: PLD
Distribution: PLD
URL: http://fdutils.linux.lu
Source: http://fdutils.linux.lu/fdutils-5.3.tar.gz
BuildArch: i386
BuildRoot: /tmp/%{name}-%{version}-root



%description
Utilities for formatting floppies and configuring floppy drive.
Floppies can be formatted up to 1992KB.

%description -l pl
Narzêdzia do formatowania dyskietek oraz do konfiguracji stacji dysków.
Dyskietki mog± byæ formatowane do 1992KB.


%prep
%setup
%build
./configure --prefix=/usr
make

%install
install -d $RPM_BUILD_ROOT/usr/{bin,share{/doc,/man/{man1,man4}}}
install -d $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version} 


install -s src/MAKEFLOPPIES  $RPM_BUILD_ROOT/usr/bin 
install -s src/convertfdprm  $RPM_BUILD_ROOT/usr/bin
install -s src/diskd         $RPM_BUILD_ROOT/usr/bin
install -s src/diskseekd     $RPM_BUILD_ROOT/usr/bin
install -s src/fdmount       $RPM_BUILD_ROOT/usr/bin
install -s src/fdrawcmd      $RPM_BUILD_ROOT/usr/bin
install -s src/floppycontrol $RPM_BUILD_ROOT/usr/bin
install -s src/floppymeter   $RPM_BUILD_ROOT/usr/bin
install -s src/getfdprm      $RPM_BUILD_ROOT/usr/bin
install -s src/setfdprm      $RPM_BUILD_ROOT/usr/bin 
install -s src/superformat   $RPM_BUILD_ROOT/usr/bin
install -s src/xdfcopy       $RPM_BUILD_ROOT/usr/bin

install -s doc/FAQ.html $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install -s doc/README  $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install -s Changelog  $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version} 
install -s CREDITS   $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
           
install -s doc/*.1 $RPM_BUILD_ROOT/usr/share/man/man1/
install -s doc/*.4 $RPM_BUILD_ROOT/usr/share/man/man4/
           

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man*/*
gzip -9nf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
%attr(644,root,root) /usr/share/doc/%{name}-%{version}/*
%attr(644,root,root) /usr/share/man/man*/*
%doc doc/FA*gz doc/READM*gz Changelo*gz CREDIT*gz
