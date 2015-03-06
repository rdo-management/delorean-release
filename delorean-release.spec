Name:           delorean-release
Version:        kilo.0.4
Release:        1
Summary:        Delorean and RDO Management Delorean repository configuration

Group:          System Environment/Base
License:        Apache2

Source0:        delorean-repo.spec
URL:            https://github.com/rdo-management/delorean-release

BuildArch:      noarch

Requires:       yum-utils

%description
This package configures both the delorean and rdo-management-delorean repositories

%prep
# intentionally blank

%build
# intentionally blank

%pre
# intentionally blank

%install
# intentionally blank

%files
# intentionally blank

%post
# Install repo file for Delorean master packages
# Pin to an older repo for now because newer openstack-keystone requires a
# newer and not yet avaialable python-pycadf.
export DELOREAN_REPO=${DELOREAN_REPO:-"http://104.130.230.24/centos70/05/d8/05d8a6b82bf1f16c064bbee84d95c88b73030fae_3ea5fe35/delorean.repo"}
curl -o /etc/yum.repos.d/delorean.repo $DELOREAN_REPO

# Install repo file for Delorean el7 midstream packages built from
# rdo-management.
export DELOREAN_RHEL7_REPO=${DELOREAN_RHEL7_REPO:-"http://trunk-mgt.rdoproject.org/repos/current/delorean.repo"}
curl -o /etc/yum.repos.d/delorean-rdo-management.repo $DELOREAN_RHEL7_REPO
# We can't have 2 yum repos called delorean though, so we must rename this one
sed -i 's/delorean/delorean-rdo-management/' /etc/yum.repos.d/delorean-rdo-management.repo

# delorean-rdo-management should default to priority=1
sudo sed -i "s/priority=1/priority=2/" /etc/yum.repos.d/delorean.repo



%changelog
* Fri Mar 06 2015 Ryan Brady <rbrady@redhat.com> kilo.0.4-1
- Added %%files section (rbrady@redhat.com)
- Added back source line (rbrady@redhat.com)

* Fri Mar 06 2015 Ryan Brady <rbrady@redhat.com> kilo.0.3-1
- changed the section where the repo files are downloaded. (rbrady@redhat.com)

* Fri Mar 06 2015 Ryan Brady <rbrady@redhat.com> kilo.0.2-1
- removed uneeded Source tag. (rbrady@redhat.com)

* Thu Mar 05 2015 Ryan Brady <rbrady@redhat.com> kilo-1
- new package built with tito


