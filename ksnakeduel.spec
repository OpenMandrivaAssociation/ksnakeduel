%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		ksnakeduel
Version:	17.08.1
Release:	1
Epoch:		1
Summary:	Snake race played against the computer
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ksnakeduel/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Obsoletes:	kdesnake < 1:4.9.80
Provides:	kdesnake = %{EVRD}
Provides:	ksnake = %{EVRD}
Obsoletes:	ktron
BuildRequires:	cmake ninja cmake(ECM)
BuildRequires:	cmake(KF5Completion) cmake(KF5Config) cmake(KF5ConfigWidgets) cmake(KF5CoreAddons) cmake(KF5Crash) cmake(KF5DBusAddons) cmake(KF5GuiAddons) cmake(KF5I18n) cmake(KF5KDEGames) cmake(KF5WidgetsAddons) cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5Svg) cmake(Qt5Widgets)

%description
KSnakeDuel is a fast action game where you steer a snake which has to eat
food. While eating the snake grows. But once a player collides with the
other snake or the wall the game is lost. This becomes of course more and
more difficult the longer the snakes grow.

%files -f %{name}.lang
%{_sysconfdir}/xdg/ksnakeduel.knsrc
%{_bindir}/ksnakeduel
%{_datadir}/applications/org.kde.ksnakeduel.desktop
%{_datadir}/config.kcfg/ksnakeduel.kcfg
%{_datadir}/ksnakeduel
%{_iconsdir}/hicolor/*/*/ksnakeduel.*    
%{_datadir}/kxmlgui5/ksnakeduel
%{_datadir}/metainfo/*.xml
  
#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
