#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooseX
%define		pnam	POE
%include	/usr/lib/rpm/macros.perl
Summary:	MooseX::POE - The Illicit Love Child of Moose and POE
#Summary(pl.UTF-8):	
Name:		perl-MooseX-POE
Version:	0.214
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	64f18c2b742e43de6ce787a9ed739dc1
URL:		http://search.cpan.org/dist/MooseX-POE/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Moose) >= 0.90
BuildRequires:	perl(POE) >= 1.004
BuildRequires:	perl(Test::Fatal) >= 0.003
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MooseX::POE is a Moose wrapper around a POE::Session.

# %description -l pl.UTF-8
# TODO

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
%doc Changes README
%{perl_vendorlib}/MooseX/*.pm
%{perl_vendorlib}/MooseX/POE
%{_mandir}/man3/*
