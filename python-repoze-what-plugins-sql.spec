%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define rcver rc1

Name:           python-repoze-what-plugins-sql
Version:        1.0
Release:        0.6.%{rcver}%{?dist}
Summary:        The repoze.what SQL plugin

Group:          Development/Languages
License:        BSD
URL:            http://code.gustavonarea.net/repoze.what.plugins.sql/
Source0:        http://pypi.python.org/packages/source/r/repoze.what.plugins.sql/repoze.what.plugins.sql-%{version}%{rcver}.tar.gz
Patch0:         %{name}-setuptools.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools-devel python-nose
BuildRequires:  python-nose python-coverage
BuildRequires:  python-repoze-what 
BuildRequires:  python-sqlalchemy >= 0.5

Requires:       python-repoze-what >= 1.0.3
Requires:       python-sqlalchemy >= 0.5
Requires:       python-zope-interface
Requires:       python-repoze-who-plugins-sa

%description
This is an adapters and extras plugin for repoze.what.

The SQL plugin makes repoze.what support sources defined in SQLAlchemy-managed
databases by providing one group adapter, one permission adapter and one
utility to configure both in one go (optionally, when the group source and the
permission source have a relationship).

This plugin also defines repoze.what.plugins.quickstart.


%prep
%setup -q -n repoze.what.plugins.sql-%{version}%{rcver}
%patch0 -p0 -b .setuptools


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


#%check
#PYTHONPATH=$(pwd) nosetests


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitelib}/*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.5.rc1
- Remove the sqlalchemy0.5 requirement for rawhide

* Wed Jun 17 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.4.rc1
- Require python-sqlalchemy0.5

* Fri Jun 05 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.3.rc1
- Patch our setup.py to use our own setuptools package

* Sat May 30 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.2.rc1
- Update to 1.0rc1

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.0-0.1.a1.r3024
- Initial package for Fedora
