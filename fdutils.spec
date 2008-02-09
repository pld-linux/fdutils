Summary:	Floppy utilities
Summary(pl.UTF-8):	Narzędzia do dyskietek
Summary(zh_CN.UTF-8):	软盘驱动调试和配置工具
Name:		fdutils
Version:	5.5
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: http://fdutils.linux.lu/download.html
Source0:	http://fdutils.linux.lu/%{name}-%{version}.tar.gz
# Source0-md5:	2b8b65f52378158a4a21e455566b456d
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-diskd-conflict.patch
Patch3:		%{name}-nodvi.patch
Patch4:		http://fdutils.linux.lu/fdutils-5.5-20060227.diff.gz
URL:		http://fdutils.linux.lu/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	texinfo
# setfdprm used to be in util-linux before
Conflicts:	util-linux < 2.13-0.pre7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for formatting floppies and configuring floppy drive.
Floppies can be formatted up to 1992KB.

Note: the fdutils are meant to control a legacy (FDC-based) floppy
drive. They won't work with other types of floppy drives (such as
LS-120, USB floppy drives). For USB floppy drives use ufiformat
package to format a floppy.

%description -l pl.UTF-8
Narzędzia do formatowania dyskietek oraz do konfiguracji stacji
dysków. Dyskietki mogą być formatowane do 1992KB.

Uwaga: fdutils są przeznaczone do sterowania tradycyjnymi stacjami
dyskietek (opartymi na FDC). Nie będą działać z innymi rodzajami
stacji, takimi jak LS-120 czy podłączane przez USB. Do formatowania
dyskietek w stacjach podłączanych przez USB służy pakiet ufiformat.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp -f /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# in man-pages
rm $RPM_BUILD_ROOT%{_mandir}/man4/fd.4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc doc/README doc/floppy_formats Changelog CREDITS doc/FAQ.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mediaprm
%attr(755,root,root) %{_bindir}/MAKEFLOPPIES
%attr(755,root,root) %{_bindir}/diskseekd
%attr(755,root,root) %{_bindir}/fddiskd
%attr(755,root,root) %{_bindir}/fdlist
%attr(755,root,root) %{_bindir}/fdmount
%attr(755,root,root) %{_bindir}/fdmountd
%attr(755,root,root) %{_bindir}/fdrawcmd
%attr(755,root,root) %{_bindir}/fdumount
%attr(755,root,root) %{_bindir}/floppycontrol
%attr(755,root,root) %{_bindir}/floppymeter
%attr(755,root,root) %{_bindir}/getfdprm
%attr(755,root,root) %{_bindir}/setfdprm
%attr(755,root,root) %{_bindir}/superformat
%attr(755,root,root) %{_bindir}/xdfcopy
%attr(755,root,root) %{_bindir}/xdfformat
%{_mandir}/man1/makefloppies.1*
%{_mandir}/man1/diskseekd.1*
%{_mandir}/man1/fddiskd.1*
%{_mandir}/man1/fdlist.1*
%{_mandir}/man1/fdmount.1*
%{_mandir}/man1/fdmountd.1*
%{_mandir}/man1/fdrawcmd.1*
%{_mandir}/man1/fdumount.1*
%{_mandir}/man1/floppycontrol.1*
%{_mandir}/man1/floppymeter.1*
%{_mandir}/man1/getfdprm.1*
%{_mandir}/man1/setfdprm.1*
%{_mandir}/man1/superformat.1*
%{_mandir}/man1/xdfcopy.1*
%{_mandir}/man1/xdfformat.1*
%{_infodir}/fdutils.info*
