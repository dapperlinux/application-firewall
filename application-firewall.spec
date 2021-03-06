%define debug_package %{nil}

Summary:    Application level firewall for gnome-shell
Name:       application-firewall
Version:    1
Release:    17

Group:      System Environment/Base
License:    BSD
Url:        https://github.com/subgraph/fw-daemon
Source0:    %{name}-%{version}.tar.xz
BuildArch:  x86_64

BuildRequires:  go
BuildRequires:  libnetfilter_queue
BuildRequires:  libnetfilter_queue-devel
BuildRequires:  cairo-gobject-devel
BuildRequires:  gtk3-devel
Requires:   libnetfilter_queue
Requires:   libnetfilter_queue-devel
Requires:   cairo-gobject
Requires: iptables-services


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
mkdir -p %{buildroot}%{_datarootdir}/dbus-1/services
mkdir -p %{buildroot}%{_datarootdir}/dbus-1/system-services
mkdir -p %{buildroot}%{_datarootdir}/gnome-shell/extensions
mkdir -p %{buildroot}%{_sysconfdir}/sgfw
mkdir -p %{buildroot}%{_datarootdir}/applications
install -m 755 fw-daemon %{buildroot}%{_sbindir}
install -m 755 fw-settings %{buildroot}%{_bindir}
install -m 644 %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/etc/sgfw/sgfw.conf %{buildroot}%{_sysconfdir}/sgfw
mv %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/gnome-shell/firewall@subgraph.com %{buildroot}%{_datarootdir}/gnome-shell/extensions
cp %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/etc/dbus-1/system.d/com.subgraph.Firewall.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d/
cp %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/etc/dbus-1/system.d/com.subgraph.fwprompt.EventNotifier.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d/
cp %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/lib/systemd/system/fw-daemon.service %{buildroot}/lib/systemd/system/
cp %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/usr/share/dbus-1/services/com.subgraph.FirewallPrompt.service %{buildroot}%{_datarootdir}/dbus-1/services
cp %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/usr/share/dbus-1/system-services/com.subgraph.Firewall.service %{buildroot}%{_datarootdir}/dbus-1/system-services
cp %{_builddir}/gocode/src/github.com/subgraph/fw-daemon/sources/usr/share/applications/subgraph-firewall.desktop %{buildroot}%{_datarootdir}/applications



%clean

%pre

%post
# Install IPTables rules
iptables -t mangle -A OUTPUT -m conntrack --ctstate NEW -j NFQUEUE --queue-num 0 --queue-bypass
iptables -A INPUT -p udp -m udp --sport 53 -j NFQUEUE --queue-num 0 --queue-bypass
iptables -A OUTPUT -p tcp -m mark --mark 0x1 -j LOG
iptables -A OUTPUT -p tcp -m mark --mark 0x1 -j REJECT --reject-with icmp-port-unreachable
# Make the rules persistent
service iptables save

systemctl enable fw-daemon.service
systemctl start fw-daemon.service

%preun
systemctl stop fw-daemon.service
systemctl disable fw-daemon.service

# Delete IPTables rules
iptables -D OUTPUT -m conntrack --ctstate NEW -j NFQUEUE --queue-num 0 --queue-bypass
iptables -D INPUT -p udp -m udp --sport 53 -j NFQUEUE --queue-num 0 --queue-bypass
iptables -D OUTPUT -p tcp -m mark --mark 0x1 -j LOG
iptables -D OUTPUT -p tcp -m mark --mark 0x1 -j REJECT --reject-with icmp-port-unreachable
# Make the rules persistent
service iptables save

%files
%{_sbindir}/fw-daemon
%{_bindir}/fw-settings
%{_sysconfdir}/dbus-1/system.d/com.subgraph.Firewall.conf
%{_sysconfdir}/dbus-1/system.d/com.subgraph.fwprompt.EventNotifier.conf
%{_sysconfdir}/sgfw/sgfw.conf
/lib/systemd/system/fw-daemon.service
%{_datarootdir}/dbus-1/services/com.subgraph.FirewallPrompt.service
%{_datarootdir}/dbus-1/system-services/com.subgraph.Firewall.service
%{_datarootdir}/gnome-shell/extensions/firewall@subgraph.com/*
%{_datarootdir}/applications/subgraph-firewall.desktop

%changelog
* Sun Oct 29 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Fixed bugs in .service and gnome-shell extension, added iptables rules to .spec

* Wed Sep 27 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Merging in new fw-daemon and resyncing to upstream

* Mon Feb 13 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Adding in /usr/share/dbus-1/system-services/com.subgraph.FirewallPrompt.service file

* Thu Feb  2 2017 Matthew Ruffell <msr50@uclive.ac.nz>
- Adding in /etc/sgfw/sgfw.conf file

* Sun Dec  4 2016 Matthew Ruffell <msr50@uclive.ac.nz>
- First packaging
