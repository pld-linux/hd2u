Summary:	Converts DOS-style EOLs to UNIX-style EOLs and vice versa
Name:		hd2u
Version:	1.0.1
Release:	0.1
License:	GPL v2
Group:		Applications/Text
Source0:	http://hany.sk/~hany/_data/hd2u/%{name}-%{version}.tgz
# Source0-md5:	dbab0f0c3ee473880ee1fc9740e43515
Patch0:		%{name}-build.patch
URL:		http://hany.sk/~hany/software/hd2u/
BuildRequires:	popt-devel
Provides:	dos2unix
Obsoletes:	dos2unix
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hd2u is "Hany's Dos2Unix convertor". It provides 'dos2unix'.
'dos2unix' is filter used to convert DOS-style EOLs to UNIX-style EOLs
and vice versa (EOL - End Of Line character). Aditionaly it can also
handle files with Macintosh-style EOLs and convert them into other
EOLs.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILD_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dos2unix
