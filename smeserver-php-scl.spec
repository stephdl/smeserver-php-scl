Summary: SME server php RH scl
%define name smeserver-php-scl
Name: %{name}
%define version 0.1
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
Requires: php54 , php54-php , php54-php-bcmath, php54-php-dba , php54-php-enchant , php54-php-fpm , php54-php-gd , php54-php-imap , php54-php-intl , php54-php-ldap
Requires: php54-php-mbstring , php54-php-mysqlnd , php54-php-odbc , php54-php-pdo , php54-php-pecl-apc , php54-php-pecl-memcache , php54-php-pecl-zendopcache
Requires: php54-php-pgsql , php54-php-pspell , php54-php-recode , php54-php-snmp , php54-php-soap , php54-php-tidy, php54-php-xmlrpc 
AutoReqProv: no

%changelog
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
$RPM_BUILD_ROOT > %{name}-%{version}-filelist


%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

