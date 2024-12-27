Name:           script-caunter
Version:        1.0
Release:        1%{?dist}
Summary:        Simple script for counting

License:        GPL
URL:            http://example.com/script-caunter
Source0:        script_caunter.sh

BuildArch:      x86_64


%description
A simple counting script.

%prep
# nothing to prep

%build
# no build step required

%install
install -D -m 755 %{SOURCE0} %{buildroot}%{_bindir}/script_caunter.sh

%files
%{_bindir}/script_caunter.sh

%changelog
* Thu Dec 26 2024 TEREN88 https://github.com/teren-ukr/System_administration - 1.0-1
- Initial package
