Summary:	ftpcopy is a tool for create and maintain a ftp mirror
Summary(pl):	ftpcopy jest narz�dziem do utw�rzenia i uaktualniania mirrora ftp
Name:		ftpcopy
Version:	0.6.4
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	ftp://www.ohse.de/uwe/ftpcopy/%{name}-%{version}.tar.gz
# Source0-md5:	e6883a23ef664c059d9d0d34eb1501cd
URL:		http://www.ohse.de/uwe/ftpcopy.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ftpcopy is a simple FTP client written to copy files or directories
(recursively) from a FTP server. It was written to mirror FTP sites
which support the EPLF directory listing format, but it also supports
the traditional listing format /bin/ls and may also be used to simply
copy files. I supports IPv4 and IPv6.

%description -l pl
ftpcopy jest prostym klientem FTP kopiuj�cum pliki i katalogi
(uaktualniaj�c) z servera FTP. Zosta� napisany z my�l� o mirrorowaniu
serwer�w FTP, kt�re wspieraj� format listowania katalog�w EPLF, lecz
wspiera te� tradycyjny format, /bin/ls . Mo�na go r�wnie� u�ywa� do
zwyk�ego kopiowania plik�w. Obs�uguje protoko�y IPv4 oraz IPv6.

%prep
%setup -q -n web/%{name}-%{version}
package/compile
package/check

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install command/* $RPM_BUILD_ROOT%{_bindir}
install doc/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
