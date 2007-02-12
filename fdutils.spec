Summary:	Floppy utilities
Summary(pl.UTF-8):	Narzędzia do dyskietek
Summary(zh_CN.UTF-8):	软盘驱动调试和配置工具
Summary(zh_TW.UTF-8):	[.AN(t$B2N(B]LinuxN$U$B(O%NN3(BnN=L$B*:N$(Bu$B(c*B(B
Name:		fdutils
Version:	5.4
Release:	10
License:	GPL v2
Group:		Applications/System
Source0:	http://fdutils.linux.lu/%{name}-%{version}.tar.gz
# Source0-md5:	17c1df04b1e524078ee52825a5ef5e56
Patch0:		%{name}-manpages.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-ac25x.patch
Patch3:		%{name}-diskd-conflict.patch
Patch4:		%{name}-nodvi.patch
URL:		http://fdutils.linux.lu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for formatting floppies and configuring floppy drive.
Floppies can be formatted up to 1992KB.

%description -l pl.UTF-8
Narzędzia do formatowania dyskietek oraz do konfiguracji stacji
dysków. Dyskietki mogą być formatowane do 1992KB.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
mv -f doc/{,fd}diskd.texi
mv -f doc/{,fd}diskd.1
%patch4 -p1

%build
install /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1,%{_infodir}}

install src/MAKEFLOPPIES  $RPM_BUILD_ROOT%{_bindir}
install src/convertfdprm  $RPM_BUILD_ROOT%{_bindir}
install src/fddiskd       $RPM_BUILD_ROOT%{_bindir}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc doc/README doc/floppy_formats Changelog CREDITS doc/FAQ.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mediaprm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
