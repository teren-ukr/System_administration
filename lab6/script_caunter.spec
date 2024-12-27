Name:           script_caunter
Version:        1.0
Release:        1%{?dist}
Summary:        Example script


Source0:        ../script_caunter.sh


%description
This is an example script for demonstration purposes.

%prep

%build

%install
install -D -m 0755 %{_sourcedir}/../script_caunter.sh %{buildroot}/usr/local/bin/script_caunter.sh


%files
%license LICENSE
/usr/local/bin/script_caunter.sh

%changelog
* Thu Dec 26 2024 TEREN88 https://github.com/teren-ukr/System_administration - 1.0-1
- Initial package
