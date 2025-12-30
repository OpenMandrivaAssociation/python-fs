# Created by pyp2rpm-3.3.2
%global pypi_name fs

Name:           python-%{pypi_name}
Version:        2.4.16
Release:        4
Summary:        Python's filesystem abstraction layer
Group:          Development/Python
License:        MIT
URL:            https://www.pyfilesystem.org/
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  locales

BuildRequires:  python-devel
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(backports.os)
#BuildRequires:  python3dist(mock)
#BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pyftpdlib)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(scandir)
BuildRequires:  python3dist(pysendfile)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%description
Work with files and directories in archives, memory, the cloud etc. as easily
as your local drive. Write code now, decide later where the data will be
stored; unit test without writing real files; upload files to the cloud
without learning a new API; sandbox your file writing code; etc.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

perl -pi -e 's/~=/>=/g' setup.py

%build
%py_build

%install
%py_install

%check
export LC_ALL=C.UTF-8
#{__python} setup.py test

%files
%license LICENSE
%doc README.md
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
