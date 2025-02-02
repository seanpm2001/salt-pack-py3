# Import base config
{% import "setup/redhat/map.jinja" as build_cfg %}

build_base_pkgs:
  pkg.installed:
    - pkgs:
      - python3-gnupg
      - python3-mock


{{build_cfg.build_runas}}:
  user.present:
    - groups:
      - mock
    - require:
      - pkg: build_base_pkgs

##
## Using EPEL-8 dsince now available
##
## mock_file_remove:
##   file.absent:
##     - name: '/etc/mock/epel-8-x86_64.cfg'
## 
## 
## mock_file_create:
##   file.append:
##     - name: '/etc/mock/epel-8-x86_64.cfg'
##     - makedirs: True
##     -  text: |
##         pts['root'] = 'epel-8-x86_64'
##         config_opts['target_arch'] = 'x86_64'
##         config_opts['legal_host_arches'] = ('x86_64',)
##         config_opts['chroot_setup_cmd'] = 'install tar gcc-c++ redhat-rpm-config redhat-release which xz sed make bzip2 gzip gcc coreutils unzip shadow-utils diffutils cpio bash gawk rpm-build info patch util-linux findutils grep'
##         config_opts['dist'] = 'el8'  # only useful for --resultdir variable subst
##         config_opts['extra_chroot_dirs'] = [ '/run/lock', ]
##         config_opts['releasever'] = '8'
##         config_opts['package_manager'] = 'dnf'
##         config_opts['dnf_install_command'] = 'install dnf dnf-plugins-core https://kojipkgs.fedoraproject.org//packages/distribution-gpg-keys/1.26/1.el7/noarch/distribution-gpg-keys-1.26-1.el7.noarch.rpm'
##         config_opts['yum.conf'] = """
##         [main]
##         keepcache=1
##         debuglevel=2
##         reposdir=/dev/null
##         logfile=/var/log/yum.log
##         retries=20
##         obsoletes=1
##         gpgcheck=0
##         assumeyes=1
##         install_weak_deps=0
##         syslog_ident=mock
##         syslog_device=
##         mdpolicy=group:primary
##         best=1
##         metadata_expire=0
##         module_platform_id=platform:el8
##         # repos
##         [base]
##         name= Red Hat Enterprise Linux 8 - BaseOS Beta (RPMs)
##         baseurl=http://downloads.redhat.com/redhat/rhel/rhel-8-beta/baseos/$basearch/
##         gpgkey=file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         gpgcheck=1
##         skip_if_unavailable=False
##         #
##         [rhel-8-baseos-beta-source-rpms]
##         name = Red Hat Enterprise Linux 8 - BaseOS Beta (Source RPMs)
##         baseurl = https://downloads.redhat.com/redhat/rhel/rhel-8-beta/baseos/source/
##         enabled = 0
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         #
##         [rhel-8-appstream-beta-source-rpms]
##         name = Red Hat Enterprise Linux 8 - AppStream Beta (Source RPMs)
##         baseurl =
##         https://downloads.redhat.com/redhat/rhel/rhel-8-beta/appstream/source/
##         enabled = 0
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         #
##         [rhel-8-appstream-beta-rpms]
##         name = Red Hat Enterprise Linux 8 - AppStream Beta (RPMs)
##         baseurl =
##         https://downloads.redhat.com/redhat/rhel/rhel-8-beta/appstream/$basearch/
##         enabled = 1
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         #
##         [rhel-8-add-ons--ha-beta-source-rpms]
##         name = Red Hat Enterprise Linux 8 - HighAvailability Beta (Source RPMs)
##         baseurl =
##         https://downloads.redhat.com/redhat/rhel/rhel-8-beta/add-ons/ha/source/
##         enabled = 0
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         #
##         [rhel-8-add-ons--ha-beta-rpms]
##         name = Red Hat Enterprise Linux 8 - HighAvailability Beta (RPMs)
##         baseurl =
##         https://downloads.redhat.com/redhat/rhel/rhel-8-beta/add-ons/ha/$basearch/
##         enabled = 0
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         #
##         [rhel-8-add-ons--rs-beta-source-rpms]
##         name = Red Hat Enterprise Linux 8 - ResilientStorage Beta (Source RPMs)
##         baseurl =
##         https://downloads.redhat.com/redhat/rhel/rhel-8-beta/add-ons/rs/source/
##         enabled = 0
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         #
##         [rhel-8-add-ons--rs-beta-rpms]
##         name = Red Hat Enterprise Linux 8 - ResilientStorage Beta (RPMs)
##         baseurl =
##         https://downloads.redhat.com/redhat/rhel/rhel-8-beta/add-ons/rs/$basearch/
##         enabled = 0
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         #
##         [rhel-8-add-ons--rt-beta-source-rpms]
##         name = Red Hat Enterprise Linux 8 - RT Beta (Source RPMs)
##         baseurl =
##         https://downloads.redhat.com/redhat/rhel/rhel-8-beta/add-ons/rt/source/
##         enabled = 0
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
## 
##         [rhel-8-add-ons--rt-beta-rpms]
##         name = Red Hat Enterprise Linux 8 - RT Beta (RPMs)
##         baseurl =
##         https://downloads.redhat.com/redhat/rhel/rhel-8-beta/add-ons/rt/$basearch/
##         enabled = 0
##         gpgcheck = 1
##         gpgkey =
##         file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-beta,file:///usr/share/distribution-gpg-keys/redhat/RPM-GPG-KEY-redhat8-release
##         """
## 
