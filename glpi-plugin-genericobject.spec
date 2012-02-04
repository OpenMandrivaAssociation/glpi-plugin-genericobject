%define name glpi-plugin-genericobject
%define version 2.0.1
%define release %mkrel 1

Summary: Add new inventory objects
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/show/genericobject/
Source0: https://forge.indepnet.net/attachments/download/993/glpi-genericobject-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This plugin allows you to add new inventory types without programmation. It
manages :
- Type creation
- Available fields
- Framework integration (Helpdesk, loans, templates, etc.)
- Integration with the file injection plugin

%prep
%setup -q -n genericobject
find . -type f | xargs chmod 644

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/genericobject
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/genericobject

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/glpi/plugins/genericobject
