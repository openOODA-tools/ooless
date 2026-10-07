Name:           ooless
Version:        0.1.0
Release:        1%{?dist}
Summary:        Memory-bounded interactive terminal pager with regex highlight and jump navigation.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooless
Source0:        ooless-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooless is a sovereign, capability-bounded INTERACTIVE PAGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooless
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooless-uninstall

%files
/usr/bin/ooless
/usr/bin/ooless-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
