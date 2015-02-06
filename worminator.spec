Name:		worminator
Version:	3.0R2.1
Release:	8
Summary:	Sidescrolling platform and shoot 'em up action game
Group:		Games/Arcade
License:	GPLv2+
URL:		http://sourceforge.net/projects/worminator/
Source0:	http://download.sourceforge.net/worminator/worminator-%{version}.tar.gz
Source1:	worminator.png
Patch0:		worminator-3.0R2.1-speed.patch
Patch1:		worminator-3.0R2.1-mdv-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	allegro-devel
Requires:	worminator-data >= %{version}

%description
You play as The Worminator and fight your way through many levels of madness
and mayhem. Worminator features nine unique weapons, visible character damage,
full screen scrolling, sound and music, and much more!

%prep
%setup -q
%patch0 -p1 -z .speed
%patch1 -p1 -b .strfmt
sed -i 's/\r//' ReadMe.txt

%build
gcc %{optflags} -fsigned-char -Wno-deprecated-declarations \
  -Wno-char-subscripts -DDATADIR=\"%{_datadir}/%{name}/\" -o %{name} \
  Worminator.c `allegro-config --libs` -lm

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Worminator
Comment=A jump, run and shoot action game
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf %{buildroot}

%post
%{update_icon_cache hicolor}

%postun
%{clean_icon_cache hicolor}

%files
%defattr(-,root,root)
%doc ReadMe.txt changes.unix license.txt license-change.txt
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/worminator.png



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0R2.1-7mdv2011.0
+ Revision: 615460
- the mass rebuild of 2010.1 packages

* Thu Dec 31 2009 Emmanuel Andry <eandry@mandriva.org> 3.0R2.1-6mdv2010.1
+ Revision: 484589
- rebuild for new allegro

* Sat Dec 05 2009 Jérôme Brenier <incubusss@mandriva.org> 3.0R2.1-5mdv2010.1
+ Revision: 473887
- number first patch macro
- fix str fmt
- fix underlinking

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 3.0R2.1-4mdv2009.0
+ Revision: 262149
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 3.0R2.1-3mdv2009.0
+ Revision: 256382
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Oct 27 2007 Adam Williamson <awilliamson@mandriva.org> 3.0R2.1-1mdv2008.1
+ Revision: 102478
- correct group
- spec based on Fedora, thanks
- import worminator


