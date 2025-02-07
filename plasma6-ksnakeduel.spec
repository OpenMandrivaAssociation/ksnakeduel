#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-ksnakeduel
Version:	24.12.2
Release:	%{?git:0.%{git}.}1
Summary:	Snake race played against the computer
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/ksnakeduel/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/ksnakeduel/-/archive/%{gitbranch}/ksnakeduel-%{gitbranchd}.tar.bz2#/ksnakeduel-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/ksnakeduel-%{version}.tar.xz
%endif
Obsoletes:	kdesnake < 1:4.9.80
Provides:	kdesnake = %{EVRD}
Provides:	ksnake = %{EVRD}
Obsoletes:	ktron
BuildRequires:	cmake ninja cmake(ECM)
BuildRequires:	cmake(KF6Completion) cmake(KF6Config) cmake(KF6ConfigWidgets) cmake(KF6CoreAddons) cmake(KF6Crash) cmake(KF6DBusAddons) cmake(KF6GuiAddons) cmake(KF6I18n) cmake(KDEGames6) cmake(KF6WidgetsAddons) cmake(KF6XmlGui) cmake(Qt6Core) cmake(Qt6Gui) cmake(Qt6Svg) cmake(Qt6Widgets) cmake(KF6DocTools)

%description
KSnakeDuel is a fast action game where you steer a snake which has to eat
food. While eating the snake grows. But once a player collides with the
other snake or the wall the game is lost. This becomes of course more and
more difficult the longer the snakes grow.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/ksnakeduel.categories
%{_datadir}/knsrcfiles/ksnakeduel.knsrc
%{_bindir}/ksnakeduel
%{_datadir}/applications/org.kde.ksnakeduel.desktop
%{_datadir}/config.kcfg/ksnakeduel.kcfg
%{_datadir}/ksnakeduel
%{_iconsdir}/hicolor/*/*/ksnakeduel.*    
%{_datadir}/metainfo/*.xml
  
#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n ksnakeduel-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
