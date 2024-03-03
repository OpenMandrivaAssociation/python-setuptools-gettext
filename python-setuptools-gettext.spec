%define pypi_name setuptools-gettext

Name:           python-%{pypi_name}
Version:        0.1.11
Release:        1
Summary:        Widget to display page-based documents for Qt5/PyQt5
Group:          Development/Python
License:        GPLv3+ AND GPLv2+
# https://github.com/frescobaldi/qpageview
URL:            https://qpageview.org/
Source0:        https://files.pythonhosted.org/packages/source/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

Provides:       %{pypi_name} = %{version}-%{release}

%description
The qpageview module provides a page based document viewer widget
for Qt5/PyQt5.
It has a flexible architecture potentionally supporting many
formats. Currently, it supports SVG documents, images, and,
using the Poppler-Qt5 binding, PDF documents.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py_build

%install
%py_install

%files 
%{python_sitelib}/setuptools_gettext*
