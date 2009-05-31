Name:           kdenlive
Version:        0.7.4
Release:        2%{?dist}
Summary:        Non-linear video editor
License:        GPLv2+
Group:          Applications/Multimedia
URL:            http://www.kdenlive.org
Source:         http://downloads.sourceforge.net/kdenlive/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  kdelibs-devel
BuildRequires:  mlt-devel
BuildRequires:  soprano-devel
BuildRequires: desktop-file-utils
Requires:       recordmydesktop
Requires:       dvgrab
Requires:       ffmpeg
Requires:       dvdauthor


%description
Kdenlive is an intuitive and powerful multi-track video editor, including most
recent video technologies.


%prep
%setup -q

%build
%cmake_kde4
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mv effects/README README.effects

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_kde4_datadir}/applications/kde4/%{name}.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_kde4_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_kde4_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_kde4_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :


%posttrans
gtk-update-icon-cache %{_kde4_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README*
%{_kde4_bindir}/*
%{_kde4_datadir}/applications/kde4/%{name}.desktop
%{_kde4_libdir}/kde4/*.so
%{_kde4_datadir}/config.kcfg/*
%{_kde4_configdir}/*
%{_kde4_datadir}/mime/packages/*
%{_kde4_appsdir}/%{name}
%{_kde4_datadir}/kde4/services/westleypreview.desktop
%{_kde4_datadir}/icons/hicolor/*
%{_kde4_datadir}/icons/oxygen/*
%{_mandir}/man1/*.gz

%changelog
* Sat May 30 2009 Zarko <zarko.pintar@gmail.com> - 0.7.4-2
- added updating of mime database
- changed dir of .desktop file

* Fri May 22 2009 Zarko <zarko.pintar@gmail.com> - 0.7.4-1
- new release
- spec cleaning

* Thu Apr 16 2009 Zarko <zarko.pintar@gmail.com> - 0.7.3-2
- some clearing
- added doc files

* Wed Apr 15 2009 Zarko <zarko.pintar@gmail.com> - 0.7.3-1
- new release

* Sun Apr 12 2009 Zarko <zarko.pintar@gmail.com> - 0.7.2.1-2
- spec convert to kde4 macros

* Mon Mar 16 2009 Zarko <zarko.pintar@gmail.com> - 0.7.2.1-1
- update to 0.7.2.1
- spec cleaned
- Resolve RPATHs

* Sun Nov 16 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7-1
- update to 0.7

* Wed Nov  5 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7-0.1.20081104svn2622
- update to last svn revision

* Tue Nov  4 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7-0.beta1
- clean up spec

* Fri Oct 17 2008 jeff <moe@blagblagblag.org> - 0.7-1.beta1
- Add URL
- Full URL for Source:
- Remove all Requires:
- Update BuildRoot
- Remove Packager: Brixton Linux Action Group
- Add BuildRequires: ffmpeg-devel kdebindings-devel soprano-devel
- Update %%files
- %%doc with only effects/README
- GPLv2+
- Add lang files

* Tue Jul  8 2008 jeff <moe@blagblagblag.org> - 0.6-1.svn2298.0blag.f9
- Update to KDE4 branch
  https://kdenlive.svn.sourceforge.net/svnroot/kdenlive/branches/KDE4

* Tue Jul  8 2008 jeff <moe@blagblagblag.org> - 0.6-1.svn2298.0blag.f9
- Update to svn r2298
- New Requires
- kdenlive-svn-r2298-renderer-CMakeLists.patch 

* Sun Nov 11 2007 jeff <moe@blagblagblag.org> - 0.5-1blag.f7
- Update to 0.5 final

* Tue Apr 17 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070417.0blag.fc6
- svn to 20070417

* Fri Apr  6 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070406.0blag.fc6
- svn to 20070406

* Tue Apr  3 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070403.0blag.fc6
- svn to 20070403

* Thu Mar 22 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070322.0blag.fc6
- svn to 20070322

* Thu Mar 15 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070316.0blag.fc6
- BLAG'd

* Sun Apr 27 2003 Jason Wood <jasonwood@blueyonder.co.uk> 0.2.2-1mdk
- First stab at an RPM package.
- This is taken from kdenlive-0.2.2 source package.
