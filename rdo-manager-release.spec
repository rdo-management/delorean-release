Name:           rdo-manager-release
Version:        kilo
Release:        1
Summary:        Delorean and RDO Management Delorean repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/rdo-management/rdo-manager-release
Source:         %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       yum-utils

%description
This package configures both the core delorean and rdo-management-delorean repositories

%install
%{__install} -p -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/rdo-manager-release.repo

%files
%{_sysconfdir}/yum.repos.d/*.repo

%post


%changelog
* Mon Apr 20 2015 Mike Burns <mburns@redhat.com> kilo-2
- rebrand to rdo-manager-release

* Thu Mar 12 2015 Ryan Brady <rbrady@redhat.com> kilo-1
- new package built with tito




