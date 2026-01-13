#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Devel
%define		pnam	CheckBin
Summary:	Devel::CheckBin - check that a command is available
Summary(pl.UTF-8):	Devel::CheckBin - sprawdzanie dostępności polecenia
Name:		perl-Devel-CheckBin
Version:	0.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	042b68e48d9b53de7d3ef4c726d57cb2
URL:		https://metacpan.org/dist/Devel-CheckBin
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.64
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.98
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::CheckBin is a Perl module that checks whether a particular
command is available.

%description -l pl.UTF-8
Devel::CheckBin to moduł Perla sprawdzający, czy dane polecenie jest
dostępne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Devel/CheckBin.pm
%{_mandir}/man3/Devel::CheckBin.3pm*
