Summary:	ftpcopy - a tool for create and maintain a FTP mirror
Summary(pl):	ftpcopy - narzêdzie do tworzenia i uaktualniania mirrora FTP
Name:		ftpcopy
Version:	0.6.7
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	ftp://www.ohse.de/uwe/ftpcopy/%{name}-%{version}.tar.gz
# Source0-md5:	78d5245970803230f0f22f0f040a58ef
URL:		http://www.ohse.de/uwe/ftpcopy.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ftpcopy is a simple FTP client written to copy files or directories
(recursively) from a FTP server. It was written to mirror FTP sites
which support the EPLF directory listing format, but it also supports
the traditional listing format /bin/ls and may also be used to simply
copy files. I supports IPv4 and IPv6.

%description -l pl
ftpcopy jest prostym klientem FTP kopiuj±cym pliki i katalogi
(uaktualniaj±c) z serwera FTP. Zosta³ napisany z my¶l± o mirrorowaniu
serwerów FTP, które wspieraj± format listowania katalogów EPLF, lecz
wspiera te¿ tradycyjny format, /bin/ls . Mo¿na go równie¿ u¿ywaæ do
zwyk³ego kopiowania plików. Obs³uguje protoko³y IPv4 oraz IPv6.

%prep
%setup -q -n web

%build
cd %{name}-%{version}
package/compile
package/check

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cd %{name}-%{version}
install command/* $RPM_BUILD_ROOT%{_bindir}
install doc/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
