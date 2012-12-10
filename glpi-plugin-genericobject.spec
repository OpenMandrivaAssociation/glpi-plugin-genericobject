%if %mandriva_branch == Cooker
%define release %mkrel 2
%else
%define subrel 1
%define release %mkrel 0
%endif

Summary: Add new inventory objects
Name: glpi-plugin-genericobject
Version: 2.0.1
Release: %{release}
License: GPL
Group: Monitoring
Url: https://forge.indepnet.net/projects/show/genericobject/
Source0: https://forge.indepnet.net/attachments/download/993/glpi-genericobject-%{version}.tar.gz
BuildArch: noarch

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
find . -type d | xargs chmod 755

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/genericobject
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/genericobject
rm -rf %{buildroot}%{_datadir}/glpi/plugins/genericobject/docs
rm -f %{buildroot}%{_datadir}/glpi/plugins/genericobject/LICENSE
rm -f %{buildroot}%{_datadir}/glpi/plugins/genericobject/README

%files
%doc docs/* LICENSE README
%{_datadir}/glpi/plugins/genericobject


%changelog
* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-2mdv2012.0
+ Revision: 771128
- various fixes

* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-1
+ Revision: 771089
- 2.0.1

* Sat Jul 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.3-1mdv2011.0
+ Revision: 554621
- import glpi-plugin-genericobject


