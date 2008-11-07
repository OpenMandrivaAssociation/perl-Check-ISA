%define module   Check-ISA
%define version    0.04
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    DWIM, correct checking of an object's class
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Check/%{module}-%{version}.tar.gz
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::use::ok)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module provides several functions to assist in testing whether a value
is an object, and if so asking about its class.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


