%define upstream_name    Config-AutoConf
%define upstream_version 0.22

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A module to implement some of AutoConf macros in pure perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/Config-AutoConf-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
A module to implement some of AutoConf macros in pure perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.160.0-3mdv2011.0
+ Revision: 657769
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 594402
- update to new version 0.16

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 517111
- update to 0.15

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 515674
- import perl-Config-AutoConf


* Mon Mar 08 2010 cpan2dist 0.14-1mdv
- initial mdv release, generated with cpan2dist

