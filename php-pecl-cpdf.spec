%define		php_name	php%{?php_suffix}
%define		modname	cpdf
%define		status		beta
%define		subver	rc1
%define		svnver	297236
Summary:	%{modname} - extension module for PHP
Summary(pl.UTF-8):	%{modname} - moduł dla PHP
Name:		%{php_name}-pecl-%{modname}
Version:	5.0
Release:	0.%{subver}.2
License:	PHP 3.0
Group:		Development/Languages/PHP
# not yet
#Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# svn checkout http://svn.php.net/repository/pecl/cpdf/trunk cpdf
Source0:	%{modname}-%{version}%{subver}-%{svnver}.tgz
# Source0-md5:	de7b9ac1a9b270036bafd85fa8130315
URL:		http://pecl.php.net/package/cpdf/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	libcpdf-devel >= 2
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	%{php_name}-cpdf
Provides:	php(%{modname}) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a dynamic shared object (DSO) for PHP that will add PDF
support through libcpdf library.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Moduł PHP dodający obsługę plików PDF poprzez bibliotekę libcpdf.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -q -c

%build
cd %{modname}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p %{modname}/modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
