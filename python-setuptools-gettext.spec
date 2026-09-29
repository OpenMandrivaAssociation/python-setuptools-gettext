%define pypi_name setuptools-gettext
%define oname setuptools_gettext

Name:		python-%{pypi_name}
Summary:	Setuptools gettext extension plugin
Version:	0.1.19
Release:	1
Group:		Development/Python
License:	GPL-2.0-or-later
URL:		https://github.com/breezy-team/setuptools-gettext
Source0:	https://files.pythonhosted.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Provides:	%{pypi_name} = %{EVRD}
Provides:	python%{pyver}dist(setuptools-gettext) = %{EVRD}

%description
Setuptools gettext extension plugin. It adds the build_mo, clean_mo, install_mo
and update_pot distutils commands, registers a file finder that picks up .po
files, and reads the [tool.setuptools-gettext] table in pyproject.toml so that
translations are compiled with msgfmt and installed under share/locale.

%files
%doc README.md
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
