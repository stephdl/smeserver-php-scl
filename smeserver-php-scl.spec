Summary: SME server php REMI scl
%define name smeserver-php-scl
Name: %{name}
%define version 0.4
%define release 1
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
Requires: php54 , php54-php , php54-php-bcmath , php54-php-gd , php54-php-imap , php54-php-ldap , php54-php-enchant
Requires: php54-php-mbstring , php54-php-pdo , php54-php-tidy , php54-php-mysqlnd php54-php-pecl-zip
Requires: php55 , php55-php , php55-php-bcmath , php55-php-gd , php55-php-imap , php55-php-ldap , php55-php-enchant
Requires: php55-php-mbstring , php55-php-pdo , php55-php-tidy , php55-php-mysqlnd
Requires: php56 , php56-php , php56-php-bcmath , php56-php-gd , php56-php-imap , php56-php-ldap , php56-php-enchant
Requires: php56-php-mbstring , php56-php-pdo , php56-php-tidy , php56-php-mysqlnd

AutoReqProv: no

%changelog
* Sat Feb 07 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.4-1
- Switch to remi repository {php54,php55,php56}

* Sun Nov 9 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.3-3
- Added a db to load the php54-mod in apache
- New php settings in php.ini
- Added default db values

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
    --file /usr/bin/phpscl/php54_REMI 'attr(0770,root,www)' \
    --file /usr/bin/phpscl/php55_REMI 'attr(0770,root,www)' \
    --file /usr/bin/phpscl/php56_REMI 'attr(0770,root,www)' \
  $RPM_BUILD_ROOT > %{name}-%{version}-filelist


%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

