Summary: Japanese dictionary for GNOME.
Name: gjiten
Version: 2.6
Release: 1
License: GPL
Group: Productivity/Office/Dictionary
Group: X11/Applications
Source: gjiten-2.6.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Packager: Botond Botyanszki <b0ti@users.sourceforge.net>
URL: http://gjiten.sourceforge.net
BuildRequires: scrollkeeper

%description
Gjiten is a Japanese dictionary program for GNOME. It also has a kanji 
dictionary; any combination of stroke number, radicals and search key can be
used for kanji lookups. Requires dictionary files in edict format and a
working X Input Method [eg. kinput2] for Japanese input.

See http://gjiten.sourceforge.net for dictionary files and updates.

%prep
%setup

%build
%configure
make

%install
if [ -d $RPM_BUILD_ROOT ] ; then rm -rf $RPM_BUILD_ROOT; fi
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

mv $RPM_BUILD_ROOT%{_docdir}/gjiten/* .
rmdir $RPM_BUILD_ROOT%{_docdir}/gjiten/
rm -rf $RPM_BUILD_ROOT/var/scrollkeeper

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
SCHEMAS="gjiten.schemas gjiten-dicfiles.schemas"
for S in $SCHEMAS; do 
  gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/$S >/dev/null
done
update-desktop-database %{_datadir}/applications
scrollkeeper-update

%postun
update-desktop-database %{_datadir}/applications
scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc README COPYING TODO AUTHORS INSTALL NEWS ChangeLog gjiten-doc.ja.html
%{_bindir}/gjiten
%{_mandir}/man1/*
%{_datadir}/pixmaps/*
%{_datadir}/gjiten/*
%{_datadir}/applications/gjiten.desktop
%{_datadir}/application-registry/gjiten.applications
%{_datadir}/gnome/help/gjiten
%{_datadir}/omf/gjiten
%{_datadir}/locale/*
%{_sysconfdir}/gconf/schemas/*.schemas
