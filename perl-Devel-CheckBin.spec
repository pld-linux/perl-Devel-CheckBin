#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Devel
%define		pnam	CheckBin
%include	/usr/lib/rpm/macros.perl
Summary:	Devel::CheckBin - check that a command is available
Summary(pl.UTF-8):	Devel::CheckBin - sprawdzanie dostępności polecenia
Name:		perl-Devel-CheckBin
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aaa02a1262bc3eb3a7e5566590cb7814
URL:		http://search.cpan.org/dist/Devel-CheckBin/
BuildRequires:	perl-Module-Build >= 0.38
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Devel/CheckBin.pm
%{_mandir}/man3/Devel::CheckBin.3pm*
