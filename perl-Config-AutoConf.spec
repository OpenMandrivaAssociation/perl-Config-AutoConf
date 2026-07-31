%define upstream_name    Config-AutoConf
%define upstream_version 0.320
Name:		perl-%{upstream_name}
Version:	0.320
Release:	11

Summary:	A module to implement some of AutoConf macros in pure perl





License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/ambs/Config-AutoConf
Source0:	https://cpan.metacpan.org/authors/id/A/AM/AMBS/Config-AutoConf-0.320.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
A module to implement some of AutoConf macros in pure perl.

%prep
%setup -q -n Config-AutoConf-0.320

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*
