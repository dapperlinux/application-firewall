Summary:    Application level firewall for gnome-shell
Name:       application-firewall
Version:    1
Release:    2

Group:      System Environment/Base
License:    BSD
Url:        https://github.com/subgraph/fw-daemon
Source0:    %{name}-%{version}.tar.xz
BuildArch:  x86_64

BuildRequires:  go
Requires:   libnetfilter_queue
Requires:   libnetfilter_queue-devel
BuildRequires:  libnetfilter_queue
BuildRequires:  libnetfilter_queue-devel
Requires:   cairo-gobject
BuildRequires:  cairo-gobject-devel
BuildRequires:  gtk3-devel


%description
Application firewall notifies the user when an application attempts to make an unknown network
request. Intergrates into gnome-shell, and the user and select to approve requests forever, for 
this session, and as a system rule.

%prep
%autosetup

%build
mkdir -p %{_builddir}/gocode/src/github.com/subgraph/
mv fw-daemon %{_builddir}/gocode/src/github.com/subgraph/
export GOPATH=%{_builddir}/gocode
go build github.com/subgraph/fw-daemon
go build github.com/subgraph/fw-daemon/fw-settings


%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/dbus-1/system.d/
mkdir -p %{buildroot}/lib/systemd/system
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/extensions
install -m 755 fw-daemon %{buildroot}%{_sbindir}
install -m 755 fw-settings %{buildroot}%{_bindir}
mv %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/gnome-shell/firewall@subgraph.com %{buildroot}%{_datarootdir}/gnome-shell/extensions
cp %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/etc/dbus-1/system.d/com.subgraph.Firewall.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d/
cp %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/lib/systemd/system/fw-daemon.service %{buildroot}/lib/systemd/system/



%clean

%pre

%post
systemctl enable fw-daemon.service
systemctl start fw-daemon.service

%files
%{_sbindir}/fw-daemon
%{_bindir}/fw-settings
%{_sysconfdir}/dbus-1/system.d/com.subgraph.Firewall.conf
/lib/systemd/system/fw-daemon.service
%{_datarootdir}/gnome-shell/extensions/firewall@subgraph.com/*

%changelog
* Sun Dec  4 2016 Matthew Ruffell <msr50@uclive.ac.nz>
- First packaging
