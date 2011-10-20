#BEGIN_dontchangeme
%define pythontest %{?pyver:0}%{!?pyver:1}
%if %pythontest
	%define pyver 2.5
%endif
%global __python /usr/bin/python%{pyver}
%define pyver_no_dot %(echo %pyver | tr -d ".")
%define python_package python%{pyver_no_dot}
%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

# Turn off the brp-python-bytecompile script, we'll invoke it again later.
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
#END_dontchangeme

%define libname zendesk
%define name %{python_package}-%{libname}
%define packagever 1.1.0

Summary: Python Zendesk is wrapper for the Zendesk API.
Name: %{name}
Version: %{packagever}
Release: 1.demonware
License: DemonWare
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: %{python_package}

#Source0: %{source}
Source0: %{name}.tar.gz

Requires: %{python_package}
Requires: %{python_package}-httplib2
Requires: %{python_package}-simplejson

%description
Python Zendesk is wrapper for the Zendesk API. This library provides an
easy and flexible way for developers to communicate with their Zendesk
account in their application.

%prep
%setup -n %name

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# Bytecompile with a specific version of Python.
/usr/lib/rpm/brp-python-bytecompile %{__python}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/Zendesk-%{version}-py%{pyver}.egg-info
%{python_sitelib}/%{libname}

%changelog
* Mon Feb 21 2011 Jonathan Frawley <jonathan@demonware.net> - 1.demonware
- Initial build.
