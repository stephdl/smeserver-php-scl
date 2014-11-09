Summary: SME server php RH scl
%define name smeserver-php-scl
Name: %{name}
%define version 0.3
%define release 2
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Administration
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/e-smith-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: x86_64
Requires: e-smith-release >= 9.0
Requires: scl-utils
Requires: php54 , php54-php-bcmath , php54-php-gd , php54-php-imap , php54-php-ldap , php54-php-enchant
Requires: php54-php-mbstring , php54-php-pdo , php54-php-tidy , php54-php-mysqlnd
Requires: php55 , php55-php-bcmath , php55-php-gd , php55-php-imap , php55-php-ldap , php55-php-enchant
Requires: php55-php-mbstring , php55-php-pdo , php55-php-tidy , php55-php-mysqlnd
AutoReqProv: no

%changelog
* Sun Nov 9 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.3-2
- Added a db to load the php54-mod in apache
- New php settings in php.ini

* Fri Nov 7 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.2-1
- Added php55

* Fri Nov 7 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1-1
- Initial release to sme9

%description
Allow to use different versions of php whith a cgi script.

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist \
    --file /usr/bin/phpscl/php54_RHSCL 'attr(0770,root,www)' \
    --file /usr/bin/phpscl/php55_RHSCL 'attr(0770,root,www)' \
  $RPM_BUILD_ROOT > %{name}-%{version}-filelist


%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

