%global _with_python3 1

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}

%global _description    \
Most existing Python modules for sending HTTP requests are extremely verbose and    \
cumbersome. Python’s built-in urllib2 module provides most of the HTTP              \
capabilities you should need, but the API is thoroughly broken. This library is     \
designed to make HTTP requests easy for developers.

%global srcname requests

Name:           python-%{srcname}
Version:        2.6.0
Release:        2%{?dist}
Summary:        HTTP library, written in Python, for human beings

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/requests
Source0:        http://pypi.python.org/packages/source/r/requests/requests-%{version}.tar.gz
# Explicitly use the system certificates in ca-certificates.
# https://bugzilla.redhat.com/show_bug.cgi?id=904614
Patch0:         python-requests-system-cert-bundle.patch

# Remove an unnecessary reference to a bundled compat lib in urllib3
Patch1:         python-requests-remove-nested-bundling-dep.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-chardet >= 2.2.1-1
BuildRequires:  python-urllib3 >= 1.10.2-1

Requires:       ca-certificates
Requires:       python-chardet >= 2.2.1-1
Requires:       python-urllib3 >= 1.10.2-1

%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires:  python-ordereddict >= 1.1
Requires:       python-ordereddict >= 1.1
%endif

%description    %{_description}

%package -n python2-%{srcname}
Summary:    %{summary}
%{?python_provide:%python_provide python-%{srcname}}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname} %{_description}
Python 2 version.


%if 0%{?_with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:    %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-chardet
BuildRequires:  python%{python3_pkgversion}-urllib3
Requires:       python%{python3_pkgversion}-chardet
Requires:       python%{python3_pkgversion}-urllib3
## %{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       python%{python3_pkgversion}-%{srcname}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}
Python 3 version.
%endif

%prep
%setup -q -n requests-%{version}

%patch0 -p1
%patch1 -p1

# Unbundle the certificate bundle from mozilla.
rm -rf requests/cacert.pem

%if 0%{?_with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%if 0%{?_with_python3}
pushd %{py3dir}
%{__python3} setup.py build

# Unbundle chardet and urllib3.
rm -rf build/lib/requests/packages/chardet
rm -rf build/lib/requests/packages/urllib3

popd
%endif

%{__python} setup.py build

# Unbundle chardet and urllib3.
rm -rf build/lib/requests/packages/chardet
rm -rf build/lib/requests/packages/urllib3

%install
rm -rf $RPM_BUILD_ROOT
%if 0%{?_with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd
%endif

%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

## The tests succeed if run locally, but fail in koji.
## They require an active network connection to query httpbin.org
#%%check
#%%{__python} test_requests.py
#%%if 0%%{?_with_python3}
#pushd %%{py3dir}
#%%{__python3} test_requests.py
#popd
#%%endif


%files -n python2-%{srcname}
%defattr(-,root,root,-)
%doc NOTICE LICENSE README.rst HISTORY.rst
%{python_sitelib}/*.egg-info
%dir %{python_sitelib}/requests
%{python_sitelib}/requests/*

%if 0%{?_with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/requests/
%endif

%changelog
* Wed Feb 07 2018 SaltStack Packaging Team <packaging@saltstack.com> - 2.6.0-2
- Add support for Python 3

* Wed Jun 03 2015 Matej Stuchlik <mstuchli@redhat.com> - 2.6.0-1
- Update to 2.6.0
Resolves: rhbz#1206465

* Mon Jan 12 2015 Endi S. Dewata <edewata@redhat.com> - 1.1.0-9
- Merged headers with different cases.
Resolves: rhbz#1206465

* Mon Jan 27 2014 Endi S. Dewata <edewata@redhat.com> - 1.1.0-8
- Removed authentication header on redirect.

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.0-7
- Mass rebuild 2013-12-27

* Fri Oct  4 2013 Endi S. Dewata <edewata@redhat.com> - 1.1.0-6
- Removed bundled packages.

* Tue Jun 18 2013 Endi S. Dewata <edewata@redhat.com> - 1.1.0-5
- Fixed bogus date in changelog entry.

* Tue Jun 11 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-4
- Correct a rhel conditional on python-ordereddict

* Thu Feb 28 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-3
- Unbundled python-urllib3.  Using system python-urllib3 now.
- Conditionally include python-ordereddict for el6.

* Wed Feb 27 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Unbundled python-charade/chardet.  Using system python-chardet now.
- Removed deprecated comments and actions against oauthlib unbundling.
  Those are no longer necessary in 1.1.0.
- Added links to bz tickets over Patch declarations.

* Tue Feb 26 2013 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- Latest upstream.
- Relicense to ASL 2.0 with upstream.
- Removed cookie handling patch (fixed in upstream tarball).
- Updated cert unbundling patch to match upstream.
- Added check section, but left it commented out for koji.

* Fri Feb  8 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.14.1-4
- Let brp_python_bytecompile run again, take care of the non-python{2,3} modules
  by removing them from the python{,3}-requests package that they did not belong
  in.
- Use the certificates in the ca-certificates package instead of the bundled one
  + https://bugzilla.redhat.com/show_bug.cgi?id=904614
- Fix a problem with cookie handling
  + https://bugzilla.redhat.com/show_bug.cgi?id=906924

* Mon Oct 22 2012 Arun S A G <sagarun@gmail.com>  0.14.1-1
- Updated to latest upstream release

* Sun Jun 10 2012 Arun S A G <sagarun@gmail.com> 0.13.1-1
- Updated to latest upstream release 0.13.1
- Use system provided ca-certificates
- No more async requests use grrequests https://github.com/kennethreitz/grequests
- Remove gevent as it is no longer required by requests

* Sun Apr 01 2012 Arun S A G <sagarun@gmail.com> 0.11.1-1
- Updated to upstream release 0.11.1

* Thu Mar 29 2012 Arun S A G <sagarun@gmail.com> 0.10.6-3
- Support building package for EL6

* Tue Mar 27 2012 Rex Dieter <rdieter@fedoraproject.org> 0.10.6-2
- +python3-requests pkg

* Sat Mar 3 2012 Arun SAG <sagarun@gmail.com> - 0.10.6-1
- Updated to new upstream version

* Sat Jan 21 2012 Arun SAG <sagarun@gmail.com> - 0.9.3-1
- Updated to new upstream version 0.9.3
- Include python-gevent as a dependency for requests.async
- Clean up shebangs in requests/setup.py,test_requests.py and test_requests_ext.py

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Arun SAG <sagarun@gmail.com> - 0.8.2-1
- New upstream version
- keep alive support
- complete removal of cookiejar and urllib2

* Thu Nov 10 2011 Arun SAG <sagarun@gmail.com> - 0.7.6-1
- Updated to new upstream release 0.7.6

* Thu Oct 20 2011 Arun SAG <sagarun@gmail.com> - 0.6.6-1
- Updated to version 0.6.6

* Fri Aug 26 2011 Arun SAG <sagarun@gmail.com> - 0.6.1-1
- Updated to version 0.6.1

* Sat Aug 20 2011 Arun SAG <sagarun@gmail.com> - 0.6.0-1
- Updated to latest version 0.6.0

* Mon Aug 15 2011 Arun SAG <sagarun@gmail.com> - 0.5.1-2
- Remove OPT_FLAGS from build section since it is a noarch package
- Fix use of mixed tabs and space
- Remove extra space around the word cumbersome in description

* Sun Aug 14 2011 Arun SAG <sagarun@gmail.com> - 0.5.1-1
- Initial package
