%define upstream_name    Check-ISA
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:    5

Summary:	DWIM, correct checking of an object's class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Check/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::use::ok)

BuildArch:	noarch

%description
This module provides several functions to assist in testing whether a value
is an object, and if so asking about its class.

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
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 654889
- rebuild for updated spec-helper

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 505424
- rebuild using %%perl_convert_version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2010.0
+ Revision: 440538
- rebuild

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 300709
- import perl-Check-ISA


* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
- initial mdv release, generated with cpan2dist
