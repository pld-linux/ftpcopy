Summary:	ftpcopy is a tool for create and maintain a ftp mirror.
Summary(pl):	ftpcopy jest narzêdziem do utwórzenia i uaktualniania mirrora ftp.
Name:		ftpcopy
Version:	0.6.4
Release:	1
License:	GPL v.2
Group:		Applications/Networking
Source0:	ftp://www.ohse.de/uwe/ftpcopy/%{name}-%{version}.tar.gz
# Source0-md5:	e6883a23ef664c059d9d0d34eb1501cd
URL:		http://www.ohse.de/uwe/ftpcopy.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ftpcopy is a simple FTP client written to copy files or directories
(recursively) from a FTP server. It was written to mirror FTP sites
which support the EPLF directory l isting format, but it also supports
the traditional listing format /bin/ls) And may also be used to simply
copy files.

%description -l pl
ftpcopy jest prostym klijentem FTP kopjuj±cum pliki i katalogi
(uaktualniaj±c) z servera FTP. Obs³uguje protoko³y IPv4 oraz IPv6.

%define 	_package	package/

%prep
%setup -q -n web/%{name}-%{version}
%{_package}compile
%{_package}check

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install command/* $RPM_BUILD_ROOT%{_bindir}/
install doc/*	$RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
