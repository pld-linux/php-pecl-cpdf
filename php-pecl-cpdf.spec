%define		_modname	cpdf
%define		_status		stable

Summary:	%{_modname} - extension module for PHP
Summary(pl):	%{_modname} - modu³ dla PHP
Name:		php-pecl-%{_modname}
Version:	2.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	ee90a55b753975faac607f4230ece2b4
URL:		http://pecl.php.net/package/cpdf/
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This is a dynamic shared object (DSO) for PHP that will add PDF
support through libcpdf library.

In PECL status of this extension is: %{_status}.

%description -l pl
Modu³ PHP dodaj±cy obs³ugê plików PDF poprzez bibliotekê libcpdf.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
