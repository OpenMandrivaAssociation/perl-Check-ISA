%define upstream_name    Check-ISA
%define upstream_version 0.09
Name:		perl-%{upstream_name}
Version:	0.09
Release:	1

Summary:	DWIM, correct checking of an object's class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/manwar/Check-ISA
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Check-ISA-0.09.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::use::ok)

BuildArch:	noarch

%description
This module provides several functions to assist in testing whether a value
is an object, and if so asking about its class.

%prep
%setup -q -n %{upstream_name}-%{version}

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


