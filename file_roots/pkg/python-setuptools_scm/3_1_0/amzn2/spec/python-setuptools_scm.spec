%global srcname setuptools_scm

%bcond_with python2
%bcond_without python3

%{!?python3_pkgversion:%global python3_pkgversion 3}

%if ( "0%{?dist}" == "0.amzn2" )
%global with_amzn2 1
%bcond_with tests
%else
%bcond_without tests
%endif


Name:           python-%{srcname}
Version:        3.1.0
Release:        3%{?dist}
Summary:        Blessed package to manage your versions by scm tags

License:        MIT
URL:            https://pypi.python.org/pypi/setuptools_scm
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if %{with tests}
BuildRequires:  git-core
BuildRequires:  mercurial
%endif

%description
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python2-rpm-macros
BuildRequires:  python-devel
%else
BuildRequires:  python2-devel
%endif
BuildRequires:  python2-setuptools
%if %{with tests}
BuildRequires:  python2-pytest
%endif
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%if 0%{?with_amzn2}
BuildRequires:  python3-rpm-macros
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Obsoletes:      platform-python-%{srcname} < %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.
%endif

%prep
%autosetup -n %{srcname}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
## %%py3_build
## amzn2 has issue with %{py_setup} expansion
CFLAGS="%{optflags}" %{__python3} setup.py %{?py_setup_args} build --executable="%{__python3} %{py3_shbang_opts}" %{?*}
sleep 1
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
## %%py3_install
## amzn2 has issue with %{py_setup} expansion
CFLAGS="%{optflags}" %{__python3} setup.py %{?py_setup_args} install -O1 --skip-build --root %{buildroot} %{?*}
%endif

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v -k 'not (test_pip_download or test_old_setuptools_fails or test_old_setuptools_allows_with_warnings or test_distlib_setuptools_works)'
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python3_version} -v -k 'not (test_pip_download or test_old_setuptools_fails or test_old_setuptools_allows_with_warnings or test_distlib_setuptools_works)'
%endif


%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-*.egg-info/
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info
%endif

%changelog
* Mon Jun 17 2019 SaltStack Packaging Team <packaging@saltstack.com> - 3.1.0-3
- Made support for Python 2 optional

* Wed Oct 10 2018 SaltStack Packaging Team <packaging@saltstack.com> - 3.1.0-2
- Support for Python 3 on Amazon Linux 2

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Sun Jul 29 2018 Orion Poplawski <orion@nwra.com> - 3.0.4-1
- Update to 3.0.4
- Re-enable tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Bootstrap for Python 3.7

* Mon May 14 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.15.7-1
- Update to 1.15.7

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.15.6-7
- Use better Obsoletes for platform-python

* Fri Nov 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.15.6-6
- Remove platform-python subpackage

* Thu Aug 24 2017 Miro Hrončok <mhroncok@redhat.com> - 1.15.6-5
- Rebuilt for rhbz#1484607

* Sun Aug 20 2017 Tomas Orsava <torsava@redhat.com> - 1.15.6-4
- Re-enable tests to finish bootstrapping the platform-python stack
  (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Aug 10 2017 Lumír Balhar <lbalhar@redhat.com> - 1.15.6-3
- Add subpackage for platform-python
- Disable tests so platform-python stack can be bootstrapped
  (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Orion Poplawski <orion@cora.nwra.com> - 1.15.6-1
- Update to 1.15.6

* Mon Apr 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.15.5-1
- Update to 1.15.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Kevin Fenzi <kevin@scrye.com> - 1.15.0-1
- Update to 1.15.0

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.13.0-2
- Rebuild for Python 3.6

* Mon Oct 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.13.0-1
- Update to 1.13.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-2
- No python2 package on EPEL (setuptools too old)

* Thu Dec 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-1
- Update to 1.10.1

* Wed Dec 2 2015 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-1
- Update to 1.9.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-2
- Cleanup stray .pyc files from tests

* Sat Sep 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-1
- Update to 1.8.0
- Fix license tag

* Mon Sep 14 2015 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-1
- Initial package
