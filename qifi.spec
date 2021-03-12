%define debug_package %{nil}

%define mybuildnumber %{?build_number}%{?!build_number:1}

Name:           qifi
Version:        0.1
Release:        %{mybuildnumber}%{?dist}
Summary:        Create Wi-Fi QR codes
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/Rudd-O/%{name}
Source0:        https://github.com/Rudd-O/%{name}/archive/{%version}.tar.gz#/%{name}-%{version}.tar.gz

Requires:       python3
Requires:       qrencode
BuildRequires:  coreutils

%description
This program creates Wi-Fi network QR codes for you.

%prep
%setup -q

%build
true

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 -T %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%attr(0755, root, root) %{_bindir}/%{name}


%changelog
* Fri Mar 12 2021 Manuel Amador (Rudd-O) <rudd-o@rudd-o.com>
- Initial release.
