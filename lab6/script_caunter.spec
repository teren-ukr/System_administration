Name:           script_caunter
Version:        1.0
Release:        1%{?dist}
Summary:        Example script

License:        GPL
Source0:        %{name}.sh

%description
This is an example script.

%prep

%build

%install
install -D -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/%{name}.sh

%files
/usr/local/bin/%{name}.sh

%changelog
* Thu Dec 26 2024 TEREN88 https://github.com/teren-ukr/System_administration - 1.0-1
- Initial package
