Name:           delorean-release
Version:        kilo
Release:        1
Summary:        Delorean and RDO Management Delorean repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            https://github.com/rdo-management/delorean-release
Source0:        delorean-release.repo

BuildArch:      noarch

Requires:       yum-utils

%description
This package configures both the delorean and rdo-management-delorean repositories

%install
%{__install} -p -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/delorean-release.repo

%files
%{_sysconfdir}/yum.repos.d/*.repo

%post
# Install repo file for Delorean master packages
# Pin to an older repo for now because newer openstack-keystone requires a
# newer and not yet avaialable python-pycadf.
export DELOREAN_REPO=${DELOREAN_REPO:-"http://104.130.230.24/centos70/05/d8/05d8a6b82bf1f16c064bbee84d95c88b73030fae_3ea5fe35/delorean.repo"}
curl -o /etc/yum.repos.d/delorean.repo $DELOREAN_REPO

# delorean-rdo-management should default to priority=1
sudo sed -i "s/priority=1/priority=2/" /etc/yum.repos.d/delorean.repo


%changelog
* Thu Mar 12 2015 Ryan Brady <rbrady@redhat.com>
- changed install to %%{__install} (rbrady@redhat.com)

* Thu Mar 12 2015 Ryan Brady <rbrady@redhat.com> kilo-1
- added additional changes to get a successful build (rbrady@redhat.com)

* Thu Mar 12 2015 Ryan Brady <rbrady@redhat.com>
- added additional changes to get a successful build (rbrady@redhat.com)

* Wed Mar 11 2015 Ryan Brady <rbrady@redhat.com> kilo.0.6-1
- added files to spec (rbrady@redhat.com)

* Wed Mar 11 2015 Ryan Brady <rbrady@redhat.com> kilo.0.5-1
- Added repo file for delorean-rdo-management to be more similar to rdo-release
  (rbrady@redhat.com)
- additional changes (rbrady@redhat.com)

* Fri Mar 06 2015 Ryan Brady <rbrady@redhat.com> kilo.0.4-1
- Added %%files section (rbrady@redhat.com)
- Added back source line (rbrady@redhat.com)

* Fri Mar 06 2015 Ryan Brady <rbrady@redhat.com> kilo.0.3-1
- changed the section where the repo files are downloaded. (rbrady@redhat.com)

* Fri Mar 06 2015 Ryan Brady <rbrady@redhat.com> kilo.0.2-1
- removed uneeded Source tag. (rbrady@redhat.com)

* Thu Mar 05 2015 Ryan Brady <rbrady@redhat.com> kilo-1
- new package built with tito


