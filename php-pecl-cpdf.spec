%define		_modname	cpdf
%define		_status		beta
Summary:	%{_modname} - extension module for PHP
Summary(pl.UTF-8):	%{_modname} - moduł dla PHP
Name:		php-pecl-%{_modname}
Version:	5.0
%define	subver	rc1
%define	svnver	297236
Release:	0.%{subver}.1
License:	PHP 3.0
Group:		Development/Languages/PHP
# not yet
#Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# svn checkout http://svn.php.net/repository/pecl/cpdf/trunk cpdf
Source0:	%{_modname}-%{version}%{subver}-%{svnver}.tgz
# Source0-md5:	de7b9ac1a9b270036bafd85fa8130315
URL:		http://pecl.php.net/package/cpdf/
BuildRequires:	libcpdf-devel >= 2
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-cpdf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a dynamic shared object (DSO) for PHP that will add PDF
support through libcpdf library.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Moduł PHP dodający obsługę plików PDF poprzez bibliotekę libcpdf.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
