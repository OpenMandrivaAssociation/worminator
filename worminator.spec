Name:		worminator
Version:	3.0R2.1
Release:	%mkrel 3
Summary:	Sidescrolling platform and shoot 'em up action game
Group:		Games/Arcade
License:	GPLv2+
URL:		http://sourceforge.net/projects/worminator/
Source0:	http://download.sourceforge.net/worminator/worminator-%{version}.tar.gz
Source1:	worminator.png
Patch0:		worminator-3.0R2.1-speed.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	allegro-devel
Requires:	worminator-data >= %{version}

%description
You play as The Worminator and fight your way through many levels of madness
and mayhem. Worminator features nine unique weapons, visible character damage,
full screen scrolling, sound and music, and much more!

%prep
%setup -q
%patch -p1 -z .speed
sed -i 's/\r//' ReadMe.txt

%build
gcc %{optflags} -fsigned-char -Wno-deprecated-declarations \
  -Wno-char-subscripts -DDATADIR=\"%{_datadir}/%{name}/\" -o %{name} \
  Worminator.c `allegro-config --libs`

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

