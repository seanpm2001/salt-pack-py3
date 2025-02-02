%global srcname pyroute2
%global sum Pure Python netlink library

%bcond_with python2
%bcond_without python3

%{!?python3_pkgversion:%global python3_pkgversion 3}

Name: python-%{srcname}
Version: 0.4.13
Release: 3%{?dist}
Summary: %{sum}
License: GPLv2+
Group: Development/Languages
URL: https://github.com/svinota/%{srcname}

BuildArch: noarch
%if %{with python2}
BuildRequires: python2-devel
%endif
%if %{with python3}
BuildRequires: python%{python3_pkgversion}-devel
%endif
Source: https://pypi.io/packages/source/p/pyroute2/pyroute2-%{version}.tar.gz

%description
PyRoute2 provides several levels of API to work with Netlink
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,
IPQ.

%if %{with python2}
%package -n python2-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
PyRoute2 provides several levels of API to work with Netlink
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,
IPQ.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
PyRoute2 provides several levels of API to work with Netlink
protocols, such as Generic Netlink, RTNL, TaskStats, NFNetlink,
IPQ.
%endif


%prep
%setup -q -n %{srcname}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{srcname}
%doc README* LICENSE.GPL.v2 LICENSE.Apache.v2
%{python2_sitelib}/%{srcname}*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%doc README* LICENSE.GPL.v2 LICENSE.Apache.v2
%{python3_sitelib}/%{srcname}*
%endif


%changelog
* Wed May 08 2019 SaltStack Packaging Team <packaging@saltstack.com> - 0.4.13-3
- Added support for Redhat 8, and support for Python 2 packages optional

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 0.4.13-2
- Rebuilt to change main python from 3.4 to 3.6

* Tue Mar  7 2017 Antoni S. Puimedon <antonisp@celebdor.com> 0.4.13-1
- upgrade to 0.4.13
- ipset hash:mac support
- ipset: hash:mac support
- ipset: list:set support
- ifinfmsg: allow absolute/relative paths in the net_ns_fd NLA
- ipdb: #322 -- IPv6 updates on interfaces in DOWN state
- rtnl: #284 -- support vlan_flags
- ipdb: #307 -- fix IPv6 routes management
- ipdb: #311 -- vlan interfaces address loading
- iprsocket: #305 -- support NETLINK_LISTEN_ALL_NSID

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.10-2
- Rebuild for Python 3.6

* Fri Oct 14 2016 Peter V. Saveliev <peter@svinota.eu> 0.4.10-1
- devlink fd leak fix

* Thu Oct  6 2016 Peter V. Saveliev <peter@svinota.eu> 0.4.9-1
- critical fd leak fix
- initial NETLINK_SOCK_DIAG support

* Tue Sep 27 2016 Peter V. Saveliev <peter@svinota.eu> 0.4.8-1
- uplift to 0.4.x

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.19-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr  5 2016 Peter V. Saveliev <peter@svinota.eu> 0.3.19-1
- separate Python2 and Python3 packages
- MPLS lwtunnel support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-2

- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Fri Nov 20 2015 Peter V. Saveliev <peter@svinota.eu> 0.3.15-1
- critical NetNS fd leak fix

* Tue Sep  1 2015 Peter V. Saveliev <peter@svinota.eu> 0.3.14-1
- bogus rpm dates in the changelog are fixed
- both licenses added

* Tue Sep  1 2015 Peter V. Saveliev <peter@svinota.eu> 0.3.13-1
- BPF filters support
- MPLS routes support
- MIPS platform support
- multiple improvements on iwutil
- memory consumption improvements

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan  8 2015 Peter V. Saveliev <peter@svinota.eu> 0.3.4-1
- Network namespaces support
- Veth, tuntap
- Route metrics

* Fri Dec  5 2014 Peter V. Saveliev <peter@svinota.eu> 0.3.3-1
- Fix-ups, 0.3.3
- Bugfixes for Python 2.6

* Tue Nov 18 2014 Peter V. Saveliev <peter@svinota.eu> 0.3.2-1
- Update to 0.3.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Jiri Pirko <jpirko@redhat.com> - 0.2.7-1
- Update to 0.2.7

* Thu Aug 22 2013 Peter V. Saveliev <peet@redhat.com> 0.1.11-1
- IPRSocket threadless objects
- rtnl: tc filters improvements

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Peter V. Saveliev <peet@redhat.com> 0.1.10-1
- fd and threads leaks fixed
- shutdown sequence fixed (release() calls)
- ipdb: interface removal
- ipdb: fail on transaction sync timeout

* Tue Jun 11 2013 Peter V. Saveliev <peet@redhat.com> 0.1.9-2
- fedpkg import fix

* Tue Jun 11 2013 Peter V. Saveliev <peet@redhat.com> 0.1.9-1
- several races fixed
- Python 2.6 compatibility issues fixed

* Wed Jun 05 2013 Peter V. Saveliev <peet@redhat.com> 0.1.8-1
- initial RH build

